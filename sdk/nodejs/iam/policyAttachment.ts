// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {ARN} from "..";
import {Group, Role, User} from "./index";

/**
 * Attaches a Managed IAM Policy to user(s), role(s), and/or group(s)
 *
 * !> **WARNING:** The aws.iam.PolicyAttachment resource creates **exclusive** attachments of IAM policies. Across the entire AWS account, all of the users/roles/groups to which a single policy is attached must be declared by a single aws.iam.PolicyAttachment resource. This means that even any users/roles/groups that have the attached policy via any other mechanism (including other resources managed by this provider) will have that attached policy revoked by this resource. Consider `aws.iam.RolePolicyAttachment`, `aws.iam.UserPolicyAttachment`, or `aws.iam.GroupPolicyAttachment` instead. These resources do not enforce exclusive attachment of an IAM policy.
 *
 * > **NOTE:** The usage of this resource conflicts with the `aws.iam.GroupPolicyAttachment`, `aws.iam.RolePolicyAttachment`, and `aws.iam.UserPolicyAttachment` resources and will permanently show a difference if both are defined.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const user = new aws.iam.User("user", {});
 * const role = new aws.iam.Role("role", {
 *     assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": "sts:AssumeRole",
 *       "Principal": {
 *         "Service": "ec2.amazonaws.com"
 *       },
 *       "Effect": "Allow",
 *       "Sid": ""
 *     }
 *   ]
 * }
 * `,
 * });
 * const group = new aws.iam.Group("group", {});
 * const policy = new aws.iam.Policy("policy", {
 *     description: "A test policy",
 *     policy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": [
 *         "ec2:Describe*"
 *       ],
 *       "Effect": "Allow",
 *       "Resource": "*"
 *     }
 *   ]
 * }
 * `,
 * });
 * const testAttach = new aws.iam.PolicyAttachment("test-attach", {
 *     groups: [group.name],
 *     policyArn: policy.arn,
 *     roles: [role.name],
 *     users: [user.name],
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
    public static readonly __pulumiType = 'aws:iam/policyAttachment:PolicyAttachment';

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
     * The group(s) the policy should be applied to
     */
    public readonly groups!: pulumi.Output<string[] | undefined>;
    /**
     * The name of the attachment. This cannot be an empty string.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ARN of the policy you want to apply
     */
    public readonly policyArn!: pulumi.Output<ARN>;
    /**
     * The role(s) the policy should be applied to
     */
    public readonly roles!: pulumi.Output<string[] | undefined>;
    /**
     * The user(s) the policy should be applied to
     */
    public readonly users!: pulumi.Output<string[] | undefined>;

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
            inputs["groups"] = state ? state.groups : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["policyArn"] = state ? state.policyArn : undefined;
            inputs["roles"] = state ? state.roles : undefined;
            inputs["users"] = state ? state.users : undefined;
        } else {
            const args = argsOrState as PolicyAttachmentArgs | undefined;
            if (!args || args.policyArn === undefined) {
                throw new Error("Missing required property 'policyArn'");
            }
            inputs["groups"] = args ? args.groups : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["policyArn"] = args ? args.policyArn : undefined;
            inputs["roles"] = args ? args.roles : undefined;
            inputs["users"] = args ? args.users : undefined;
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
     * The group(s) the policy should be applied to
     */
    readonly groups?: pulumi.Input<pulumi.Input<string | Group>[]>;
    /**
     * The name of the attachment. This cannot be an empty string.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ARN of the policy you want to apply
     */
    readonly policyArn?: pulumi.Input<ARN>;
    /**
     * The role(s) the policy should be applied to
     */
    readonly roles?: pulumi.Input<pulumi.Input<string | Role>[]>;
    /**
     * The user(s) the policy should be applied to
     */
    readonly users?: pulumi.Input<pulumi.Input<string | User>[]>;
}

/**
 * The set of arguments for constructing a PolicyAttachment resource.
 */
export interface PolicyAttachmentArgs {
    /**
     * The group(s) the policy should be applied to
     */
    readonly groups?: pulumi.Input<pulumi.Input<string | Group>[]>;
    /**
     * The name of the attachment. This cannot be an empty string.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ARN of the policy you want to apply
     */
    readonly policyArn: pulumi.Input<ARN>;
    /**
     * The role(s) the policy should be applied to
     */
    readonly roles?: pulumi.Input<pulumi.Input<string | Role>[]>;
    /**
     * The user(s) the policy should be applied to
     */
    readonly users?: pulumi.Input<pulumi.Input<string | User>[]>;
}
