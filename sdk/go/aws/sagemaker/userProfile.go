// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Sagemaker User Profile resource.
//
// ## Example Usage
// ### Basic usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/sagemaker"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sagemaker.NewUserProfile(ctx, "example", &sagemaker.UserProfileArgs{
// 			DomainId:        pulumi.Any(aws_sagemaker_domain.Test.Id),
// 			UserProfileName: pulumi.String("example"),
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
// Sagemaker Code User Profiles can be imported using the `arn`, e.g.
//
// ```sh
//  $ pulumi import aws:sagemaker/userProfile:UserProfile test_user_profile arn:aws:sagemaker:us-west-2:123456789012:user-profile/domain-id/profile-name
// ```
type UserProfile struct {
	pulumi.CustomResourceState

	// The user profile Amazon Resource Name (ARN).
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ID of the associated Domain.
	DomainId pulumi.StringOutput `pulumi:"domainId"`
	// The ID of the user's profile in the Amazon Elastic File System (EFS) volume.
	HomeEfsFileSystemUid pulumi.StringOutput `pulumi:"homeEfsFileSystemUid"`
	// A specifier for the type of value specified in `singleSignOnUserValue`. Currently, the only supported value is `UserName`. If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserIdentifier pulumi.StringPtrOutput `pulumi:"singleSignOnUserIdentifier"`
	// The username of the associated AWS Single Sign-On User for this User Profile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserValue pulumi.StringPtrOutput `pulumi:"singleSignOnUserValue"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The name for the User Profile.
	UserProfileName pulumi.StringOutput `pulumi:"userProfileName"`
	// The user settings. See User Settings below.
	UserSettings UserProfileUserSettingsPtrOutput `pulumi:"userSettings"`
}

// NewUserProfile registers a new resource with the given unique name, arguments, and options.
func NewUserProfile(ctx *pulumi.Context,
	name string, args *UserProfileArgs, opts ...pulumi.ResourceOption) (*UserProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DomainId == nil {
		return nil, errors.New("invalid value for required argument 'DomainId'")
	}
	if args.UserProfileName == nil {
		return nil, errors.New("invalid value for required argument 'UserProfileName'")
	}
	var resource UserProfile
	err := ctx.RegisterResource("aws:sagemaker/userProfile:UserProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUserProfile gets an existing UserProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserProfileState, opts ...pulumi.ResourceOption) (*UserProfile, error) {
	var resource UserProfile
	err := ctx.ReadResource("aws:sagemaker/userProfile:UserProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UserProfile resources.
type userProfileState struct {
	// The user profile Amazon Resource Name (ARN).
	Arn *string `pulumi:"arn"`
	// The ID of the associated Domain.
	DomainId *string `pulumi:"domainId"`
	// The ID of the user's profile in the Amazon Elastic File System (EFS) volume.
	HomeEfsFileSystemUid *string `pulumi:"homeEfsFileSystemUid"`
	// A specifier for the type of value specified in `singleSignOnUserValue`. Currently, the only supported value is `UserName`. If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserIdentifier *string `pulumi:"singleSignOnUserIdentifier"`
	// The username of the associated AWS Single Sign-On User for this User Profile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserValue *string `pulumi:"singleSignOnUserValue"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The name for the User Profile.
	UserProfileName *string `pulumi:"userProfileName"`
	// The user settings. See User Settings below.
	UserSettings *UserProfileUserSettings `pulumi:"userSettings"`
}

type UserProfileState struct {
	// The user profile Amazon Resource Name (ARN).
	Arn pulumi.StringPtrInput
	// The ID of the associated Domain.
	DomainId pulumi.StringPtrInput
	// The ID of the user's profile in the Amazon Elastic File System (EFS) volume.
	HomeEfsFileSystemUid pulumi.StringPtrInput
	// A specifier for the type of value specified in `singleSignOnUserValue`. Currently, the only supported value is `UserName`. If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserIdentifier pulumi.StringPtrInput
	// The username of the associated AWS Single Sign-On User for this User Profile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserValue pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The name for the User Profile.
	UserProfileName pulumi.StringPtrInput
	// The user settings. See User Settings below.
	UserSettings UserProfileUserSettingsPtrInput
}

func (UserProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*userProfileState)(nil)).Elem()
}

type userProfileArgs struct {
	// The ID of the associated Domain.
	DomainId string `pulumi:"domainId"`
	// A specifier for the type of value specified in `singleSignOnUserValue`. Currently, the only supported value is `UserName`. If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserIdentifier *string `pulumi:"singleSignOnUserIdentifier"`
	// The username of the associated AWS Single Sign-On User for this User Profile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserValue *string `pulumi:"singleSignOnUserValue"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The name for the User Profile.
	UserProfileName string `pulumi:"userProfileName"`
	// The user settings. See User Settings below.
	UserSettings *UserProfileUserSettings `pulumi:"userSettings"`
}

// The set of arguments for constructing a UserProfile resource.
type UserProfileArgs struct {
	// The ID of the associated Domain.
	DomainId pulumi.StringInput
	// A specifier for the type of value specified in `singleSignOnUserValue`. Currently, the only supported value is `UserName`. If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserIdentifier pulumi.StringPtrInput
	// The username of the associated AWS Single Sign-On User for this User Profile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
	SingleSignOnUserValue pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The name for the User Profile.
	UserProfileName pulumi.StringInput
	// The user settings. See User Settings below.
	UserSettings UserProfileUserSettingsPtrInput
}

func (UserProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userProfileArgs)(nil)).Elem()
}

type UserProfileInput interface {
	pulumi.Input

	ToUserProfileOutput() UserProfileOutput
	ToUserProfileOutputWithContext(ctx context.Context) UserProfileOutput
}

func (*UserProfile) ElementType() reflect.Type {
	return reflect.TypeOf((*UserProfile)(nil))
}

func (i *UserProfile) ToUserProfileOutput() UserProfileOutput {
	return i.ToUserProfileOutputWithContext(context.Background())
}

func (i *UserProfile) ToUserProfileOutputWithContext(ctx context.Context) UserProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserProfileOutput)
}

func (i *UserProfile) ToUserProfilePtrOutput() UserProfilePtrOutput {
	return i.ToUserProfilePtrOutputWithContext(context.Background())
}

func (i *UserProfile) ToUserProfilePtrOutputWithContext(ctx context.Context) UserProfilePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserProfilePtrOutput)
}

type UserProfilePtrInput interface {
	pulumi.Input

	ToUserProfilePtrOutput() UserProfilePtrOutput
	ToUserProfilePtrOutputWithContext(ctx context.Context) UserProfilePtrOutput
}

type userProfilePtrType UserProfileArgs

func (*userProfilePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**UserProfile)(nil))
}

func (i *userProfilePtrType) ToUserProfilePtrOutput() UserProfilePtrOutput {
	return i.ToUserProfilePtrOutputWithContext(context.Background())
}

func (i *userProfilePtrType) ToUserProfilePtrOutputWithContext(ctx context.Context) UserProfilePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserProfilePtrOutput)
}

// UserProfileArrayInput is an input type that accepts UserProfileArray and UserProfileArrayOutput values.
// You can construct a concrete instance of `UserProfileArrayInput` via:
//
//          UserProfileArray{ UserProfileArgs{...} }
type UserProfileArrayInput interface {
	pulumi.Input

	ToUserProfileArrayOutput() UserProfileArrayOutput
	ToUserProfileArrayOutputWithContext(context.Context) UserProfileArrayOutput
}

type UserProfileArray []UserProfileInput

func (UserProfileArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*UserProfile)(nil))
}

func (i UserProfileArray) ToUserProfileArrayOutput() UserProfileArrayOutput {
	return i.ToUserProfileArrayOutputWithContext(context.Background())
}

func (i UserProfileArray) ToUserProfileArrayOutputWithContext(ctx context.Context) UserProfileArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserProfileArrayOutput)
}

// UserProfileMapInput is an input type that accepts UserProfileMap and UserProfileMapOutput values.
// You can construct a concrete instance of `UserProfileMapInput` via:
//
//          UserProfileMap{ "key": UserProfileArgs{...} }
type UserProfileMapInput interface {
	pulumi.Input

	ToUserProfileMapOutput() UserProfileMapOutput
	ToUserProfileMapOutputWithContext(context.Context) UserProfileMapOutput
}

type UserProfileMap map[string]UserProfileInput

func (UserProfileMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*UserProfile)(nil))
}

func (i UserProfileMap) ToUserProfileMapOutput() UserProfileMapOutput {
	return i.ToUserProfileMapOutputWithContext(context.Background())
}

func (i UserProfileMap) ToUserProfileMapOutputWithContext(ctx context.Context) UserProfileMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserProfileMapOutput)
}

type UserProfileOutput struct {
	*pulumi.OutputState
}

func (UserProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UserProfile)(nil))
}

func (o UserProfileOutput) ToUserProfileOutput() UserProfileOutput {
	return o
}

func (o UserProfileOutput) ToUserProfileOutputWithContext(ctx context.Context) UserProfileOutput {
	return o
}

func (o UserProfileOutput) ToUserProfilePtrOutput() UserProfilePtrOutput {
	return o.ToUserProfilePtrOutputWithContext(context.Background())
}

func (o UserProfileOutput) ToUserProfilePtrOutputWithContext(ctx context.Context) UserProfilePtrOutput {
	return o.ApplyT(func(v UserProfile) *UserProfile {
		return &v
	}).(UserProfilePtrOutput)
}

type UserProfilePtrOutput struct {
	*pulumi.OutputState
}

func (UserProfilePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**UserProfile)(nil))
}

func (o UserProfilePtrOutput) ToUserProfilePtrOutput() UserProfilePtrOutput {
	return o
}

func (o UserProfilePtrOutput) ToUserProfilePtrOutputWithContext(ctx context.Context) UserProfilePtrOutput {
	return o
}

type UserProfileArrayOutput struct{ *pulumi.OutputState }

func (UserProfileArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]UserProfile)(nil))
}

func (o UserProfileArrayOutput) ToUserProfileArrayOutput() UserProfileArrayOutput {
	return o
}

func (o UserProfileArrayOutput) ToUserProfileArrayOutputWithContext(ctx context.Context) UserProfileArrayOutput {
	return o
}

func (o UserProfileArrayOutput) Index(i pulumi.IntInput) UserProfileOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) UserProfile {
		return vs[0].([]UserProfile)[vs[1].(int)]
	}).(UserProfileOutput)
}

type UserProfileMapOutput struct{ *pulumi.OutputState }

func (UserProfileMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]UserProfile)(nil))
}

func (o UserProfileMapOutput) ToUserProfileMapOutput() UserProfileMapOutput {
	return o
}

func (o UserProfileMapOutput) ToUserProfileMapOutputWithContext(ctx context.Context) UserProfileMapOutput {
	return o
}

func (o UserProfileMapOutput) MapIndex(k pulumi.StringInput) UserProfileOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) UserProfile {
		return vs[0].(map[string]UserProfile)[vs[1].(string)]
	}).(UserProfileOutput)
}

func init() {
	pulumi.RegisterOutputType(UserProfileOutput{})
	pulumi.RegisterOutputType(UserProfilePtrOutput{})
	pulumi.RegisterOutputType(UserProfileArrayOutput{})
	pulumi.RegisterOutputType(UserProfileMapOutput{})
}
