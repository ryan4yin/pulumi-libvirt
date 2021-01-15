Pulumi Provider for Libvirt
======

![master branch status](https://github.com/ryan4yin/pulumi-libvirt/workflows/master/badge.svg)
[![PYPI Version](https://img.shields.io/pypi/v/pulumi_libvirt.svg)](https://pypi.org/project/pulumi_libvirt/)

A Pulumi provider that lets you provision servers on a libvirt host via pulumi.


Based on [dmacvicar/terraform-provider-libvirt](https://github.com/dmacvicar/terraform-provider-libvirt)

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

from pulumi_libvirt import *

private_key = Path("ssh-common").read_text()

os_image = Volume(
    "opensuse-image",
    name="opensuse-base-qcow2.qcow2",
    # uri to the volume file, http/file
    source="/data/os-images/opensuse15.2-OpenStack.x86_64.qcow2",
)

disk_pool = Pool(
    "libvirt-test-pool",
    name="libvirt-test",
    type="dir",
    path="/data/kvm-pool"
)

volume = Volume(
    "opensuse-vm-test-disk",
    name="opensuse-vm-test-disk.qcow2",
    base_volume_id=os_image.id,
    pool=disk_pool.name,
    size=30 * 1024 * 1024 * 1024,  # clone from base volume, and resize to 10GB(in bytes)
)

cloudinit_disk = CloudInitDisk(
    "cloudinit-test",
    name="cloudinit-test.iso",
    user_data=f"""#cloud-config
hostname: k8s-master-0
# let cloudinit ensure that a entry for the fqdn with a distribution dependent ip is present in /etc/hosts
manage_etc_hosts: localhost

package_upgrade: true

disable_root: false

# set root's password/keys
user: root
# set password for console login
password: xxxxx
ssh_authorized_keys:
  - "{private_key}"

chpasswd:
  # expire password once uesed
  expire: false
  
# allow auth by password(not recommended)
# ssh_pwauth: true
    """,
    network_config="""
version: 2
ethernets:
  eth0:
    dhcp4: false
    addresses: 
    - 192.168.122.160/24
    gateway4: 192.168.122.1
    nameservers:
      addresses: [ 114.114.114.114,8.8.8.8 ]
    """,
    pool=disk_pool.name,
)


vm = Domain(
    "opensuse-vm-test",
    name="opensuse-vm-test",

    autostart=True,
    qemu_agent=False,
    running=False,

    vcpu=2,
    memory=4096,
    description="opensuse vm",

    cloudinit=cloudinit_disk.id,
    disks=[
        DomainDiskArgs(volume_id=volume.id, scsi=True)
    ],

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
```

