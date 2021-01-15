// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Libvirt
{
    public partial class Domain : Pulumi.CustomResource
    {
        [Output("arch")]
        public Output<string> Arch { get; private set; } = null!;

        [Output("autostart")]
        public Output<bool?> Autostart { get; private set; } = null!;

        [Output("bootDevices")]
        public Output<ImmutableArray<Outputs.DomainBootDevice>> BootDevices { get; private set; } = null!;

        [Output("cloudinit")]
        public Output<string?> Cloudinit { get; private set; } = null!;

        [Output("cmdlines")]
        public Output<ImmutableArray<ImmutableDictionary<string, object>>> Cmdlines { get; private set; } = null!;

        [Output("consoles")]
        public Output<ImmutableArray<Outputs.DomainConsole>> Consoles { get; private set; } = null!;

        [Output("coreosIgnition")]
        public Output<string?> CoreosIgnition { get; private set; } = null!;

        [Output("cpu")]
        public Output<Outputs.DomainCpu?> Cpu { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("disks")]
        public Output<ImmutableArray<Outputs.DomainDisk>> Disks { get; private set; } = null!;

        [Output("emulator")]
        public Output<string> Emulator { get; private set; } = null!;

        [Output("filesystems")]
        public Output<ImmutableArray<Outputs.DomainFilesystem>> Filesystems { get; private set; } = null!;

        [Output("firmware")]
        public Output<string?> Firmware { get; private set; } = null!;

        [Output("fwCfgName")]
        public Output<string?> FwCfgName { get; private set; } = null!;

        [Output("graphics")]
        public Output<Outputs.DomainGraphics?> Graphics { get; private set; } = null!;

        [Output("initrd")]
        public Output<string?> Initrd { get; private set; } = null!;

        [Output("kernel")]
        public Output<string?> Kernel { get; private set; } = null!;

        [Output("machine")]
        public Output<string> Machine { get; private set; } = null!;

        [Output("memory")]
        public Output<int?> Memory { get; private set; } = null!;

        [Output("metadata")]
        public Output<string?> Metadata { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("networkInterfaces")]
        public Output<ImmutableArray<Outputs.DomainNetworkInterface>> NetworkInterfaces { get; private set; } = null!;

        [Output("nvram")]
        public Output<Outputs.DomainNvram?> Nvram { get; private set; } = null!;

        [Output("qemuAgent")]
        public Output<bool?> QemuAgent { get; private set; } = null!;

        [Output("running")]
        public Output<bool?> Running { get; private set; } = null!;

        [Output("vcpu")]
        public Output<int?> Vcpu { get; private set; } = null!;

        [Output("video")]
        public Output<Outputs.DomainVideo?> Video { get; private set; } = null!;

        [Output("xml")]
        public Output<Outputs.DomainXml?> Xml { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs? args = null, CustomResourceOptions? options = null)
            : base("libvirt:index/domain:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
            : base("libvirt:index/domain:Domain", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, state, options);
        }
    }

    public sealed class DomainArgs : Pulumi.ResourceArgs
    {
        [Input("arch")]
        public Input<string>? Arch { get; set; }

        [Input("autostart")]
        public Input<bool>? Autostart { get; set; }

        [Input("bootDevices")]
        private InputList<Inputs.DomainBootDeviceArgs>? _bootDevices;
        public InputList<Inputs.DomainBootDeviceArgs> BootDevices
        {
            get => _bootDevices ?? (_bootDevices = new InputList<Inputs.DomainBootDeviceArgs>());
            set => _bootDevices = value;
        }

        [Input("cloudinit")]
        public Input<string>? Cloudinit { get; set; }

        [Input("cmdlines")]
        private InputList<ImmutableDictionary<string, object>>? _cmdlines;
        public InputList<ImmutableDictionary<string, object>> Cmdlines
        {
            get => _cmdlines ?? (_cmdlines = new InputList<ImmutableDictionary<string, object>>());
            set => _cmdlines = value;
        }

        [Input("consoles")]
        private InputList<Inputs.DomainConsoleArgs>? _consoles;
        public InputList<Inputs.DomainConsoleArgs> Consoles
        {
            get => _consoles ?? (_consoles = new InputList<Inputs.DomainConsoleArgs>());
            set => _consoles = value;
        }

        [Input("coreosIgnition")]
        public Input<string>? CoreosIgnition { get; set; }

        [Input("cpu")]
        public Input<Inputs.DomainCpuArgs>? Cpu { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("disks")]
        private InputList<Inputs.DomainDiskArgs>? _disks;
        public InputList<Inputs.DomainDiskArgs> Disks
        {
            get => _disks ?? (_disks = new InputList<Inputs.DomainDiskArgs>());
            set => _disks = value;
        }

        [Input("emulator")]
        public Input<string>? Emulator { get; set; }

        [Input("filesystems")]
        private InputList<Inputs.DomainFilesystemArgs>? _filesystems;
        public InputList<Inputs.DomainFilesystemArgs> Filesystems
        {
            get => _filesystems ?? (_filesystems = new InputList<Inputs.DomainFilesystemArgs>());
            set => _filesystems = value;
        }

        [Input("firmware")]
        public Input<string>? Firmware { get; set; }

        [Input("fwCfgName")]
        public Input<string>? FwCfgName { get; set; }

        [Input("graphics")]
        public Input<Inputs.DomainGraphicsArgs>? Graphics { get; set; }

        [Input("initrd")]
        public Input<string>? Initrd { get; set; }

        [Input("kernel")]
        public Input<string>? Kernel { get; set; }

        [Input("machine")]
        public Input<string>? Machine { get; set; }

        [Input("memory")]
        public Input<int>? Memory { get; set; }

        [Input("metadata")]
        public Input<string>? Metadata { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.DomainNetworkInterfaceArgs>? _networkInterfaces;
        public InputList<Inputs.DomainNetworkInterfaceArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.DomainNetworkInterfaceArgs>());
            set => _networkInterfaces = value;
        }

        [Input("nvram")]
        public Input<Inputs.DomainNvramArgs>? Nvram { get; set; }

        [Input("qemuAgent")]
        public Input<bool>? QemuAgent { get; set; }

        [Input("running")]
        public Input<bool>? Running { get; set; }

        [Input("vcpu")]
        public Input<int>? Vcpu { get; set; }

        [Input("video")]
        public Input<Inputs.DomainVideoArgs>? Video { get; set; }

        [Input("xml")]
        public Input<Inputs.DomainXmlArgs>? Xml { get; set; }

        public DomainArgs()
        {
        }
    }

    public sealed class DomainState : Pulumi.ResourceArgs
    {
        [Input("arch")]
        public Input<string>? Arch { get; set; }

        [Input("autostart")]
        public Input<bool>? Autostart { get; set; }

        [Input("bootDevices")]
        private InputList<Inputs.DomainBootDeviceGetArgs>? _bootDevices;
        public InputList<Inputs.DomainBootDeviceGetArgs> BootDevices
        {
            get => _bootDevices ?? (_bootDevices = new InputList<Inputs.DomainBootDeviceGetArgs>());
            set => _bootDevices = value;
        }

        [Input("cloudinit")]
        public Input<string>? Cloudinit { get; set; }

        [Input("cmdlines")]
        private InputList<ImmutableDictionary<string, object>>? _cmdlines;
        public InputList<ImmutableDictionary<string, object>> Cmdlines
        {
            get => _cmdlines ?? (_cmdlines = new InputList<ImmutableDictionary<string, object>>());
            set => _cmdlines = value;
        }

        [Input("consoles")]
        private InputList<Inputs.DomainConsoleGetArgs>? _consoles;
        public InputList<Inputs.DomainConsoleGetArgs> Consoles
        {
            get => _consoles ?? (_consoles = new InputList<Inputs.DomainConsoleGetArgs>());
            set => _consoles = value;
        }

        [Input("coreosIgnition")]
        public Input<string>? CoreosIgnition { get; set; }

        [Input("cpu")]
        public Input<Inputs.DomainCpuGetArgs>? Cpu { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("disks")]
        private InputList<Inputs.DomainDiskGetArgs>? _disks;
        public InputList<Inputs.DomainDiskGetArgs> Disks
        {
            get => _disks ?? (_disks = new InputList<Inputs.DomainDiskGetArgs>());
            set => _disks = value;
        }

        [Input("emulator")]
        public Input<string>? Emulator { get; set; }

        [Input("filesystems")]
        private InputList<Inputs.DomainFilesystemGetArgs>? _filesystems;
        public InputList<Inputs.DomainFilesystemGetArgs> Filesystems
        {
            get => _filesystems ?? (_filesystems = new InputList<Inputs.DomainFilesystemGetArgs>());
            set => _filesystems = value;
        }

        [Input("firmware")]
        public Input<string>? Firmware { get; set; }

        [Input("fwCfgName")]
        public Input<string>? FwCfgName { get; set; }

        [Input("graphics")]
        public Input<Inputs.DomainGraphicsGetArgs>? Graphics { get; set; }

        [Input("initrd")]
        public Input<string>? Initrd { get; set; }

        [Input("kernel")]
        public Input<string>? Kernel { get; set; }

        [Input("machine")]
        public Input<string>? Machine { get; set; }

        [Input("memory")]
        public Input<int>? Memory { get; set; }

        [Input("metadata")]
        public Input<string>? Metadata { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.DomainNetworkInterfaceGetArgs>? _networkInterfaces;
        public InputList<Inputs.DomainNetworkInterfaceGetArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.DomainNetworkInterfaceGetArgs>());
            set => _networkInterfaces = value;
        }

        [Input("nvram")]
        public Input<Inputs.DomainNvramGetArgs>? Nvram { get; set; }

        [Input("qemuAgent")]
        public Input<bool>? QemuAgent { get; set; }

        [Input("running")]
        public Input<bool>? Running { get; set; }

        [Input("vcpu")]
        public Input<int>? Vcpu { get; set; }

        [Input("video")]
        public Input<Inputs.DomainVideoGetArgs>? Video { get; set; }

        [Input("xml")]
        public Input<Inputs.DomainXmlGetArgs>? Xml { get; set; }

        public DomainState()
        {
        }
    }
}