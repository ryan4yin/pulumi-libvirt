Pulumi Provider for Libvirt
======

![master branch status](https://github.com/ryan4yin/pulumi-libvirt/workflows/master/badge.svg)
[![PYPI Version](https://img.shields.io/pypi/v/pulumi_libvirt.svg)](https://pypi.org/project/pulumi_libvirt/)

A Pulumi provider that lets you provision servers on a libvirt host via pulumi.


Based on [dmacvicar/terraform-provider-libvirt](https://github.com/dmacvicar/terraform-provider-libvirt)

## Warning

**WARNING: This repository are now deprecated since an Official Provider [pulumi/pulumi-libvirt](https://github.com/pulumi/pulumi-libvirt) is available.**

but the examples in this README is still usable with the offical provider, as the offical provider is also based on [dmacvicar/terraform-provider-libvirt](https://github.com/dmacvicar/terraform-provider-libvirt).

## Installation

1. Resources plugin for Linux are available as tarballs in the [release](https://github.com/ryan4yin/pulumi-libvirt/releases) page.
1. Follow the installation instructions in release page to install the resource plugin and the python sdk.
1. for other languages, ​​please install sdk from source in the `sdk` folder.

## Build and Install the provider From Source

In order to properly build the sdks, the following tools are expected:
- `pulumictl` (See the project's README for installation instructions: https://github.com/pulumi/pulumictl)

other complie requirements:

1. [libvirt](https://libvirt.org/downloads.html) 1.2.14 or newer development headers
1. `cgo` is required by the [libvirt-go](https://github.com/libvirt/libvirt-go) package. `export CGO_ENABLED="1"`

runtime requirements:

1. libvirt daemon 1.2.14 or newer
1. `mkisofs` is required to use the [CloudInit](https://github.com/dmacvicar/terraform-provider-libvirt/blob/master/website/docs/r/cloudinit.html.markdown)

to build all the sdks, you need install and set up all the 4 language sdks first: go/dotnet/python/nodejs.

then use the following command to build the resource plugin and all the sdks:

```shell
make build_sdks
```

### Install Resource Plugin 

first, build and install resource plugin:

```shell
make install_resource_plugin
```

**Note**: Installing package directly from the package registry like pypi/npm/nuget is not supported yet, you need to install package from source via `make`.


### Node.js (Java/TypeScript)

```shell
make install_nodejs_sdk
```

### Python

```shell
make install_python_sdk
```

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/ryan4yin/pulumi-libvirt/sdk/go/...


### .NET

To use from .NET, use the following command:

    $ make install_dotnet_sdk

## Configuration

The following configuration points are available for the `libvirt` provider:

- `libvirt:uri` (environment: `LIBVIRT_DEFAULT_URI`) - The [connection URI](https://libvirt.org/uri.html) used to connect to the libvirt host.
  - e.g. `qemu:///system`

## Documentation

Please visit [dmacvicar/terraform-provider-libvirt](https://github.com/dmacvicar/terraform-provider-libvirt) for details

## Examples

set libvirt_url first:

```shell
export LIBVIRT_DEFAULT_URI=qemu:///system
```

Create VirtualMachine using Python SDK(writing in other languages ​​is almost the same):

```python
from pathlib import Path
import pulumi

from pulumi_libvirt import *


# notice: `#cloud-config` must be the first line without leading `\n`!
USER_DATA_TEMP = """#cloud-config
hostname: "{hostname}"
# let cloudinit ensure that a entry for the fqdn with a distribution dependent ip is present in /etc/hosts
manage_etc_hosts: localhost

package_upgrade: false

chpasswd:
  # expire password once uesed
  expire: false

# allow auth by password(not recommended for prod env)
ssh_pwauth: true

disable_root: false
# set root's password/keys
user: root
# set password for console login
password: "{root_passwd}"
ssh_authorized_keys:
- "{public_key}"

growpart:
  mode: auto
  devices: ['/']

# allow login using root
runcmd:
 - sed  -i '/PermitRootLogin/s/.*/PermitRootLogin yes/' /etc/ssh/sshd_config 
 - systemctl restart sshd
"""


NETWORK_CONFIG_TEMP = """
version: 1
config:
  - type: physical
    name: eth0
    subnets:
      - type: static
        address: {ip_addr}
        netmask: 255.255.255.0
        gateway: 192.168.122.1
  - type: nameserver
    interface: eth0
    address:
      - 114.114.114.114
      - 8.8.8.8
    # search:  # search domain
    #   - xxx
"""

LIBVRIT_DISK_POOL = Pool(
    "k8s-pool",
    name="k8s",
    type="dir",
    path="/data/k8s-pool"
)


def new_vm(
    hostname: str,
    ip_addr: str,
    public_key: str,
    root_passwd: str,
    template_qcow2_path: str,
    cpu: int = 2,
    memory: int = 4096,
    disk_size: int = 20 * 1024 * 1024 * 1024,
    ):

    os_image = Volume(
        f"{hostname}-image",
        name=f"{hostname}.qcow2",
        # uri to the volume file, http/file
        source=template_qcow2_path,
    )

    # clone from base volume, and resize it
    volume = Volume(
        f"{hostname}-disk",
        name=f"{hostname}-disk.qcow2",
        base_volume_id=os_image.id,
        pool=LIBVRIT_DISK_POOL.name,
        size=disk_size,
    )

    # generate cloudinit seed iso
    cloudinit_disk = CloudInitDisk(
        f"{hostname}-cloudinit-seed",
        name=f"{hostname}-seed.iso",
        user_data=USER_DATA_TEMP.format(
            hostname=hostname,
            root_passwd=root_passwd,
            public_key=public_key,
        ),
        network_config=NETWORK_CONFIG_TEMP.format(
            ip_addr=ip_addr,
        ),
        pool=LIBVRIT_DISK_POOL.name,
    )


    # create the new vm
    return Domain(
        f"{hostname}-vm",
        name=f"{hostname}-vm",

        autostart=True,
        qemu_agent=False,
        running=False,

        vcpu=cpu,
        memory=memory,
        description=f"{hostname}-vm",

        cloudinit=cloudinit_disk.id,
        disks=[
            DomainDiskArgs(volume_id=volume.id, scsi=True)
        ],

        # connect to the defaul network
        network_interfaces=[
            DomainNetworkInterfaceArgs(
                network_name="default",
            )
        ],


        # The optional filesystem block are used to share a directory of the libvirtd host with the guest.
        # filesystems=[
        #     # mount this dir inside guest os: `sudo mount -t 9p -o trans=virtio,version=9p2000.L,r share /data/share`
        #     DomainFilesystemArgs(source="/data/share", target="share", readonly=True)
        # ]

        # IMPORTANT: this is a known bug on cloud images, since they expect a console
        # we need to pass it
        # https://bugs.launchpad.net/cloud-images/+bug/1573095
        consoles=[
            DomainConsoleArgs(
                type="pty",
                target_type="virtio",
                target_port="1",
            )
        ],

        # graphics=DomainGraphicsArgs(type="vnc", listen_type="address"),
        graphics=DomainGraphicsArgs(
            type="spice", listen_type="address", autoport=True),
    )



def main():
    public_key = Path("ssh-common.pub").read_text()
    template_qcow2_path = "/data/base-os/openSUSE-Leap-15.2-OpenStack.x86_64.qcow2"
    # notice: ubuntu's default network interface is ens3 instead of eth0!
    # template_qcow2_path = "/data/base-os/ubuntu-21.04-server-cloudimg-amd64-disk-kvm.img"
    disk_size = 30 * 1024 * 1024 * 1024  # 30G
    root_passwd = "xxx123"

    k8s_master = new_vm(
        hostname="k8s-master-0",
        ip_addr = "192.168.122.160",
        public_key=public_key,
        root_passwd=root_passwd,
        template_qcow2_path=template_qcow2_path,
        cpu= 2,
        memory = 4096,
        disk_size =disk_size,
    )
    k8s_node_1 = new_vm(
        hostname="k8s-worker-0",
        ip_addr = "192.168.122.170",
        public_key=public_key,
        root_passwd=root_passwd,
        template_qcow2_path=template_qcow2_path,
        cpu= 4,
        memory = 8192,
        disk_size =disk_size,
    )
    k8s_node_2 = new_vm(
        hostname="k8s-worker-1",
        ip_addr = "192.168.122.171",
        public_key=public_key,
        root_passwd=root_passwd,
        template_qcow2_path=template_qcow2_path,
        cpu= 4,
        memory = 8192,
        disk_size =disk_size,
    )



main()
```


## Some Known Problems related to Cloud Images

- [Ubuntu Cloud Images (RELEASED)](https://cloud-images.ubuntu.com/releases/)
  - bug: `no such device: root` when boot, but the system can still boot correctly...
    - it's a bug of ubuntu: https://bugs.launchpad.net/cloud-images/+bug/1726476
  - ubuntu's default network interface is `ens3` instead of `eth0`!
- [OpenSUSE Cloud Images](https://download.opensuse.org/repositories/Cloud:/Images:/)
  - bug: only support `network_config` version 1! if you use version 2, some configs such as `gateway4` will be ignored!
- [Debian Cloud Images](https://cdimage.debian.org/cdimage/cloud/)
  - bug: stuck on boot, or report kernel panic
    - DO NOT use spice as graphic card, repleace it with `vnc` and then everything will be ok.
  - `debian-nocloud` do not run cloudinit on startup
    - still don't know why...

