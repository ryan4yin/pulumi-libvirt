// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Outputs
{

    [OutputType]
    public sealed class NetworkDns
    {
        public readonly bool? Enabled;
        public readonly ImmutableArray<Outputs.NetworkDnsForwarder> Forwarders;
        public readonly ImmutableArray<Outputs.NetworkDnsHost> Hosts;
        public readonly bool? LocalOnly;
        public readonly ImmutableArray<Outputs.NetworkDnsSrv> Srvs;

        [OutputConstructor]
        private NetworkDns(
            bool? enabled,

            ImmutableArray<Outputs.NetworkDnsForwarder> forwarders,

            ImmutableArray<Outputs.NetworkDnsHost> hosts,

            bool? localOnly,

            ImmutableArray<Outputs.NetworkDnsSrv> srvs)
        {
            Enabled = enabled;
            Forwarders = forwarders;
            Hosts = hosts;
            LocalOnly = localOnly;
            Srvs = srvs;
        }
    }
}