// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Creates a snapshot copy grant that allows AWS Redshift to encrypt copied snapshots with a customer master key from AWS KMS in a destination region.
// 
// Note that the grant must exist in the destination region, and not in the region of the cluster.
type SnapshotCopyGrant struct {
	s *pulumi.ResourceState
}

// NewSnapshotCopyGrant registers a new resource with the given unique name, arguments, and options.
func NewSnapshotCopyGrant(ctx *pulumi.Context,
	name string, args *SnapshotCopyGrantArgs, opts ...pulumi.ResourceOpt) (*SnapshotCopyGrant, error) {
	if args == nil || args.SnapshotCopyGrantName == nil {
		return nil, errors.New("missing required argument 'SnapshotCopyGrantName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["kmsKeyId"] = nil
		inputs["snapshotCopyGrantName"] = nil
		inputs["tags"] = nil
	} else {
		inputs["kmsKeyId"] = args.KmsKeyId
		inputs["snapshotCopyGrantName"] = args.SnapshotCopyGrantName
		inputs["tags"] = args.Tags
	}
	s, err := ctx.RegisterResource("aws:redshift/snapshotCopyGrant:SnapshotCopyGrant", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SnapshotCopyGrant{s: s}, nil
}

// GetSnapshotCopyGrant gets an existing SnapshotCopyGrant resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshotCopyGrant(ctx *pulumi.Context,
	name string, id pulumi.ID, state *SnapshotCopyGrantState, opts ...pulumi.ResourceOpt) (*SnapshotCopyGrant, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["kmsKeyId"] = state.KmsKeyId
		inputs["snapshotCopyGrantName"] = state.SnapshotCopyGrantName
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:redshift/snapshotCopyGrant:SnapshotCopyGrant", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &SnapshotCopyGrant{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *SnapshotCopyGrant) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *SnapshotCopyGrant) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
func (r *SnapshotCopyGrant) KmsKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["kmsKeyId"])
}

// A friendly name for identifying the grant.
func (r *SnapshotCopyGrant) SnapshotCopyGrantName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["snapshotCopyGrantName"])
}

func (r *SnapshotCopyGrant) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering SnapshotCopyGrant resources.
type SnapshotCopyGrantState struct {
	// The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
	KmsKeyId interface{}
	// A friendly name for identifying the grant.
	SnapshotCopyGrantName interface{}
	Tags interface{}
}

// The set of arguments for constructing a SnapshotCopyGrant resource.
type SnapshotCopyGrantArgs struct {
	// The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
	KmsKeyId interface{}
	// A friendly name for identifying the grant.
	SnapshotCopyGrantName interface{}
	Tags interface{}
}
