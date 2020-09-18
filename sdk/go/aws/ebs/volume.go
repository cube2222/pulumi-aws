// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ebs

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a single EBS volume.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ebs"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ebs.NewVolume(ctx, "example", &ebs.VolumeArgs{
// 			AvailabilityZone: pulumi.String("us-west-2a"),
// 			Size:             pulumi.Int(40),
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("HelloWorld"),
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
// > **NOTE**: One of `size` or `snapshotId` is required when specifying an EBS volume
type Volume struct {
	pulumi.CustomResourceState

	// The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The AZ where the EBS volume will exist.
	AvailabilityZone pulumi.StringOutput `pulumi:"availabilityZone"`
	// If true, the disk will be encrypted.
	Encrypted pulumi.BoolOutput `pulumi:"encrypted"`
	// The amount of IOPS to provision for the disk. Only valid for `type` of `io1` or `io2`.
	Iops pulumi.IntOutput `pulumi:"iops"`
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `encrypted` needs to be set to true.
	KmsKeyId pulumi.StringOutput `pulumi:"kmsKeyId"`
	// Specifies whether to enable Amazon EBS Multi-Attach. Multi-Attach is supported exclusively on `io1` volumes.
	MultiAttachEnabled pulumi.BoolPtrOutput `pulumi:"multiAttachEnabled"`
	// The Amazon Resource Name (ARN) of the Outpost.
	OutpostArn pulumi.StringPtrOutput `pulumi:"outpostArn"`
	// The size of the drive in GiBs.
	Size pulumi.IntOutput `pulumi:"size"`
	// A snapshot to base the EBS volume off of.
	SnapshotId pulumi.StringOutput `pulumi:"snapshotId"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The type of EBS volume. Can be "standard", "gp2", "io1", "io2", "sc1" or "st1" (Default: "gp2").
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOption) (*Volume, error) {
	if args == nil || args.AvailabilityZone == nil {
		return nil, errors.New("missing required argument 'AvailabilityZone'")
	}
	if args == nil {
		args = &VolumeArgs{}
	}
	var resource Volume
	err := ctx.RegisterResource("aws:ebs/volume:Volume", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolume gets an existing Volume resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolume(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeState, opts ...pulumi.ResourceOption) (*Volume, error) {
	var resource Volume
	err := ctx.ReadResource("aws:ebs/volume:Volume", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Volume resources.
type volumeState struct {
	// The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
	Arn *string `pulumi:"arn"`
	// The AZ where the EBS volume will exist.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// If true, the disk will be encrypted.
	Encrypted *bool `pulumi:"encrypted"`
	// The amount of IOPS to provision for the disk. Only valid for `type` of `io1` or `io2`.
	Iops *int `pulumi:"iops"`
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `encrypted` needs to be set to true.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Specifies whether to enable Amazon EBS Multi-Attach. Multi-Attach is supported exclusively on `io1` volumes.
	MultiAttachEnabled *bool `pulumi:"multiAttachEnabled"`
	// The Amazon Resource Name (ARN) of the Outpost.
	OutpostArn *string `pulumi:"outpostArn"`
	// The size of the drive in GiBs.
	Size *int `pulumi:"size"`
	// A snapshot to base the EBS volume off of.
	SnapshotId *string `pulumi:"snapshotId"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The type of EBS volume. Can be "standard", "gp2", "io1", "io2", "sc1" or "st1" (Default: "gp2").
	Type *string `pulumi:"type"`
}

type VolumeState struct {
	// The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
	Arn pulumi.StringPtrInput
	// The AZ where the EBS volume will exist.
	AvailabilityZone pulumi.StringPtrInput
	// If true, the disk will be encrypted.
	Encrypted pulumi.BoolPtrInput
	// The amount of IOPS to provision for the disk. Only valid for `type` of `io1` or `io2`.
	Iops pulumi.IntPtrInput
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `encrypted` needs to be set to true.
	KmsKeyId pulumi.StringPtrInput
	// Specifies whether to enable Amazon EBS Multi-Attach. Multi-Attach is supported exclusively on `io1` volumes.
	MultiAttachEnabled pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) of the Outpost.
	OutpostArn pulumi.StringPtrInput
	// The size of the drive in GiBs.
	Size pulumi.IntPtrInput
	// A snapshot to base the EBS volume off of.
	SnapshotId pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The type of EBS volume. Can be "standard", "gp2", "io1", "io2", "sc1" or "st1" (Default: "gp2").
	Type pulumi.StringPtrInput
}

func (VolumeState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeState)(nil)).Elem()
}

type volumeArgs struct {
	// The AZ where the EBS volume will exist.
	AvailabilityZone string `pulumi:"availabilityZone"`
	// If true, the disk will be encrypted.
	Encrypted *bool `pulumi:"encrypted"`
	// The amount of IOPS to provision for the disk. Only valid for `type` of `io1` or `io2`.
	Iops *int `pulumi:"iops"`
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `encrypted` needs to be set to true.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// Specifies whether to enable Amazon EBS Multi-Attach. Multi-Attach is supported exclusively on `io1` volumes.
	MultiAttachEnabled *bool `pulumi:"multiAttachEnabled"`
	// The Amazon Resource Name (ARN) of the Outpost.
	OutpostArn *string `pulumi:"outpostArn"`
	// The size of the drive in GiBs.
	Size *int `pulumi:"size"`
	// A snapshot to base the EBS volume off of.
	SnapshotId *string `pulumi:"snapshotId"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The type of EBS volume. Can be "standard", "gp2", "io1", "io2", "sc1" or "st1" (Default: "gp2").
	Type *string `pulumi:"type"`
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	// The AZ where the EBS volume will exist.
	AvailabilityZone pulumi.StringInput
	// If true, the disk will be encrypted.
	Encrypted pulumi.BoolPtrInput
	// The amount of IOPS to provision for the disk. Only valid for `type` of `io1` or `io2`.
	Iops pulumi.IntPtrInput
	// The ARN for the KMS encryption key. When specifying `kmsKeyId`, `encrypted` needs to be set to true.
	KmsKeyId pulumi.StringPtrInput
	// Specifies whether to enable Amazon EBS Multi-Attach. Multi-Attach is supported exclusively on `io1` volumes.
	MultiAttachEnabled pulumi.BoolPtrInput
	// The Amazon Resource Name (ARN) of the Outpost.
	OutpostArn pulumi.StringPtrInput
	// The size of the drive in GiBs.
	Size pulumi.IntPtrInput
	// A snapshot to base the EBS volume off of.
	SnapshotId pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The type of EBS volume. Can be "standard", "gp2", "io1", "io2", "sc1" or "st1" (Default: "gp2").
	Type pulumi.StringPtrInput
}

func (VolumeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeArgs)(nil)).Elem()
}
