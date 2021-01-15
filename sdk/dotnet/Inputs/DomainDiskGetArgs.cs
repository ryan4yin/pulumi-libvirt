// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt.Inputs
{

    public sealed class DomainDiskGetArgs : Pulumi.ResourceArgs
    {
        [Input("blockDevice")]
        public Input<string>? BlockDevice { get; set; }

        [Input("file")]
        public Input<string>? File { get; set; }

        [Input("scsi")]
        public Input<bool>? Scsi { get; set; }

        [Input("url")]
        public Input<string>? Url { get; set; }

        [Input("volumeId")]
        public Input<string>? VolumeId { get; set; }

        [Input("wwn")]
        public Input<string>? Wwn { get; set; }

        public DomainDiskGetArgs()
        {
        }
    }
}
