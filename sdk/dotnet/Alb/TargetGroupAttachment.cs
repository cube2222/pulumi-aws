// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Alb
{
    /// <summary>
    /// Provides the ability to register instances and containers with an Application Load Balancer (ALB) or Network Load Balancer (NLB) target group. For attaching resources with Elastic Load Balancer (ELB), see the `aws.elb.Attachment` resource.
    /// 
    /// &gt; **Note:** `aws.alb.TargetGroupAttachment` is known as `aws.lb.TargetGroupAttachment`. The functionality is identical.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var testTargetGroup = new Aws.LB.TargetGroup("testTargetGroup", new Aws.LB.TargetGroupArgs
    ///         {
    ///         });
    ///         // ... other configuration ...
    ///         var testInstance = new Aws.Ec2.Instance("testInstance", new Aws.Ec2.InstanceArgs
    ///         {
    ///         });
    ///         // ... other configuration ...
    ///         var testTargetGroupAttachment = new Aws.LB.TargetGroupAttachment("testTargetGroupAttachment", new Aws.LB.TargetGroupAttachmentArgs
    ///         {
    ///             TargetGroupArn = testTargetGroup.Arn,
    ///             TargetId = testInstance.Id,
    ///             Port = 80,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Usage with lambda
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var testTargetGroup = new Aws.LB.TargetGroup("testTargetGroup", new Aws.LB.TargetGroupArgs
    ///         {
    ///             TargetType = "lambda",
    ///         });
    ///         var testFunction = new Aws.Lambda.Function("testFunction", new Aws.Lambda.FunctionArgs
    ///         {
    ///         });
    ///         // ... other configuration ...
    ///         var withLb = new Aws.Lambda.Permission("withLb", new Aws.Lambda.PermissionArgs
    ///         {
    ///             Action = "lambda:InvokeFunction",
    ///             Function = testFunction.Arn,
    ///             Principal = "elasticloadbalancing.amazonaws.com",
    ///             SourceArn = testTargetGroup.Arn,
    ///         });
    ///         var testTargetGroupAttachment = new Aws.LB.TargetGroupAttachment("testTargetGroupAttachment", new Aws.LB.TargetGroupAttachmentArgs
    ///         {
    ///             TargetGroupArn = testTargetGroup.Arn,
    ///             TargetId = testFunction.Arn,
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 withLb,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Target Group Attachments cannot be imported.
    /// </summary>
    [AwsResourceType("aws:alb/targetGroupAttachment:TargetGroupAttachment")]
    public partial class TargetGroupAttachment : Pulumi.CustomResource
    {
        /// <summary>
        /// The Availability Zone where the IP address of the target is to be registered. If the private ip address is outside of the VPC scope, this value must be set to 'all'.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string?> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The port on which targets receive traffic.
        /// </summary>
        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        /// <summary>
        /// The ARN of the target group with which to register targets
        /// </summary>
        [Output("targetGroupArn")]
        public Output<string> TargetGroupArn { get; private set; } = null!;

        /// <summary>
        /// The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.
        /// </summary>
        [Output("targetId")]
        public Output<string> TargetId { get; private set; } = null!;


        /// <summary>
        /// Create a TargetGroupAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TargetGroupAttachment(string name, TargetGroupAttachmentArgs args, CustomResourceOptions? options = null)
            : base("aws:alb/targetGroupAttachment:TargetGroupAttachment", name, args ?? new TargetGroupAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TargetGroupAttachment(string name, Input<string> id, TargetGroupAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("aws:alb/targetGroupAttachment:TargetGroupAttachment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                Aliases =
                {
                    new Pulumi.Alias { Type = "aws:applicationloadbalancing/targetGroupAttachment:TargetGroupAttachment"},
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TargetGroupAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TargetGroupAttachment Get(string name, Input<string> id, TargetGroupAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new TargetGroupAttachment(name, id, state, options);
        }
    }

    public sealed class TargetGroupAttachmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Availability Zone where the IP address of the target is to be registered. If the private ip address is outside of the VPC scope, this value must be set to 'all'.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The port on which targets receive traffic.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The ARN of the target group with which to register targets
        /// </summary>
        [Input("targetGroupArn", required: true)]
        public Input<string> TargetGroupArn { get; set; } = null!;

        /// <summary>
        /// The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.
        /// </summary>
        [Input("targetId", required: true)]
        public Input<string> TargetId { get; set; } = null!;

        public TargetGroupAttachmentArgs()
        {
        }
    }

    public sealed class TargetGroupAttachmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Availability Zone where the IP address of the target is to be registered. If the private ip address is outside of the VPC scope, this value must be set to 'all'.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The port on which targets receive traffic.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The ARN of the target group with which to register targets
        /// </summary>
        [Input("targetGroupArn")]
        public Input<string>? TargetGroupArn { get; set; }

        /// <summary>
        /// The ID of the target. This is the Instance ID for an instance, or the container ID for an ECS container. If the target type is ip, specify an IP address. If the target type is lambda, specify the arn of lambda.
        /// </summary>
        [Input("targetId")]
        public Input<string>? TargetId { get; set; }

        public TargetGroupAttachmentState()
        {
        }
    }
}
