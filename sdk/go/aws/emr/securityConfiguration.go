// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package emr

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage AWS EMR Security Configurations
type SecurityConfiguration struct {
	pulumi.CustomResourceState

	// A JSON formatted Security Configuration
	Configuration pulumi.StringOutput `pulumi:"configuration"`
	// Date the Security Configuration was created
	CreationDate pulumi.StringOutput `pulumi:"creationDate"`
	// The name of the EMR Security Configuration. By default generated by this provider.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
}

// NewSecurityConfiguration registers a new resource with the given unique name, arguments, and options.
func NewSecurityConfiguration(ctx *pulumi.Context,
	name string, args *SecurityConfigurationArgs, opts ...pulumi.ResourceOption) (*SecurityConfiguration, error) {
	if args == nil || args.Configuration == nil {
		return nil, errors.New("missing required argument 'Configuration'")
	}
	if args == nil {
		args = &SecurityConfigurationArgs{}
	}
	var resource SecurityConfiguration
	err := ctx.RegisterResource("aws:emr/securityConfiguration:SecurityConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecurityConfiguration gets an existing SecurityConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecurityConfigurationState, opts ...pulumi.ResourceOption) (*SecurityConfiguration, error) {
	var resource SecurityConfiguration
	err := ctx.ReadResource("aws:emr/securityConfiguration:SecurityConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecurityConfiguration resources.
type securityConfigurationState struct {
	// A JSON formatted Security Configuration
	Configuration *string `pulumi:"configuration"`
	// Date the Security Configuration was created
	CreationDate *string `pulumi:"creationDate"`
	// The name of the EMR Security Configuration. By default generated by this provider.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
}

type SecurityConfigurationState struct {
	// A JSON formatted Security Configuration
	Configuration pulumi.StringPtrInput
	// Date the Security Configuration was created
	CreationDate pulumi.StringPtrInput
	// The name of the EMR Security Configuration. By default generated by this provider.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
}

func (SecurityConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*securityConfigurationState)(nil)).Elem()
}

type securityConfigurationArgs struct {
	// A JSON formatted Security Configuration
	Configuration string `pulumi:"configuration"`
	// The name of the EMR Security Configuration. By default generated by this provider.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
}

// The set of arguments for constructing a SecurityConfiguration resource.
type SecurityConfigurationArgs struct {
	// A JSON formatted Security Configuration
	Configuration pulumi.StringInput
	// The name of the EMR Security Configuration. By default generated by this provider.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
}

func (SecurityConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*securityConfigurationArgs)(nil)).Elem()
}
