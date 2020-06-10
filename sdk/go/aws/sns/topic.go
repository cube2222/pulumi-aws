// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sns

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an SNS topic resource
//
// ## Example Usage
//
//
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/sns"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		userUpdates, err := sns.NewTopic(ctx, "userUpdates", nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Example with Delivery Policy
//
//
// ## Example with Server-side encryption (SSE)
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/sns"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		userUpdates, err := sns.NewTopic(ctx, "userUpdates", &sns.TopicArgs{
// 			KmsMasterKeyId: pulumi.String("alias/aws/sns"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Message Delivery Status Arguments
//
// The `<endpoint>_success_feedback_role_arn` and `<endpoint>_failure_feedback_role_arn` arguments are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The `<endpoint>_success_feedback_sample_rate` argument is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the  `<endpoint>_failure_feedback_role_arn` argument, then all failed message deliveries generate CloudWatch Logs.
type Topic struct {
	pulumi.CustomResourceState

	// IAM role for failure feedback
	ApplicationFailureFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"applicationFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	ApplicationSuccessFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"applicationSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	ApplicationSuccessFeedbackSampleRate pulumi.IntPtrOutput `pulumi:"applicationSuccessFeedbackSampleRate"`
	// The ARN of the SNS topic, as a more obvious property (clone of id)
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
	DeliveryPolicy pulumi.StringPtrOutput `pulumi:"deliveryPolicy"`
	// The display name for the SNS topic
	DisplayName pulumi.StringPtrOutput `pulumi:"displayName"`
	// IAM role for failure feedback
	HttpFailureFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"httpFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	HttpSuccessFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"httpSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	HttpSuccessFeedbackSampleRate pulumi.IntPtrOutput `pulumi:"httpSuccessFeedbackSampleRate"`
	// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
	KmsMasterKeyId pulumi.StringPtrOutput `pulumi:"kmsMasterKeyId"`
	// IAM role for failure feedback
	LambdaFailureFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"lambdaFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	LambdaSuccessFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"lambdaSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	LambdaSuccessFeedbackSampleRate pulumi.IntPtrOutput `pulumi:"lambdaSuccessFeedbackSampleRate"`
	// The friendly name for the SNS topic. By default generated by this provider.
	Name pulumi.StringOutput `pulumi:"name"`
	// The friendly name for the SNS topic. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// The fully-formed AWS policy as JSON.
	Policy pulumi.StringOutput `pulumi:"policy"`
	// IAM role for failure feedback
	SqsFailureFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"sqsFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	SqsSuccessFeedbackRoleArn pulumi.StringPtrOutput `pulumi:"sqsSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	SqsSuccessFeedbackSampleRate pulumi.IntPtrOutput `pulumi:"sqsSuccessFeedbackSampleRate"`
	// Key-value map of resource tags
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewTopic registers a new resource with the given unique name, arguments, and options.
func NewTopic(ctx *pulumi.Context,
	name string, args *TopicArgs, opts ...pulumi.ResourceOption) (*Topic, error) {
	if args == nil {
		args = &TopicArgs{}
	}
	var resource Topic
	err := ctx.RegisterResource("aws:sns/topic:Topic", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTopic gets an existing Topic resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTopic(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TopicState, opts ...pulumi.ResourceOption) (*Topic, error) {
	var resource Topic
	err := ctx.ReadResource("aws:sns/topic:Topic", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Topic resources.
type topicState struct {
	// IAM role for failure feedback
	ApplicationFailureFeedbackRoleArn *string `pulumi:"applicationFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	ApplicationSuccessFeedbackRoleArn *string `pulumi:"applicationSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	ApplicationSuccessFeedbackSampleRate *int `pulumi:"applicationSuccessFeedbackSampleRate"`
	// The ARN of the SNS topic, as a more obvious property (clone of id)
	Arn *string `pulumi:"arn"`
	// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
	DeliveryPolicy *string `pulumi:"deliveryPolicy"`
	// The display name for the SNS topic
	DisplayName *string `pulumi:"displayName"`
	// IAM role for failure feedback
	HttpFailureFeedbackRoleArn *string `pulumi:"httpFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	HttpSuccessFeedbackRoleArn *string `pulumi:"httpSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	HttpSuccessFeedbackSampleRate *int `pulumi:"httpSuccessFeedbackSampleRate"`
	// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
	KmsMasterKeyId *string `pulumi:"kmsMasterKeyId"`
	// IAM role for failure feedback
	LambdaFailureFeedbackRoleArn *string `pulumi:"lambdaFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	LambdaSuccessFeedbackRoleArn *string `pulumi:"lambdaSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	LambdaSuccessFeedbackSampleRate *int `pulumi:"lambdaSuccessFeedbackSampleRate"`
	// The friendly name for the SNS topic. By default generated by this provider.
	Name *string `pulumi:"name"`
	// The friendly name for the SNS topic. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The fully-formed AWS policy as JSON.
	Policy *string `pulumi:"policy"`
	// IAM role for failure feedback
	SqsFailureFeedbackRoleArn *string `pulumi:"sqsFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	SqsSuccessFeedbackRoleArn *string `pulumi:"sqsSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	SqsSuccessFeedbackSampleRate *int `pulumi:"sqsSuccessFeedbackSampleRate"`
	// Key-value map of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

type TopicState struct {
	// IAM role for failure feedback
	ApplicationFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	ApplicationSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	ApplicationSuccessFeedbackSampleRate pulumi.IntPtrInput
	// The ARN of the SNS topic, as a more obvious property (clone of id)
	Arn pulumi.StringPtrInput
	// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
	DeliveryPolicy pulumi.StringPtrInput
	// The display name for the SNS topic
	DisplayName pulumi.StringPtrInput
	// IAM role for failure feedback
	HttpFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	HttpSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	HttpSuccessFeedbackSampleRate pulumi.IntPtrInput
	// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
	KmsMasterKeyId pulumi.StringPtrInput
	// IAM role for failure feedback
	LambdaFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	LambdaSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	LambdaSuccessFeedbackSampleRate pulumi.IntPtrInput
	// The friendly name for the SNS topic. By default generated by this provider.
	Name pulumi.StringPtrInput
	// The friendly name for the SNS topic. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The fully-formed AWS policy as JSON.
	Policy pulumi.StringPtrInput
	// IAM role for failure feedback
	SqsFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	SqsSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	SqsSuccessFeedbackSampleRate pulumi.IntPtrInput
	// Key-value map of resource tags
	Tags pulumi.MapInput
}

func (TopicState) ElementType() reflect.Type {
	return reflect.TypeOf((*topicState)(nil)).Elem()
}

type topicArgs struct {
	// IAM role for failure feedback
	ApplicationFailureFeedbackRoleArn *string `pulumi:"applicationFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	ApplicationSuccessFeedbackRoleArn *string `pulumi:"applicationSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	ApplicationSuccessFeedbackSampleRate *int `pulumi:"applicationSuccessFeedbackSampleRate"`
	// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
	DeliveryPolicy *string `pulumi:"deliveryPolicy"`
	// The display name for the SNS topic
	DisplayName *string `pulumi:"displayName"`
	// IAM role for failure feedback
	HttpFailureFeedbackRoleArn *string `pulumi:"httpFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	HttpSuccessFeedbackRoleArn *string `pulumi:"httpSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	HttpSuccessFeedbackSampleRate *int `pulumi:"httpSuccessFeedbackSampleRate"`
	// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
	KmsMasterKeyId *string `pulumi:"kmsMasterKeyId"`
	// IAM role for failure feedback
	LambdaFailureFeedbackRoleArn *string `pulumi:"lambdaFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	LambdaSuccessFeedbackRoleArn *string `pulumi:"lambdaSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	LambdaSuccessFeedbackSampleRate *int `pulumi:"lambdaSuccessFeedbackSampleRate"`
	// The friendly name for the SNS topic. By default generated by this provider.
	Name *string `pulumi:"name"`
	// The friendly name for the SNS topic. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The fully-formed AWS policy as JSON.
	Policy *string `pulumi:"policy"`
	// IAM role for failure feedback
	SqsFailureFeedbackRoleArn *string `pulumi:"sqsFailureFeedbackRoleArn"`
	// The IAM role permitted to receive success feedback for this topic
	SqsSuccessFeedbackRoleArn *string `pulumi:"sqsSuccessFeedbackRoleArn"`
	// Percentage of success to sample
	SqsSuccessFeedbackSampleRate *int `pulumi:"sqsSuccessFeedbackSampleRate"`
	// Key-value map of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Topic resource.
type TopicArgs struct {
	// IAM role for failure feedback
	ApplicationFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	ApplicationSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	ApplicationSuccessFeedbackSampleRate pulumi.IntPtrInput
	// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
	DeliveryPolicy pulumi.StringPtrInput
	// The display name for the SNS topic
	DisplayName pulumi.StringPtrInput
	// IAM role for failure feedback
	HttpFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	HttpSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	HttpSuccessFeedbackSampleRate pulumi.IntPtrInput
	// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
	KmsMasterKeyId pulumi.StringPtrInput
	// IAM role for failure feedback
	LambdaFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	LambdaSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	LambdaSuccessFeedbackSampleRate pulumi.IntPtrInput
	// The friendly name for the SNS topic. By default generated by this provider.
	Name pulumi.StringPtrInput
	// The friendly name for the SNS topic. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The fully-formed AWS policy as JSON.
	Policy pulumi.StringPtrInput
	// IAM role for failure feedback
	SqsFailureFeedbackRoleArn pulumi.StringPtrInput
	// The IAM role permitted to receive success feedback for this topic
	SqsSuccessFeedbackRoleArn pulumi.StringPtrInput
	// Percentage of success to sample
	SqsSuccessFeedbackSampleRate pulumi.IntPtrInput
	// Key-value map of resource tags
	Tags pulumi.MapInput
}

func (TopicArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*topicArgs)(nil)).Elem()
}
