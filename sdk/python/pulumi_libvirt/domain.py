# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Domain']


class Domain(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arch: Optional[pulumi.Input[str]] = None,
                 autostart: Optional[pulumi.Input[bool]] = None,
                 boot_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainBootDeviceArgs']]]]] = None,
                 cloudinit: Optional[pulumi.Input[str]] = None,
                 cmdlines: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 consoles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainConsoleArgs']]]]] = None,
                 coreos_ignition: Optional[pulumi.Input[str]] = None,
                 cpu: Optional[pulumi.Input[pulumi.InputType['DomainCpuArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainDiskArgs']]]]] = None,
                 emulator: Optional[pulumi.Input[str]] = None,
                 filesystems: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainFilesystemArgs']]]]] = None,
                 firmware: Optional[pulumi.Input[str]] = None,
                 fw_cfg_name: Optional[pulumi.Input[str]] = None,
                 graphics: Optional[pulumi.Input[pulumi.InputType['DomainGraphicsArgs']]] = None,
                 initrd: Optional[pulumi.Input[str]] = None,
                 kernel: Optional[pulumi.Input[str]] = None,
                 machine: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[int]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainNetworkInterfaceArgs']]]]] = None,
                 nvram: Optional[pulumi.Input[pulumi.InputType['DomainNvramArgs']]] = None,
                 qemu_agent: Optional[pulumi.Input[bool]] = None,
                 running: Optional[pulumi.Input[bool]] = None,
                 vcpu: Optional[pulumi.Input[int]] = None,
                 video: Optional[pulumi.Input[pulumi.InputType['DomainVideoArgs']]] = None,
                 xml: Optional[pulumi.Input[pulumi.InputType['DomainXmlArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['arch'] = arch
            __props__['autostart'] = autostart
            __props__['boot_devices'] = boot_devices
            __props__['cloudinit'] = cloudinit
            __props__['cmdlines'] = cmdlines
            __props__['consoles'] = consoles
            __props__['coreos_ignition'] = coreos_ignition
            __props__['cpu'] = cpu
            __props__['description'] = description
            __props__['disks'] = disks
            __props__['emulator'] = emulator
            __props__['filesystems'] = filesystems
            __props__['firmware'] = firmware
            __props__['fw_cfg_name'] = fw_cfg_name
            __props__['graphics'] = graphics
            __props__['initrd'] = initrd
            __props__['kernel'] = kernel
            __props__['machine'] = machine
            __props__['memory'] = memory
            __props__['metadata'] = metadata
            __props__['name'] = name
            __props__['network_interfaces'] = network_interfaces
            __props__['nvram'] = nvram
            __props__['qemu_agent'] = qemu_agent
            __props__['running'] = running
            __props__['vcpu'] = vcpu
            __props__['video'] = video
            __props__['xml'] = xml
        super(Domain, __self__).__init__(
            'libvirt:index/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arch: Optional[pulumi.Input[str]] = None,
            autostart: Optional[pulumi.Input[bool]] = None,
            boot_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainBootDeviceArgs']]]]] = None,
            cloudinit: Optional[pulumi.Input[str]] = None,
            cmdlines: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
            consoles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainConsoleArgs']]]]] = None,
            coreos_ignition: Optional[pulumi.Input[str]] = None,
            cpu: Optional[pulumi.Input[pulumi.InputType['DomainCpuArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainDiskArgs']]]]] = None,
            emulator: Optional[pulumi.Input[str]] = None,
            filesystems: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainFilesystemArgs']]]]] = None,
            firmware: Optional[pulumi.Input[str]] = None,
            fw_cfg_name: Optional[pulumi.Input[str]] = None,
            graphics: Optional[pulumi.Input[pulumi.InputType['DomainGraphicsArgs']]] = None,
            initrd: Optional[pulumi.Input[str]] = None,
            kernel: Optional[pulumi.Input[str]] = None,
            machine: Optional[pulumi.Input[str]] = None,
            memory: Optional[pulumi.Input[int]] = None,
            metadata: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainNetworkInterfaceArgs']]]]] = None,
            nvram: Optional[pulumi.Input[pulumi.InputType['DomainNvramArgs']]] = None,
            qemu_agent: Optional[pulumi.Input[bool]] = None,
            running: Optional[pulumi.Input[bool]] = None,
            vcpu: Optional[pulumi.Input[int]] = None,
            video: Optional[pulumi.Input[pulumi.InputType['DomainVideoArgs']]] = None,
            xml: Optional[pulumi.Input[pulumi.InputType['DomainXmlArgs']]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arch"] = arch
        __props__["autostart"] = autostart
        __props__["boot_devices"] = boot_devices
        __props__["cloudinit"] = cloudinit
        __props__["cmdlines"] = cmdlines
        __props__["consoles"] = consoles
        __props__["coreos_ignition"] = coreos_ignition
        __props__["cpu"] = cpu
        __props__["description"] = description
        __props__["disks"] = disks
        __props__["emulator"] = emulator
        __props__["filesystems"] = filesystems
        __props__["firmware"] = firmware
        __props__["fw_cfg_name"] = fw_cfg_name
        __props__["graphics"] = graphics
        __props__["initrd"] = initrd
        __props__["kernel"] = kernel
        __props__["machine"] = machine
        __props__["memory"] = memory
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["network_interfaces"] = network_interfaces
        __props__["nvram"] = nvram
        __props__["qemu_agent"] = qemu_agent
        __props__["running"] = running
        __props__["vcpu"] = vcpu
        __props__["video"] = video
        __props__["xml"] = xml
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arch(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arch")

    @property
    @pulumi.getter
    def autostart(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "autostart")

    @property
    @pulumi.getter(name="bootDevices")
    def boot_devices(self) -> pulumi.Output[Optional[Sequence['outputs.DomainBootDevice']]]:
        return pulumi.get(self, "boot_devices")

    @property
    @pulumi.getter
    def cloudinit(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cloudinit")

    @property
    @pulumi.getter
    def cmdlines(self) -> pulumi.Output[Optional[Sequence[Mapping[str, Any]]]]:
        return pulumi.get(self, "cmdlines")

    @property
    @pulumi.getter
    def consoles(self) -> pulumi.Output[Optional[Sequence['outputs.DomainConsole']]]:
        return pulumi.get(self, "consoles")

    @property
    @pulumi.getter(name="coreosIgnition")
    def coreos_ignition(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "coreos_ignition")

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Output[Optional['outputs.DomainCpu']]:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Optional[Sequence['outputs.DomainDisk']]]:
        return pulumi.get(self, "disks")

    @property
    @pulumi.getter
    def emulator(self) -> pulumi.Output[str]:
        return pulumi.get(self, "emulator")

    @property
    @pulumi.getter
    def filesystems(self) -> pulumi.Output[Optional[Sequence['outputs.DomainFilesystem']]]:
        return pulumi.get(self, "filesystems")

    @property
    @pulumi.getter
    def firmware(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "firmware")

    @property
    @pulumi.getter(name="fwCfgName")
    def fw_cfg_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "fw_cfg_name")

    @property
    @pulumi.getter
    def graphics(self) -> pulumi.Output[Optional['outputs.DomainGraphics']]:
        return pulumi.get(self, "graphics")

    @property
    @pulumi.getter
    def initrd(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "initrd")

    @property
    @pulumi.getter
    def kernel(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kernel")

    @property
    @pulumi.getter
    def machine(self) -> pulumi.Output[str]:
        return pulumi.get(self, "machine")

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional[Sequence['outputs.DomainNetworkInterface']]]:
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter
    def nvram(self) -> pulumi.Output[Optional['outputs.DomainNvram']]:
        return pulumi.get(self, "nvram")

    @property
    @pulumi.getter(name="qemuAgent")
    def qemu_agent(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "qemu_agent")

    @property
    @pulumi.getter
    def running(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "running")

    @property
    @pulumi.getter
    def vcpu(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "vcpu")

    @property
    @pulumi.getter
    def video(self) -> pulumi.Output[Optional['outputs.DomainVideo']]:
        return pulumi.get(self, "video")

    @property
    @pulumi.getter
    def xml(self) -> pulumi.Output[Optional['outputs.DomainXml']]:
        return pulumi.get(self, "xml")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
