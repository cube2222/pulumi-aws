// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an IAM policy attached to a user.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		lbUser, err := iam.NewUser(ctx, "lbUser", &iam.UserArgs{
// 			Path: pulumi.String("/system/"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewUserPolicy(ctx, "lbRo", &iam.UserPolicyArgs{
// 			User:   lbUser.Name,
// 			Policy: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v", "{\n", "  \"Version\": \"2012-10-17\",\n", "  \"Statement\": [\n", "    {\n", "      \"Action\": [\n", "        \"ec2:Describe*\"\n", "      ],\n", "      \"Effect\": \"Allow\",\n", "      \"Resource\": \"*\"\n", "    }\n", "  ]\n", "}\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewAccessKey(ctx, "lbAccessKey", &iam.AccessKeyArgs{
// 			User: lbUser.Name,
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
// IAM User Policies can be imported using the `user_name:user_policy_name`, e.g.
//
// ```sh
//  $ pulumi import aws:iam/userPolicy:UserPolicy mypolicy user_of_mypolicy_name:mypolicy_name
// ```
type UserPolicy struct {
	pulumi.CustomResourceState

	// The name of the policy. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// The policy document. This is a JSON formatted string.
	Policy pulumi.StringOutput `pulumi:"policy"`
	// IAM user to which to attach this policy.
	User pulumi.StringOutput `pulumi:"user"`
}

// NewUserPolicy registers a new resource with the given unique name, arguments, and options.
func NewUserPolicy(ctx *pulumi.Context,
	name string, args *UserPolicyArgs, opts ...pulumi.ResourceOption) (*UserPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	var resource UserPolicy
	err := ctx.RegisterResource("aws:iam/userPolicy:UserPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserPolicy gets an existing UserPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserPolicyState, opts ...pulumi.ResourceOption) (*UserPolicy, error) {
	var resource UserPolicy
	err := ctx.ReadResource("aws:iam/userPolicy:UserPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserPolicy resources.
type userPolicyState struct {
	// The name of the policy. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The policy document. This is a JSON formatted string.
	Policy *string `pulumi:"policy"`
	// IAM user to which to attach this policy.
	User *string `pulumi:"user"`
}

type UserPolicyState struct {
	// The name of the policy. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The policy document. This is a JSON formatted string.
	Policy pulumi.StringPtrInput
	// IAM user to which to attach this policy.
	User pulumi.StringPtrInput
}

func (UserPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*userPolicyState)(nil)).Elem()
}

type userPolicyArgs struct {
	// The name of the policy. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The policy document. This is a JSON formatted string.
	Policy interface{} `pulumi:"policy"`
	// IAM user to which to attach this policy.
	User string `pulumi:"user"`
}

// The set of arguments for constructing a UserPolicy resource.
type UserPolicyArgs struct {
	// The name of the policy. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The policy document. This is a JSON formatted string.
	Policy pulumi.Input
	// IAM user to which to attach this policy.
	User pulumi.StringInput
}

func (UserPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userPolicyArgs)(nil)).Elem()
}

type UserPolicyInput interface {
	pulumi.Input

	ToUserPolicyOutput() UserPolicyOutput
	ToUserPolicyOutputWithContext(ctx context.Context) UserPolicyOutput
}

func (UserPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*UserPolicy)(nil)).Elem()
}

func (i UserPolicy) ToUserPolicyOutput() UserPolicyOutput {
	return i.ToUserPolicyOutputWithContext(context.Background())
}

func (i UserPolicy) ToUserPolicyOutputWithContext(ctx context.Context) UserPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserPolicyOutput)
}

type UserPolicyOutput struct {
	*pulumi.OutputState
}

func (UserPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserPolicyOutput)(nil)).Elem()
}

func (o UserPolicyOutput) ToUserPolicyOutput() UserPolicyOutput {
	return o
}

func (o UserPolicyOutput) ToUserPolicyOutputWithContext(ctx context.Context) UserPolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UserPolicyOutput{})
}
