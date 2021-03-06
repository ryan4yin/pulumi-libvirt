# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'DomainBootDeviceArgs',
    'DomainConsoleArgs',
    'DomainCpuArgs',
    'DomainDiskArgs',
    'DomainFilesystemArgs',
    'DomainGraphicsArgs',
    'DomainNetworkInterfaceArgs',
    'DomainNvramArgs',
    'DomainVideoArgs',
    'DomainXmlArgs',
    'NetworkDhcpArgs',
    'NetworkDnsArgs',
    'NetworkDnsForwarderArgs',
    'NetworkDnsHostArgs',
    'NetworkDnsSrvArgs',
    'NetworkRouteArgs',
    'NetworkXmlArgs',
    'PoolXmlArgs',
    'VolumeXmlArgs',
]

@pulumi.input_type
class DomainBootDeviceArgs:
    def __init__(__self__, *,
                 devs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        if devs is not None:
            pulumi.set(__self__, "devs", devs)

    @property
    @pulumi.getter
    def devs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "devs")

    @devs.setter
    def devs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "devs", value)


@pulumi.input_type
class DomainConsoleArgs:
    def __init__(__self__, *,
                 target_port: pulumi.Input[str],
                 type: pulumi.Input[str],
                 source_host: Optional[pulumi.Input[str]] = None,
                 source_path: Optional[pulumi.Input[str]] = None,
                 source_service: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "target_port", target_port)
        pulumi.set(__self__, "type", type)
        if source_host is not None:
            pulumi.set(__self__, "source_host", source_host)
        if source_path is not None:
            pulumi.set(__self__, "source_path", source_path)
        if source_service is not None:
            pulumi.set(__self__, "source_service", source_service)
        if target_type is not None:
            pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_port")

    @target_port.setter
    def target_port(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_port", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="sourceHost")
    def source_host(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_host")

    @source_host.setter
    def source_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_host", value)

    @property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_path")

    @source_path.setter
    def source_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_path", value)

    @property
    @pulumi.getter(name="sourceService")
    def source_service(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_service")

    @source_service.setter
    def source_service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_service", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_type", value)


@pulumi.input_type
class DomainCpuArgs:
    def __init__(__self__, *,
                 mode: pulumi.Input[str]):
        pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "mode", value)


@pulumi.input_type
class DomainDiskArgs:
    def __init__(__self__, *,
                 block_device: Optional[pulumi.Input[str]] = None,
                 file: Optional[pulumi.Input[str]] = None,
                 scsi: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 wwn: Optional[pulumi.Input[str]] = None):
        if block_device is not None:
            pulumi.set(__self__, "block_device", block_device)
        if file is not None:
            pulumi.set(__self__, "file", file)
        if scsi is not None:
            pulumi.set(__self__, "scsi", scsi)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if volume_id is not None:
            pulumi.set(__self__, "volume_id", volume_id)
        if wwn is not None:
            pulumi.set(__self__, "wwn", wwn)

    @property
    @pulumi.getter(name="blockDevice")
    def block_device(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "block_device")

    @block_device.setter
    def block_device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "block_device", value)

    @property
    @pulumi.getter
    def file(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file")

    @file.setter
    def file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file", value)

    @property
    @pulumi.getter
    def scsi(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "scsi")

    @scsi.setter
    def scsi(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "scsi", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_id", value)

    @property
    @pulumi.getter
    def wwn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "wwn")

    @wwn.setter
    def wwn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "wwn", value)


@pulumi.input_type
class DomainFilesystemArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[str],
                 target: pulumi.Input[str],
                 accessmode: Optional[pulumi.Input[str]] = None,
                 readonly: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "target", target)
        if accessmode is not None:
            pulumi.set(__self__, "accessmode", accessmode)
        if readonly is not None:
            pulumi.set(__self__, "readonly", readonly)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def accessmode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "accessmode")

    @accessmode.setter
    def accessmode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accessmode", value)

    @property
    @pulumi.getter
    def readonly(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "readonly")

    @readonly.setter
    def readonly(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "readonly", value)


@pulumi.input_type
class DomainGraphicsArgs:
    def __init__(__self__, *,
                 autoport: Optional[pulumi.Input[bool]] = None,
                 listen_address: Optional[pulumi.Input[str]] = None,
                 listen_type: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if autoport is not None:
            pulumi.set(__self__, "autoport", autoport)
        if listen_address is not None:
            pulumi.set(__self__, "listen_address", listen_address)
        if listen_type is not None:
            pulumi.set(__self__, "listen_type", listen_type)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def autoport(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "autoport")

    @autoport.setter
    def autoport(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "autoport", value)

    @property
    @pulumi.getter(name="listenAddress")
    def listen_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "listen_address")

    @listen_address.setter
    def listen_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listen_address", value)

    @property
    @pulumi.getter(name="listenType")
    def listen_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "listen_type")

    @listen_type.setter
    def listen_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listen_type", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class DomainNetworkInterfaceArgs:
    def __init__(__self__, *,
                 addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 bridge: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 macvtap: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 passthrough: Optional[pulumi.Input[str]] = None,
                 vepa: Optional[pulumi.Input[str]] = None,
                 wait_for_lease: Optional[pulumi.Input[bool]] = None):
        if addresses is not None:
            pulumi.set(__self__, "addresses", addresses)
        if bridge is not None:
            pulumi.set(__self__, "bridge", bridge)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if macvtap is not None:
            pulumi.set(__self__, "macvtap", macvtap)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if network_name is not None:
            pulumi.set(__self__, "network_name", network_name)
        if passthrough is not None:
            pulumi.set(__self__, "passthrough", passthrough)
        if vepa is not None:
            pulumi.set(__self__, "vepa", vepa)
        if wait_for_lease is not None:
            pulumi.set(__self__, "wait_for_lease", wait_for_lease)

    @property
    @pulumi.getter
    def addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "addresses")

    @addresses.setter
    def addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "addresses", value)

    @property
    @pulumi.getter
    def bridge(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bridge")

    @bridge.setter
    def bridge(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bridge", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def macvtap(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "macvtap")

    @macvtap.setter
    def macvtap(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macvtap", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter
    def passthrough(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "passthrough")

    @passthrough.setter
    def passthrough(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "passthrough", value)

    @property
    @pulumi.getter
    def vepa(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vepa")

    @vepa.setter
    def vepa(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vepa", value)

    @property
    @pulumi.getter(name="waitForLease")
    def wait_for_lease(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "wait_for_lease")

    @wait_for_lease.setter
    def wait_for_lease(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wait_for_lease", value)


@pulumi.input_type
class DomainNvramArgs:
    def __init__(__self__, *,
                 file: pulumi.Input[str],
                 template: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "file", file)
        if template is not None:
            pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter
    def file(self) -> pulumi.Input[str]:
        return pulumi.get(self, "file")

    @file.setter
    def file(self, value: pulumi.Input[str]):
        pulumi.set(self, "file", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template", value)


@pulumi.input_type
class DomainVideoArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[str]] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class DomainXmlArgs:
    def __init__(__self__, *,
                 xslt: Optional[pulumi.Input[str]] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "xslt")

    @xslt.setter
    def xslt(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "xslt", value)


@pulumi.input_type
class NetworkDhcpArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class NetworkDnsArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 forwarders: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsForwarderArgs']]]] = None,
                 hosts: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsHostArgs']]]] = None,
                 local_only: Optional[pulumi.Input[bool]] = None,
                 srvs: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsSrvArgs']]]] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if forwarders is not None:
            pulumi.set(__self__, "forwarders", forwarders)
        if hosts is not None:
            pulumi.set(__self__, "hosts", hosts)
        if local_only is not None:
            pulumi.set(__self__, "local_only", local_only)
        if srvs is not None:
            pulumi.set(__self__, "srvs", srvs)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def forwarders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsForwarderArgs']]]]:
        return pulumi.get(self, "forwarders")

    @forwarders.setter
    def forwarders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsForwarderArgs']]]]):
        pulumi.set(self, "forwarders", value)

    @property
    @pulumi.getter
    def hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsHostArgs']]]]:
        return pulumi.get(self, "hosts")

    @hosts.setter
    def hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsHostArgs']]]]):
        pulumi.set(self, "hosts", value)

    @property
    @pulumi.getter(name="localOnly")
    def local_only(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "local_only")

    @local_only.setter
    def local_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "local_only", value)

    @property
    @pulumi.getter
    def srvs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsSrvArgs']]]]:
        return pulumi.get(self, "srvs")

    @srvs.setter
    def srvs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkDnsSrvArgs']]]]):
        pulumi.set(self, "srvs", value)


@pulumi.input_type
class NetworkDnsForwarderArgs:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None):
        if address is not None:
            pulumi.set(__self__, "address", address)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)


@pulumi.input_type
class NetworkDnsHostArgs:
    def __init__(__self__, *,
                 hostname: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None):
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)


@pulumi.input_type
class NetworkDnsSrvArgs:
    def __init__(__self__, *,
                 domain: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[str]] = None):
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if service is not None:
            pulumi.set(__self__, "service", service)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class NetworkRouteArgs:
    def __init__(__self__, *,
                 cidr: pulumi.Input[str],
                 gateway: pulumi.Input[str]):
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "gateway", gateway)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Input[str]:
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway", value)


@pulumi.input_type
class NetworkXmlArgs:
    def __init__(__self__, *,
                 xslt: Optional[pulumi.Input[str]] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "xslt")

    @xslt.setter
    def xslt(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "xslt", value)


@pulumi.input_type
class PoolXmlArgs:
    def __init__(__self__, *,
                 xslt: Optional[pulumi.Input[str]] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "xslt")

    @xslt.setter
    def xslt(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "xslt", value)


@pulumi.input_type
class VolumeXmlArgs:
    def __init__(__self__, *,
                 xslt: Optional[pulumi.Input[str]] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "xslt")

    @xslt.setter
    def xslt(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "xslt", value)


