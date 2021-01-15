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

__all__ = ['Network']


class Network(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 autostart: Optional[pulumi.Input[bool]] = None,
                 bridge: Optional[pulumi.Input[str]] = None,
                 dhcp: Optional[pulumi.Input[pulumi.InputType['NetworkDhcpArgs']]] = None,
                 dns: Optional[pulumi.Input[pulumi.InputType['NetworkDnsArgs']]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkRouteArgs']]]]] = None,
                 xml: Optional[pulumi.Input[pulumi.InputType['NetworkXmlArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Network resource with the given unique name, props, and options.
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

            __props__['addresses'] = addresses
            __props__['autostart'] = autostart
            __props__['bridge'] = bridge
            __props__['dhcp'] = dhcp
            __props__['dns'] = dns
            __props__['domain'] = domain
            __props__['mode'] = mode
            __props__['mtu'] = mtu
            __props__['name'] = name
            __props__['routes'] = routes
            __props__['xml'] = xml
        super(Network, __self__).__init__(
            'libvirt:index/network:Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            autostart: Optional[pulumi.Input[bool]] = None,
            bridge: Optional[pulumi.Input[str]] = None,
            dhcp: Optional[pulumi.Input[pulumi.InputType['NetworkDhcpArgs']]] = None,
            dns: Optional[pulumi.Input[pulumi.InputType['NetworkDnsArgs']]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkRouteArgs']]]]] = None,
            xml: Optional[pulumi.Input[pulumi.InputType['NetworkXmlArgs']]] = None) -> 'Network':
        """
        Get an existing Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["addresses"] = addresses
        __props__["autostart"] = autostart
        __props__["bridge"] = bridge
        __props__["dhcp"] = dhcp
        __props__["dns"] = dns
        __props__["domain"] = domain
        __props__["mode"] = mode
        __props__["mtu"] = mtu
        __props__["name"] = name
        __props__["routes"] = routes
        __props__["xml"] = xml
        return Network(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def addresses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter
    def autostart(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "autostart")

    @property
    @pulumi.getter
    def bridge(self) -> pulumi.Output[str]:
        return pulumi.get(self, "bridge")

    @property
    @pulumi.getter
    def dhcp(self) -> pulumi.Output[Optional['outputs.NetworkDhcp']]:
        return pulumi.get(self, "dhcp")

    @property
    @pulumi.getter
    def dns(self) -> pulumi.Output[Optional['outputs.NetworkDns']]:
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkRoute']]]:
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def xml(self) -> pulumi.Output[Optional['outputs.NetworkXml']]:
        return pulumi.get(self, "xml")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

