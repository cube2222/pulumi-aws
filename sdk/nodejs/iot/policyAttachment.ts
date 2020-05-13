// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {ARN} from "..";
import {Policy} from "./index";

/**
 * Provides an IoT policy attachment.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as fs from "fs";
 *
 * const pubsub = new aws.iot.Policy("pubsub", {
 *     policy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": [
 *         "iot:*"
 *       ],
 *       "Effect": "Allow",
 *       "Resource": "*"
 *     }
 *   ]
 * }
 * `,
 * });
 * const cert = new aws.iot.Certificate("cert", {
 *     active: true,
 *     csr: fs.readFileSync("csr.pem", "utf-8"),
 * });
 * const att = new aws.iot.PolicyAttachment("att", {
 *     policy: pubsub.name,
 *     target: cert.arn,
 * });
 * ```
 */
export class PolicyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing PolicyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyAttachmentState, opts?: pulumi.CustomResourceOptions): PolicyAttachment {
        return new PolicyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:iot/policyAttachment:PolicyAttachment';

    /**
     * Returns true if the given object is an instance of PolicyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PolicyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PolicyAttachment.__pulumiType;
    }

    /**
     * The name of the policy to attach.
     */
    public readonly policy!: pulumi.Output<string>;
    /**
     * The identity to which the policy is attached.
     */
    public readonly target!: pulumi.Output<ARN>;

    /**
     * Create a PolicyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PolicyAttachmentArgs | PolicyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PolicyAttachmentState | undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["target"] = state ? state.target : undefined;
        } else {
            const args = argsOrState as PolicyAttachmentArgs | undefined;
            if (!args || args.policy === undefined) {
                throw new Error("Missing required property 'policy'");
            }
            if (!args || args.target === undefined) {
                throw new Error("Missing required property 'target'");
            }
            inputs["policy"] = args ? args.policy : undefined;
            inputs["target"] = args ? args.target : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(PolicyAttachment.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PolicyAttachment resources.
 */
export interface PolicyAttachmentState {
    /**
     * The name of the policy to attach.
     */
    readonly policy?: pulumi.Input<string | Policy>;
    /**
     * The identity to which the policy is attached.
     */
    readonly target?: pulumi.Input<ARN>;
}

/**
 * The set of arguments for constructing a PolicyAttachment resource.
 */
export interface PolicyAttachmentArgs {
    /**
     * The name of the policy to attach.
     */
    readonly policy: pulumi.Input<string | Policy>;
    /**
     * The identity to which the policy is attached.
     */
    readonly target: pulumi.Input<ARN>;
}
