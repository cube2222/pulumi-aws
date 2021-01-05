// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Lambda Code Signing Config resource. A code signing configuration defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail).
//
// For information about Lambda code signing configurations and how to use them, see [configuring code signing for Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/lambda"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := lambda.NewCodeSigningConfig(ctx, "newCsc", &lambda.CodeSigningConfigArgs{
// 			AllowedPublishers: &lambda.CodeSigningConfigAllowedPublishersArgs{
// 				SigningProfileVersionArns: pulumi.StringArray{
// 					pulumi.Any(aws_signer_signing_profile.Example1.Arn),
// 					pulumi.Any(aws_signer_signing_profile.Example2.Arn),
// 				},
// 			},
// 			Policies: &lambda.CodeSigningConfigPoliciesArgs{
// 				UntrustedArtifactOnDeployment: pulumi.String("Warn"),
// 			},
// 			Description: pulumi.String("My awesome code signing config."),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Code Signing Configs can be imported using their ARN, e.g.
//
// ```sh
//  $ pulumi import aws:lambda/codeSigningConfig:CodeSigningConfig imported_csc arn:aws:lambda:us-west-2:123456789012:code-signing-config:csc-0f6c334abcdea4d8b
// ```
type CodeSigningConfig struct {
	pulumi.CustomResourceState

	// A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
	AllowedPublishers CodeSigningConfigAllowedPublishersOutput `pulumi:"allowedPublishers"`
	// The Amazon Resource Name (ARN) of the code signing configuration.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Unique identifier for the code signing configuration.
	ConfigId pulumi.StringOutput `pulumi:"configId"`
	// Descriptive name for this code signing configuration.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The date and time that the code signing configuration was last modified.
	LastModified pulumi.StringOutput `pulumi:"lastModified"`
	// A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
	Policies CodeSigningConfigPoliciesOutput `pulumi:"policies"`
}

// NewCodeSigningConfig registers a new resource with the given unique name, arguments, and options.
func NewCodeSigningConfig(ctx *pulumi.Context,
	name string, args *CodeSigningConfigArgs, opts ...pulumi.ResourceOption) (*CodeSigningConfig, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AllowedPublishers == nil {
		return nil, errors.New("invalid value for required argument 'AllowedPublishers'")
	}
	var resource CodeSigningConfig
	err := ctx.RegisterResource("aws:lambda/codeSigningConfig:CodeSigningConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCodeSigningConfig gets an existing CodeSigningConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCodeSigningConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CodeSigningConfigState, opts ...pulumi.ResourceOption) (*CodeSigningConfig, error) {
	var resource CodeSigningConfig
	err := ctx.ReadResource("aws:lambda/codeSigningConfig:CodeSigningConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CodeSigningConfig resources.
type codeSigningConfigState struct {
	// A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
	AllowedPublishers *CodeSigningConfigAllowedPublishers `pulumi:"allowedPublishers"`
	// The Amazon Resource Name (ARN) of the code signing configuration.
	Arn *string `pulumi:"arn"`
	// Unique identifier for the code signing configuration.
	ConfigId *string `pulumi:"configId"`
	// Descriptive name for this code signing configuration.
	Description *string `pulumi:"description"`
	// The date and time that the code signing configuration was last modified.
	LastModified *string `pulumi:"lastModified"`
	// A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
	Policies *CodeSigningConfigPolicies `pulumi:"policies"`
}

type CodeSigningConfigState struct {
	// A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
	AllowedPublishers CodeSigningConfigAllowedPublishersPtrInput
	// The Amazon Resource Name (ARN) of the code signing configuration.
	Arn pulumi.StringPtrInput
	// Unique identifier for the code signing configuration.
	ConfigId pulumi.StringPtrInput
	// Descriptive name for this code signing configuration.
	Description pulumi.StringPtrInput
	// The date and time that the code signing configuration was last modified.
	LastModified pulumi.StringPtrInput
	// A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
	Policies CodeSigningConfigPoliciesPtrInput
}

func (CodeSigningConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*codeSigningConfigState)(nil)).Elem()
}

type codeSigningConfigArgs struct {
	// A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
	AllowedPublishers CodeSigningConfigAllowedPublishers `pulumi:"allowedPublishers"`
	// Descriptive name for this code signing configuration.
	Description *string `pulumi:"description"`
	// A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
	Policies *CodeSigningConfigPolicies `pulumi:"policies"`
}

// The set of arguments for constructing a CodeSigningConfig resource.
type CodeSigningConfigArgs struct {
	// A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
	AllowedPublishers CodeSigningConfigAllowedPublishersInput
	// Descriptive name for this code signing configuration.
	Description pulumi.StringPtrInput
	// A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
	Policies CodeSigningConfigPoliciesPtrInput
}

func (CodeSigningConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*codeSigningConfigArgs)(nil)).Elem()
}

type CodeSigningConfigInput interface {
	pulumi.Input

	ToCodeSigningConfigOutput() CodeSigningConfigOutput
	ToCodeSigningConfigOutputWithContext(ctx context.Context) CodeSigningConfigOutput
}

func (*CodeSigningConfig) ElementType() reflect.Type {
	return reflect.TypeOf((*CodeSigningConfig)(nil))
}

func (i *CodeSigningConfig) ToCodeSigningConfigOutput() CodeSigningConfigOutput {
	return i.ToCodeSigningConfigOutputWithContext(context.Background())
}

func (i *CodeSigningConfig) ToCodeSigningConfigOutputWithContext(ctx context.Context) CodeSigningConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CodeSigningConfigOutput)
}

type CodeSigningConfigOutput struct {
	*pulumi.OutputState
}

func (CodeSigningConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CodeSigningConfig)(nil))
}

func (o CodeSigningConfigOutput) ToCodeSigningConfigOutput() CodeSigningConfigOutput {
	return o
}

func (o CodeSigningConfigOutput) ToCodeSigningConfigOutputWithContext(ctx context.Context) CodeSigningConfigOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CodeSigningConfigOutput{})
}
