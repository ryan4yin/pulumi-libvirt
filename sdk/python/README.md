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

>to be done.

