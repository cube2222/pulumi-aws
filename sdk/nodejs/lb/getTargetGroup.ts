// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * > **Note:** `aws.alb.TargetGroup` is known as `aws.lb.TargetGroup`. The functionality is identical.
 *
 * Provides information about a Load Balancer Target Group.
 *
 * This data source can prove useful when a module accepts an LB Target Group as an
 * input variable and needs to know its attributes. It can also be used to get the ARN of
 * an LB Target Group for use in other resources, given LB Target Group name.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const config = new pulumi.Config();
 * const lbTgArn = config.get("lbTgArn") || "";
 * const lbTgName = config.get("lbTgName") || "";
 *
 * const test = pulumi.output(aws.lb.getTargetGroup({
 *     arn: lbTgArn,
 *     name: lbTgName,
 * }, { async: true }));
 * ```
 */
export function getTargetGroup(args?: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws:lb/getTargetGroup:getTargetGroup", {
        "arn": args.arn,
        "name": args.name,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupArgs {
    /**
     * The full ARN of the target group.
     */
    readonly arn?: string;
    /**
     * The unique name of the target group.
     */
    readonly name?: string;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getTargetGroup.
 */
export interface GetTargetGroupResult {
    readonly arn: string;
    readonly arnSuffix: string;
    readonly deregistrationDelay: number;
    readonly healthCheck: outputs.lb.GetTargetGroupHealthCheck;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly lambdaMultiValueHeadersEnabled: boolean;
    readonly name: string;
    readonly port: number;
    readonly protocol: string;
    readonly proxyProtocolV2: boolean;
    readonly slowStart: number;
    readonly stickiness: outputs.lb.GetTargetGroupStickiness;
    readonly tags: {[key: string]: any};
    readonly targetType: string;
    readonly vpcId: string;
}
