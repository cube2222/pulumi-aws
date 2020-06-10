// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS, enabling serverless backend solutions. The Lambda Function itself includes source code and runtime configuration.
//
// For information about Lambda and how to use it, see [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
//
// > **NOTE:** Due to [AWS Lambda improved VPC networking changes that began deploying in September 2019](https://aws.amazon.com/blogs/compute/announcing-improved-vpc-networking-for-aws-lambda-functions/), EC2 subnets and security groups associated with Lambda Functions can take up to 45 minutes to successfully delete.
//
// ## Example Usage
//
// ### Lambda Layers
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/lambda"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleLayerVersion, err := lambda.NewLayerVersion(ctx, "exampleLayerVersion", nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleFunction, err := lambda.NewFunction(ctx, "exampleFunction", &lambda.FunctionArgs{
// 			Layers: pulumi.StringArray{
// 				exampleLayerVersion.Arn,
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Specifying the Deployment Package
//
// AWS Lambda expects source code to be provided as a deployment package whose structure varies depending on which `runtime` is in use.
// See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for the valid values of `runtime`. The expected structure of the deployment package can be found in
// [the AWS Lambda documentation for each runtime](https://docs.aws.amazon.com/lambda/latest/dg/deployment-package-v2.html).
//
// Once you have created your deployment package you can specify it either directly as a local file (using the `filename` argument) or
// indirectly via Amazon S3 (using the `s3Bucket`, `s3Key` and `s3ObjectVersion` arguments). When providing the deployment
// package via S3 it may be useful to use the `s3.BucketObject` resource to upload it.
//
// For larger deployment packages it is recommended by Amazon to upload via S3, since the S3 API has better support for uploading
// large files efficiently.
type Function struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) identifying your Lambda Function.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
	Code pulumi.ArchiveOutput `pulumi:"code"`
	// Nested block to configure the function's *dead letter queue*. See details below.
	DeadLetterConfig FunctionDeadLetterConfigPtrOutput `pulumi:"deadLetterConfig"`
	// Description of what your Lambda Function does.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The Lambda environment's configuration settings. Fields documented below.
	Environment FunctionEnvironmentPtrOutput `pulumi:"environment"`
	// The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
	Handler pulumi.StringOutput `pulumi:"handler"`
	// The ARN to be used for invoking Lambda Function from API Gateway - to be used in `apigateway.Integration`'s `uri`
	InvokeArn pulumi.StringOutput `pulumi:"invokeArn"`
	// Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to encrypt environment variables. If this configuration is not provided when environment variables are in use, AWS Lambda uses a default service key. If this configuration is provided when environment variables are not in use, the AWS Lambda API does not save this configuration and this provider will show a perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.
	KmsKeyArn pulumi.StringPtrOutput `pulumi:"kmsKeyArn"`
	// The date this resource was last modified.
	LastModified pulumi.StringOutput `pulumi:"lastModified"`
	// List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
	Layers pulumi.StringArrayOutput `pulumi:"layers"`
	// Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	MemorySize pulumi.IntPtrOutput `pulumi:"memorySize"`
	// A unique name for your Lambda Function.
	Name pulumi.StringOutput `pulumi:"name"`
	// Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
	Publish pulumi.BoolPtrOutput `pulumi:"publish"`
	// The Amazon Resource Name (ARN) identifying your Lambda Function Version
	// (if versioning is enabled via `publish = true`).
	QualifiedArn pulumi.StringOutput `pulumi:"qualifiedArn"`
	// The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
	ReservedConcurrentExecutions pulumi.IntPtrOutput `pulumi:"reservedConcurrentExecutions"`
	// IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
	Role pulumi.StringOutput `pulumi:"role"`
	// See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
	Runtime pulumi.StringOutput `pulumi:"runtime"`
	// The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
	S3Bucket pulumi.StringPtrOutput `pulumi:"s3Bucket"`
	// The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
	S3Key pulumi.StringPtrOutput `pulumi:"s3Key"`
	// The object version containing the function's deployment package. Conflicts with `filename`.
	S3ObjectVersion pulumi.StringPtrOutput `pulumi:"s3ObjectVersion"`
	// Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3Key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
	SourceCodeHash pulumi.StringOutput `pulumi:"sourceCodeHash"`
	// The size in bytes of the function .zip file.
	SourceCodeSize pulumi.IntOutput `pulumi:"sourceCodeSize"`
	// A mapping of tags to assign to the object.
	Tags pulumi.MapOutput `pulumi:"tags"`
	// The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	Timeout       pulumi.IntPtrOutput         `pulumi:"timeout"`
	TracingConfig FunctionTracingConfigOutput `pulumi:"tracingConfig"`
	// Latest published version of your Lambda Function.
	Version pulumi.StringOutput `pulumi:"version"`
	// Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
	VpcConfig FunctionVpcConfigPtrOutput `pulumi:"vpcConfig"`
}

// NewFunction registers a new resource with the given unique name, arguments, and options.
func NewFunction(ctx *pulumi.Context,
	name string, args *FunctionArgs, opts ...pulumi.ResourceOption) (*Function, error) {
	if args == nil || args.Handler == nil {
		return nil, errors.New("missing required argument 'Handler'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	if args == nil || args.Runtime == nil {
		return nil, errors.New("missing required argument 'Runtime'")
	}
	if args == nil {
		args = &FunctionArgs{}
	}
	var resource Function
	err := ctx.RegisterResource("aws:lambda/function:Function", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFunction gets an existing Function resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFunction(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FunctionState, opts ...pulumi.ResourceOption) (*Function, error) {
	var resource Function
	err := ctx.ReadResource("aws:lambda/function:Function", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Function resources.
type functionState struct {
	// The Amazon Resource Name (ARN) identifying your Lambda Function.
	Arn *string `pulumi:"arn"`
	// The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
	Code pulumi.Archive `pulumi:"code"`
	// Nested block to configure the function's *dead letter queue*. See details below.
	DeadLetterConfig *FunctionDeadLetterConfig `pulumi:"deadLetterConfig"`
	// Description of what your Lambda Function does.
	Description *string `pulumi:"description"`
	// The Lambda environment's configuration settings. Fields documented below.
	Environment *FunctionEnvironment `pulumi:"environment"`
	// The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
	Handler *string `pulumi:"handler"`
	// The ARN to be used for invoking Lambda Function from API Gateway - to be used in `apigateway.Integration`'s `uri`
	InvokeArn *string `pulumi:"invokeArn"`
	// Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to encrypt environment variables. If this configuration is not provided when environment variables are in use, AWS Lambda uses a default service key. If this configuration is provided when environment variables are not in use, the AWS Lambda API does not save this configuration and this provider will show a perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
	// The date this resource was last modified.
	LastModified *string `pulumi:"lastModified"`
	// List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
	Layers []string `pulumi:"layers"`
	// Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	MemorySize *int `pulumi:"memorySize"`
	// A unique name for your Lambda Function.
	Name *string `pulumi:"name"`
	// Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
	Publish *bool `pulumi:"publish"`
	// The Amazon Resource Name (ARN) identifying your Lambda Function Version
	// (if versioning is enabled via `publish = true`).
	QualifiedArn *string `pulumi:"qualifiedArn"`
	// The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
	ReservedConcurrentExecutions *int `pulumi:"reservedConcurrentExecutions"`
	// IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
	Role *string `pulumi:"role"`
	// See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
	Runtime *string `pulumi:"runtime"`
	// The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
	S3Bucket *string `pulumi:"s3Bucket"`
	// The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
	S3Key *string `pulumi:"s3Key"`
	// The object version containing the function's deployment package. Conflicts with `filename`.
	S3ObjectVersion *string `pulumi:"s3ObjectVersion"`
	// Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3Key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
	SourceCodeHash *string `pulumi:"sourceCodeHash"`
	// The size in bytes of the function .zip file.
	SourceCodeSize *int `pulumi:"sourceCodeSize"`
	// A mapping of tags to assign to the object.
	Tags map[string]interface{} `pulumi:"tags"`
	// The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	Timeout       *int                   `pulumi:"timeout"`
	TracingConfig *FunctionTracingConfig `pulumi:"tracingConfig"`
	// Latest published version of your Lambda Function.
	Version *string `pulumi:"version"`
	// Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
	VpcConfig *FunctionVpcConfig `pulumi:"vpcConfig"`
}

type FunctionState struct {
	// The Amazon Resource Name (ARN) identifying your Lambda Function.
	Arn pulumi.StringPtrInput
	// The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
	Code pulumi.ArchiveInput
	// Nested block to configure the function's *dead letter queue*. See details below.
	DeadLetterConfig FunctionDeadLetterConfigPtrInput
	// Description of what your Lambda Function does.
	Description pulumi.StringPtrInput
	// The Lambda environment's configuration settings. Fields documented below.
	Environment FunctionEnvironmentPtrInput
	// The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
	Handler pulumi.StringPtrInput
	// The ARN to be used for invoking Lambda Function from API Gateway - to be used in `apigateway.Integration`'s `uri`
	InvokeArn pulumi.StringPtrInput
	// Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to encrypt environment variables. If this configuration is not provided when environment variables are in use, AWS Lambda uses a default service key. If this configuration is provided when environment variables are not in use, the AWS Lambda API does not save this configuration and this provider will show a perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.
	KmsKeyArn pulumi.StringPtrInput
	// The date this resource was last modified.
	LastModified pulumi.StringPtrInput
	// List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
	Layers pulumi.StringArrayInput
	// Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	MemorySize pulumi.IntPtrInput
	// A unique name for your Lambda Function.
	Name pulumi.StringPtrInput
	// Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
	Publish pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) identifying your Lambda Function Version
	// (if versioning is enabled via `publish = true`).
	QualifiedArn pulumi.StringPtrInput
	// The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
	ReservedConcurrentExecutions pulumi.IntPtrInput
	// IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
	Role pulumi.StringPtrInput
	// See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
	Runtime pulumi.StringPtrInput
	// The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
	S3Bucket pulumi.StringPtrInput
	// The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
	S3Key pulumi.StringPtrInput
	// The object version containing the function's deployment package. Conflicts with `filename`.
	S3ObjectVersion pulumi.StringPtrInput
	// Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3Key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
	SourceCodeHash pulumi.StringPtrInput
	// The size in bytes of the function .zip file.
	SourceCodeSize pulumi.IntPtrInput
	// A mapping of tags to assign to the object.
	Tags pulumi.MapInput
	// The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	Timeout       pulumi.IntPtrInput
	TracingConfig FunctionTracingConfigPtrInput
	// Latest published version of your Lambda Function.
	Version pulumi.StringPtrInput
	// Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
	VpcConfig FunctionVpcConfigPtrInput
}

func (FunctionState) ElementType() reflect.Type {
	return reflect.TypeOf((*functionState)(nil)).Elem()
}

type functionArgs struct {
	// The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
	Code pulumi.Archive `pulumi:"code"`
	// Nested block to configure the function's *dead letter queue*. See details below.
	DeadLetterConfig *FunctionDeadLetterConfig `pulumi:"deadLetterConfig"`
	// Description of what your Lambda Function does.
	Description *string `pulumi:"description"`
	// The Lambda environment's configuration settings. Fields documented below.
	Environment *FunctionEnvironment `pulumi:"environment"`
	// The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
	Handler string `pulumi:"handler"`
	// Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to encrypt environment variables. If this configuration is not provided when environment variables are in use, AWS Lambda uses a default service key. If this configuration is provided when environment variables are not in use, the AWS Lambda API does not save this configuration and this provider will show a perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.
	KmsKeyArn *string `pulumi:"kmsKeyArn"`
	// List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
	Layers []string `pulumi:"layers"`
	// Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	MemorySize *int `pulumi:"memorySize"`
	// A unique name for your Lambda Function.
	Name *string `pulumi:"name"`
	// Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
	Publish *bool `pulumi:"publish"`
	// The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
	ReservedConcurrentExecutions *int `pulumi:"reservedConcurrentExecutions"`
	// IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
	Role string `pulumi:"role"`
	// See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
	Runtime string `pulumi:"runtime"`
	// The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
	S3Bucket *string `pulumi:"s3Bucket"`
	// The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
	S3Key *string `pulumi:"s3Key"`
	// The object version containing the function's deployment package. Conflicts with `filename`.
	S3ObjectVersion *string `pulumi:"s3ObjectVersion"`
	// Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3Key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
	SourceCodeHash *string `pulumi:"sourceCodeHash"`
	// A mapping of tags to assign to the object.
	Tags map[string]interface{} `pulumi:"tags"`
	// The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	Timeout       *int                   `pulumi:"timeout"`
	TracingConfig *FunctionTracingConfig `pulumi:"tracingConfig"`
	// Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
	VpcConfig *FunctionVpcConfig `pulumi:"vpcConfig"`
}

// The set of arguments for constructing a Function resource.
type FunctionArgs struct {
	// The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.
	Code pulumi.ArchiveInput
	// Nested block to configure the function's *dead letter queue*. See details below.
	DeadLetterConfig FunctionDeadLetterConfigPtrInput
	// Description of what your Lambda Function does.
	Description pulumi.StringPtrInput
	// The Lambda environment's configuration settings. Fields documented below.
	Environment FunctionEnvironmentPtrInput
	// The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
	Handler pulumi.StringInput
	// Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to encrypt environment variables. If this configuration is not provided when environment variables are in use, AWS Lambda uses a default service key. If this configuration is provided when environment variables are not in use, the AWS Lambda API does not save this configuration and this provider will show a perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.
	KmsKeyArn pulumi.StringPtrInput
	// List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
	Layers pulumi.StringArrayInput
	// Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	MemorySize pulumi.IntPtrInput
	// A unique name for your Lambda Function.
	Name pulumi.StringPtrInput
	// Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
	Publish pulumi.BoolPtrInput
	// The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
	ReservedConcurrentExecutions pulumi.IntPtrInput
	// IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
	Role pulumi.StringInput
	// See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
	Runtime pulumi.StringInput
	// The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.
	S3Bucket pulumi.StringPtrInput
	// The S3 key of an object containing the function's deployment package. Conflicts with `filename`.
	S3Key pulumi.StringPtrInput
	// The object version containing the function's deployment package. Conflicts with `filename`.
	S3ObjectVersion pulumi.StringPtrInput
	// Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3Key`. The usual way to set this is `filebase64sha256("file.zip")` (this provider 0.11.12 and later) or `base64sha256(file("file.zip"))` (this provider 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.
	SourceCodeHash pulumi.StringPtrInput
	// A mapping of tags to assign to the object.
	Tags pulumi.MapInput
	// The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
	Timeout       pulumi.IntPtrInput
	TracingConfig FunctionTracingConfigPtrInput
	// Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
	VpcConfig FunctionVpcConfigPtrInput
}

func (FunctionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*functionArgs)(nil)).Elem()
}
