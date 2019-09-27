// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a static IP address attachment - relationship between a Lightsail static IP & Lightsail instance.
 * 
 * > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const testInstance = new aws.lightsail.Instance("test", {
 *     availabilityZone: "us-east-1b",
 *     blueprintId: "string",
 *     bundleId: "string",
 *     keyPairName: "someKeyName",
 * });
 * const testStaticIp = new aws.lightsail.StaticIp("test", {});
 * const testStaticIpAttachment = new aws.lightsail.StaticIpAttachment("test", {
 *     instanceName: testInstance.name,
 *     staticIpName: testStaticIp.name,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_static_ip_attachment.html.markdown.
 */
export class StaticIpAttachment extends pulumi.CustomResource {
    /**
     * Get an existing StaticIpAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StaticIpAttachmentState, opts?: pulumi.CustomResourceOptions): StaticIpAttachment {
        return new StaticIpAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:lightsail/staticIpAttachment:StaticIpAttachment';

    /**
     * Returns true if the given object is an instance of StaticIpAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StaticIpAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StaticIpAttachment.__pulumiType;
    }

    /**
     * The name of the Lightsail instance to attach the IP to
     */
    public readonly instanceName!: pulumi.Output<string>;
    /**
     * The allocated static IP address
     */
    public /*out*/ readonly ipAddress!: pulumi.Output<string>;
    /**
     * The name of the allocated static IP
     */
    public readonly staticIpName!: pulumi.Output<string>;

    /**
     * Create a StaticIpAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StaticIpAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StaticIpAttachmentArgs | StaticIpAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as StaticIpAttachmentState | undefined;
            inputs["instanceName"] = state ? state.instanceName : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["staticIpName"] = state ? state.staticIpName : undefined;
        } else {
            const args = argsOrState as StaticIpAttachmentArgs | undefined;
            if (!args || args.instanceName === undefined) {
                throw new Error("Missing required property 'instanceName'");
            }
            if (!args || args.staticIpName === undefined) {
                throw new Error("Missing required property 'staticIpName'");
            }
            inputs["instanceName"] = args ? args.instanceName : undefined;
            inputs["staticIpName"] = args ? args.staticIpName : undefined;
            inputs["ipAddress"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(StaticIpAttachment.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering StaticIpAttachment resources.
 */
export interface StaticIpAttachmentState {
    /**
     * The name of the Lightsail instance to attach the IP to
     */
    readonly instanceName?: pulumi.Input<string>;
    /**
     * The allocated static IP address
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * The name of the allocated static IP
     */
    readonly staticIpName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a StaticIpAttachment resource.
 */
export interface StaticIpAttachmentArgs {
    /**
     * The name of the Lightsail instance to attach the IP to
     */
    readonly instanceName: pulumi.Input<string>;
    /**
     * The name of the allocated static IP
     */
    readonly staticIpName: pulumi.Input<string>;
}
