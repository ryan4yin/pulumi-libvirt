// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class NetworkDnsGetArgs : Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("forwarders")]
        private InputList<Inputs.NetworkDnsForwarderGetArgs>? _forwarders;
        public InputList<Inputs.NetworkDnsForwarderGetArgs> Forwarders
        {
            get => _forwarders ?? (_forwarders = new InputList<Inputs.NetworkDnsForwarderGetArgs>());
            set => _forwarders = value;
        }

        [Input("hosts")]
        private InputList<Inputs.NetworkDnsHostGetArgs>? _hosts;
        public InputList<Inputs.NetworkDnsHostGetArgs> Hosts
        {
            get => _hosts ?? (_hosts = new InputList<Inputs.NetworkDnsHostGetArgs>());
            set => _hosts = value;
        }

        [Input("localOnly")]
        public Input<bool>? LocalOnly { get; set; }

        [Input("srvs")]
        private InputList<Inputs.NetworkDnsSrvGetArgs>? _srvs;
        public InputList<Inputs.NetworkDnsSrvGetArgs> Srvs
        {
            get => _srvs ?? (_srvs = new InputList<Inputs.NetworkDnsSrvGetArgs>());
            set => _srvs = value;
        }

        public NetworkDnsGetArgs()
        {
        }
    }
}