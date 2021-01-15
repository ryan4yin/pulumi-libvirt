// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Ignition extends pulumi.CustomResource {
    /**
     * Get an existing Ignition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IgnitionState, opts?: pulumi.CustomResourceOptions): Ignition {
        return new Ignition(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'libvirt:index/ignition:Ignition';

    /**
     * Returns true if the given object is an instance of Ignition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Ignition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Ignition.__pulumiType;
    }

    public readonly content!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly pool!: pulumi.Output<string | undefined>;

    /**
     * Create a Ignition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IgnitionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IgnitionArgs | IgnitionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IgnitionState | undefined;
            inputs["content"] = state ? state.content : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["pool"] = state ? state.pool : undefined;
        } else {
            const args = argsOrState as IgnitionArgs | undefined;
            if (!args || args.content === undefined) {
                throw new Error("Missing required property 'content'");
            }
            inputs["content"] = args ? args.content : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["pool"] = args ? args.pool : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Ignition.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Ignition resources.
 */
export interface IgnitionState {
    readonly content?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly pool?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Ignition resource.
 */
export interface IgnitionArgs {
    readonly content: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly pool?: pulumi.Input<string>;
}
