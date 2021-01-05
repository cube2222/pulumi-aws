// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource for adding an [IAM User](https://www.terraform.io/docs/providers/aws/r/iam_user.html) to [IAM Groups](https://www.terraform.io/docs/providers/aws/r/iam_group.html). This
// resource can be used multiple times with the same user for non-overlapping
// groups.
//
// To exclusively manage the users in a group, see the
// [`iam.GroupMembership` resource][3].
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		user1, err := iam.NewUser(ctx, "user1", nil)
// 		if err != nil {
// 			return err
// 		}
// 		group1, err := iam.NewGroup(ctx, "group1", nil)
// 		if err != nil {
// 			return err
// 		}
// 		group2, err := iam.NewGroup(ctx, "group2", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewUserGroupMembership(ctx, "example1", &iam.UserGroupMembershipArgs{
// 			User: user1.Name,
// 			Groups: pulumi.StringArray{
// 				group1.Name,
// 				group2.Name,
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		group3, err := iam.NewGroup(ctx, "group3", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewUserGroupMembership(ctx, "example2", &iam.UserGroupMembershipArgs{
// 			User: user1.Name,
// 			Groups: pulumi.StringArray{
// 				group3.Name,
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
// ## Import
//
// IAM user group membership can be imported using the user name and group names separated by `/`.
//
// ```sh
//  $ pulumi import aws:iam/userGroupMembership:UserGroupMembership example1 user1/group1/group2
// ```
type UserGroupMembership struct {
	pulumi.CustomResourceState

	// A list of [IAM Groups](https://www.terraform.io/docs/providers/aws/r/iam_group.html) to add the user to
	Groups pulumi.StringArrayOutput `pulumi:"groups"`
	// The name of the [IAM User](https://www.terraform.io/docs/providers/aws/r/iam_user.html) to add to groups
	User pulumi.StringOutput `pulumi:"user"`
}

// NewUserGroupMembership registers a new resource with the given unique name, arguments, and options.
func NewUserGroupMembership(ctx *pulumi.Context,
	name string, args *UserGroupMembershipArgs, opts ...pulumi.ResourceOption) (*UserGroupMembership, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Groups == nil {
		return nil, errors.New("invalid value for required argument 'Groups'")
	}
	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	var resource UserGroupMembership
	err := ctx.RegisterResource("aws:iam/userGroupMembership:UserGroupMembership", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserGroupMembership gets an existing UserGroupMembership resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserGroupMembership(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserGroupMembershipState, opts ...pulumi.ResourceOption) (*UserGroupMembership, error) {
	var resource UserGroupMembership
	err := ctx.ReadResource("aws:iam/userGroupMembership:UserGroupMembership", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserGroupMembership resources.
type userGroupMembershipState struct {
	// A list of [IAM Groups](https://www.terraform.io/docs/providers/aws/r/iam_group.html) to add the user to
	Groups []string `pulumi:"groups"`
	// The name of the [IAM User](https://www.terraform.io/docs/providers/aws/r/iam_user.html) to add to groups
	User *string `pulumi:"user"`
}

type UserGroupMembershipState struct {
	// A list of [IAM Groups](https://www.terraform.io/docs/providers/aws/r/iam_group.html) to add the user to
	Groups pulumi.StringArrayInput
	// The name of the [IAM User](https://www.terraform.io/docs/providers/aws/r/iam_user.html) to add to groups
	User pulumi.StringPtrInput
}

func (UserGroupMembershipState) ElementType() reflect.Type {
	return reflect.TypeOf((*userGroupMembershipState)(nil)).Elem()
}

type userGroupMembershipArgs struct {
	// A list of [IAM Groups](https://www.terraform.io/docs/providers/aws/r/iam_group.html) to add the user to
	Groups []string `pulumi:"groups"`
	// The name of the [IAM User](https://www.terraform.io/docs/providers/aws/r/iam_user.html) to add to groups
	User string `pulumi:"user"`
}

// The set of arguments for constructing a UserGroupMembership resource.
type UserGroupMembershipArgs struct {
	// A list of [IAM Groups](https://www.terraform.io/docs/providers/aws/r/iam_group.html) to add the user to
	Groups pulumi.StringArrayInput
	// The name of the [IAM User](https://www.terraform.io/docs/providers/aws/r/iam_user.html) to add to groups
	User pulumi.StringInput
}

func (UserGroupMembershipArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userGroupMembershipArgs)(nil)).Elem()
}

type UserGroupMembershipInput interface {
	pulumi.Input

	ToUserGroupMembershipOutput() UserGroupMembershipOutput
	ToUserGroupMembershipOutputWithContext(ctx context.Context) UserGroupMembershipOutput
}

func (*UserGroupMembership) ElementType() reflect.Type {
	return reflect.TypeOf((*UserGroupMembership)(nil))
}

func (i *UserGroupMembership) ToUserGroupMembershipOutput() UserGroupMembershipOutput {
	return i.ToUserGroupMembershipOutputWithContext(context.Background())
}

func (i *UserGroupMembership) ToUserGroupMembershipOutputWithContext(ctx context.Context) UserGroupMembershipOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserGroupMembershipOutput)
}

type UserGroupMembershipOutput struct {
	*pulumi.OutputState
}

func (UserGroupMembershipOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserGroupMembership)(nil))
}

func (o UserGroupMembershipOutput) ToUserGroupMembershipOutput() UserGroupMembershipOutput {
	return o
}

func (o UserGroupMembershipOutput) ToUserGroupMembershipOutputWithContext(ctx context.Context) UserGroupMembershipOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UserGroupMembershipOutput{})
}
