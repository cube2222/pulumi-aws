// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storagegateway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages an AWS Storage Gateway cache.
//
// > **NOTE:** The Storage Gateway API provides no method to remove a cache disk. Destroying this resource does not perform any Storage Gateway actions.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/storagegateway"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := storagegateway.NewCache(ctx, "example", &storagegateway.CacheArgs{
// 			DiskId:     pulumi.Any(data.Aws_storagegateway_local_disk.Example.Id),
// 			GatewayArn: pulumi.Any(aws_storagegateway_gateway.Example.Arn),
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
// `aws_storagegateway_cache` can be imported by using the gateway Amazon Resource Name (ARN) and local disk identifier separated with a colon (`:`), e.g.
//
// ```sh
//  $ pulumi import aws:storagegateway/cache:Cache example arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678:pci-0000:03:00.0-scsi-0:0:0:0
// ```
type Cache struct {
	pulumi.CustomResourceState

	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId pulumi.StringOutput `pulumi:"diskId"`
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn pulumi.StringOutput `pulumi:"gatewayArn"`
}

// NewCache registers a new resource with the given unique name, arguments, and options.
func NewCache(ctx *pulumi.Context,
	name string, args *CacheArgs, opts ...pulumi.ResourceOption) (*Cache, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DiskId == nil {
		return nil, errors.New("invalid value for required argument 'DiskId'")
	}
	if args.GatewayArn == nil {
		return nil, errors.New("invalid value for required argument 'GatewayArn'")
	}
	var resource Cache
	err := ctx.RegisterResource("aws:storagegateway/cache:Cache", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCache gets an existing Cache resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCache(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CacheState, opts ...pulumi.ResourceOption) (*Cache, error) {
	var resource Cache
	err := ctx.ReadResource("aws:storagegateway/cache:Cache", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cache resources.
type cacheState struct {
	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId *string `pulumi:"diskId"`
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn *string `pulumi:"gatewayArn"`
}

type CacheState struct {
	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId pulumi.StringPtrInput
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn pulumi.StringPtrInput
}

func (CacheState) ElementType() reflect.Type {
	return reflect.TypeOf((*cacheState)(nil)).Elem()
}

type cacheArgs struct {
	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId string `pulumi:"diskId"`
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn string `pulumi:"gatewayArn"`
}

// The set of arguments for constructing a Cache resource.
type CacheArgs struct {
	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId pulumi.StringInput
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn pulumi.StringInput
}

func (CacheArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cacheArgs)(nil)).Elem()
}

type CacheInput interface {
	pulumi.Input

	ToCacheOutput() CacheOutput
	ToCacheOutputWithContext(ctx context.Context) CacheOutput
}

func (*Cache) ElementType() reflect.Type {
	return reflect.TypeOf((*Cache)(nil))
}

func (i *Cache) ToCacheOutput() CacheOutput {
	return i.ToCacheOutputWithContext(context.Background())
}

func (i *Cache) ToCacheOutputWithContext(ctx context.Context) CacheOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CacheOutput)
}

type CacheOutput struct {
	*pulumi.OutputState
}

func (CacheOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Cache)(nil))
}

func (o CacheOutput) ToCacheOutput() CacheOutput {
	return o
}

func (o CacheOutput) ToCacheOutputWithContext(ctx context.Context) CacheOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CacheOutput{})
}
