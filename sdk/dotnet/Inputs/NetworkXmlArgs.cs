// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class NetworkXmlArgs : Pulumi.ResourceArgs
    {
        [Input("xslt")]
        public Input<string>? Xslt { get; set; }

        public NetworkXmlArgs()
        {
        }
    }
}
