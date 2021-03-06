# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs

__all__ = [
    'DomainBootDevice',
    'DomainConsole',
    'DomainCpu',
    'DomainDisk',
    'DomainFilesystem',
    'DomainGraphics',
    'DomainNetworkInterface',
    'DomainNvram',
    'DomainVideo',
    'DomainXml',
    'NetworkDhcp',
    'NetworkDns',
    'NetworkDnsForwarder',
    'NetworkDnsHost',
    'NetworkDnsSrv',
    'NetworkRoute',
    'NetworkXml',
    'PoolXml',
    'VolumeXml',
]

@pulumi.output_type
class DomainBootDevice(dict):
    def __init__(__self__, *,
                 devs: Optional[Sequence[str]] = None):
        if devs is not None:
            pulumi.set(__self__, "devs", devs)

    @property
    @pulumi.getter
    def devs(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "devs")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainConsole(dict):
    def __init__(__self__, *,
                 target_port: str,
                 type: str,
                 source_host: Optional[str] = None,
                 source_path: Optional[str] = None,
                 source_service: Optional[str] = None,
                 target_type: Optional[str] = None):
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
    def target_port(self) -> str:
        return pulumi.get(self, "target_port")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="sourceHost")
    def source_host(self) -> Optional[str]:
        return pulumi.get(self, "source_host")

    @property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> Optional[str]:
        return pulumi.get(self, "source_path")

    @property
    @pulumi.getter(name="sourceService")
    def source_service(self) -> Optional[str]:
        return pulumi.get(self, "source_service")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[str]:
        return pulumi.get(self, "target_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainCpu(dict):
    def __init__(__self__, *,
                 mode: str):
        pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter
    def mode(self) -> str:
        return pulumi.get(self, "mode")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainDisk(dict):
    def __init__(__self__, *,
                 block_device: Optional[str] = None,
                 file: Optional[str] = None,
                 scsi: Optional[bool] = None,
                 url: Optional[str] = None,
                 volume_id: Optional[str] = None,
                 wwn: Optional[str] = None):
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
    def block_device(self) -> Optional[str]:
        return pulumi.get(self, "block_device")

    @property
    @pulumi.getter
    def file(self) -> Optional[str]:
        return pulumi.get(self, "file")

    @property
    @pulumi.getter
    def scsi(self) -> Optional[bool]:
        return pulumi.get(self, "scsi")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[str]:
        return pulumi.get(self, "volume_id")

    @property
    @pulumi.getter
    def wwn(self) -> Optional[str]:
        return pulumi.get(self, "wwn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainFilesystem(dict):
    def __init__(__self__, *,
                 source: str,
                 target: str,
                 accessmode: Optional[str] = None,
                 readonly: Optional[bool] = None):
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "target", target)
        if accessmode is not None:
            pulumi.set(__self__, "accessmode", accessmode)
        if readonly is not None:
            pulumi.set(__self__, "readonly", readonly)

    @property
    @pulumi.getter
    def source(self) -> str:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def target(self) -> str:
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def accessmode(self) -> Optional[str]:
        return pulumi.get(self, "accessmode")

    @property
    @pulumi.getter
    def readonly(self) -> Optional[bool]:
        return pulumi.get(self, "readonly")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainGraphics(dict):
    def __init__(__self__, *,
                 autoport: Optional[bool] = None,
                 listen_address: Optional[str] = None,
                 listen_type: Optional[str] = None,
                 type: Optional[str] = None):
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
    def autoport(self) -> Optional[bool]:
        return pulumi.get(self, "autoport")

    @property
    @pulumi.getter(name="listenAddress")
    def listen_address(self) -> Optional[str]:
        return pulumi.get(self, "listen_address")

    @property
    @pulumi.getter(name="listenType")
    def listen_type(self) -> Optional[str]:
        return pulumi.get(self, "listen_type")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainNetworkInterface(dict):
    def __init__(__self__, *,
                 addresses: Optional[Sequence[str]] = None,
                 bridge: Optional[str] = None,
                 hostname: Optional[str] = None,
                 mac: Optional[str] = None,
                 macvtap: Optional[str] = None,
                 network_id: Optional[str] = None,
                 network_name: Optional[str] = None,
                 passthrough: Optional[str] = None,
                 vepa: Optional[str] = None,
                 wait_for_lease: Optional[bool] = None):
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
    def addresses(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter
    def bridge(self) -> Optional[str]:
        return pulumi.get(self, "bridge")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def mac(self) -> Optional[str]:
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def macvtap(self) -> Optional[str]:
        return pulumi.get(self, "macvtap")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[str]:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> Optional[str]:
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter
    def passthrough(self) -> Optional[str]:
        return pulumi.get(self, "passthrough")

    @property
    @pulumi.getter
    def vepa(self) -> Optional[str]:
        return pulumi.get(self, "vepa")

    @property
    @pulumi.getter(name="waitForLease")
    def wait_for_lease(self) -> Optional[bool]:
        return pulumi.get(self, "wait_for_lease")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainNvram(dict):
    def __init__(__self__, *,
                 file: str,
                 template: Optional[str] = None):
        pulumi.set(__self__, "file", file)
        if template is not None:
            pulumi.set(__self__, "template", template)

    @property
    @pulumi.getter
    def file(self) -> str:
        return pulumi.get(self, "file")

    @property
    @pulumi.getter
    def template(self) -> Optional[str]:
        return pulumi.get(self, "template")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainVideo(dict):
    def __init__(__self__, *,
                 type: Optional[str] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DomainXml(dict):
    def __init__(__self__, *,
                 xslt: Optional[str] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[str]:
        return pulumi.get(self, "xslt")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkDhcp(dict):
    def __init__(__self__, *,
                 enabled: Optional[bool] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkDns(dict):
    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 forwarders: Optional[Sequence['outputs.NetworkDnsForwarder']] = None,
                 hosts: Optional[Sequence['outputs.NetworkDnsHost']] = None,
                 local_only: Optional[bool] = None,
                 srvs: Optional[Sequence['outputs.NetworkDnsSrv']] = None):
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
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def forwarders(self) -> Optional[Sequence['outputs.NetworkDnsForwarder']]:
        return pulumi.get(self, "forwarders")

    @property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence['outputs.NetworkDnsHost']]:
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter(name="localOnly")
    def local_only(self) -> Optional[bool]:
        return pulumi.get(self, "local_only")

    @property
    @pulumi.getter
    def srvs(self) -> Optional[Sequence['outputs.NetworkDnsSrv']]:
        return pulumi.get(self, "srvs")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkDnsForwarder(dict):
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 domain: Optional[str] = None):
        if address is not None:
            pulumi.set(__self__, "address", address)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkDnsHost(dict):
    def __init__(__self__, *,
                 hostname: Optional[str] = None,
                 ip: Optional[str] = None):
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def ip(self) -> Optional[str]:
        return pulumi.get(self, "ip")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkDnsSrv(dict):
    def __init__(__self__, *,
                 domain: Optional[str] = None,
                 port: Optional[str] = None,
                 priority: Optional[str] = None,
                 protocol: Optional[str] = None,
                 service: Optional[str] = None,
                 target: Optional[str] = None,
                 weight: Optional[str] = None):
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
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def priority(self) -> Optional[str]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def service(self) -> Optional[str]:
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def target(self) -> Optional[str]:
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def weight(self) -> Optional[str]:
        return pulumi.get(self, "weight")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkRoute(dict):
    def __init__(__self__, *,
                 cidr: str,
                 gateway: str):
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "gateway", gateway)

    @property
    @pulumi.getter
    def cidr(self) -> str:
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def gateway(self) -> str:
        return pulumi.get(self, "gateway")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NetworkXml(dict):
    def __init__(__self__, *,
                 xslt: Optional[str] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[str]:
        return pulumi.get(self, "xslt")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PoolXml(dict):
    def __init__(__self__, *,
                 xslt: Optional[str] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[str]:
        return pulumi.get(self, "xslt")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeXml(dict):
    def __init__(__self__, *,
                 xslt: Optional[str] = None):
        if xslt is not None:
            pulumi.set(__self__, "xslt", xslt)

    @property
    @pulumi.getter
    def xslt(self) -> Optional[str]:
        return pulumi.get(self, "xslt")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


