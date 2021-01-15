// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class DomainNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        [Input("addresses")]
        private InputList<string>? _addresses;
        public InputList<string> Addresses
        {
            get => _addresses ?? (_addresses = new InputList<string>());
            set => _addresses = value;
        }

        [Input("bridge")]
        public Input<string>? Bridge { get; set; }

        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("mac")]
        public Input<string>? Mac { get; set; }

        [Input("macvtap")]
        public Input<string>? Macvtap { get; set; }

        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        [Input("networkName")]
        public Input<string>? NetworkName { get; set; }

        [Input("passthrough")]
        public Input<string>? Passthrough { get; set; }

        [Input("vepa")]
        public Input<string>? Vepa { get; set; }

        [Input("waitForLease")]
        public Input<bool>? WaitForLease { get; set; }

        public DomainNetworkInterfaceArgs()
        {
        }
    }
}
