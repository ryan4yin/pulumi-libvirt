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
    public sealed class DomainDisk
    {
        public readonly string? BlockDevice;
        public readonly string? File;
        public readonly bool? Scsi;
        public readonly string? Url;
        public readonly string? VolumeId;
        public readonly string? Wwn;

        [OutputConstructor]
        private DomainDisk(
            string? blockDevice,

            string? file,

            bool? scsi,

            string? url,

            string? volumeId,

            string? wwn)
        {
            BlockDevice = blockDevice;
            File = file;
            Scsi = scsi;
            Url = url;
            VolumeId = volumeId;
            Wwn = wwn;
        }
    }
}
