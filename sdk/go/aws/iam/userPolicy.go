// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an IAM policy attached to a user.
type UserPolicy struct {
	s *pulumi.ResourceState
}

// NewUserPolicy registers a new resource with the given unique name, arguments, and options.
func NewUserPolicy(ctx *pulumi.Context,
	name string, args *UserPolicyArgs, opts ...pulumi.ResourceOpt) (*UserPolicy, error) {
	if args == nil || args.Policy == nil {
		return nil, errors.New("missing required argument 'Policy'")
	}
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["policy"] = nil
		inputs["user"] = nil
	} else {
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["policy"] = args.Policy
		inputs["user"] = args.User
	}
	s, err := ctx.RegisterResource("aws:iam/userPolicy:UserPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPolicy{s: s}, nil
}

// GetUserPolicy gets an existing UserPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *UserPolicyState, opts ...pulumi.ResourceOpt) (*UserPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["policy"] = state.Policy
		inputs["user"] = state.User
	}
	s, err := ctx.ReadResource("aws:iam/userPolicy:UserPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *UserPolicy) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *UserPolicy) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The name of the policy. If omitted, Terraform will assign a random, unique name.
func (r *UserPolicy) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
func (r *UserPolicy) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
func (r *UserPolicy) Policy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["policy"])
}

// IAM user to which to attach this policy.
func (r *UserPolicy) User() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["user"])
}

// Input properties used for looking up and filtering UserPolicy resources.
type UserPolicyState struct {
	// The name of the policy. If omitted, Terraform will assign a random, unique name.
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
	Policy interface{}
	// IAM user to which to attach this policy.
	User interface{}
}

// The set of arguments for constructing a UserPolicy resource.
type UserPolicyArgs struct {
	// The name of the policy. If omitted, Terraform will assign a random, unique name.
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The policy document. This is a JSON formatted string. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).
	Policy interface{}
	// IAM user to which to attach this policy.
	User interface{}
}
