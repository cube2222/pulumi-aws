// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ## Import
//
// DB proxy default target groups can be imported using the `db_proxy_name`, e.g.
//
// ```sh
//  $ pulumi import aws:rds/proxyDefaultTargetGroup:ProxyDefaultTargetGroup example example
// ```
type ProxyDefaultTargetGroup struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) representing the target group.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The settings that determine the size and behavior of the connection pool for the target group.
	ConnectionPoolConfig ProxyDefaultTargetGroupConnectionPoolConfigOutput `pulumi:"connectionPoolConfig"`
	// Name of the RDS DB Proxy.
	DbProxyName pulumi.StringOutput `pulumi:"dbProxyName"`
	// The name of the default target group.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewProxyDefaultTargetGroup registers a new resource with the given unique name, arguments, and options.
func NewProxyDefaultTargetGroup(ctx *pulumi.Context,
	name string, args *ProxyDefaultTargetGroupArgs, opts ...pulumi.ResourceOption) (*ProxyDefaultTargetGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DbProxyName == nil {
		return nil, errors.New("invalid value for required argument 'DbProxyName'")
	}
	var resource ProxyDefaultTargetGroup
	err := ctx.RegisterResource("aws:rds/proxyDefaultTargetGroup:ProxyDefaultTargetGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProxyDefaultTargetGroup gets an existing ProxyDefaultTargetGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProxyDefaultTargetGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProxyDefaultTargetGroupState, opts ...pulumi.ResourceOption) (*ProxyDefaultTargetGroup, error) {
	var resource ProxyDefaultTargetGroup
	err := ctx.ReadResource("aws:rds/proxyDefaultTargetGroup:ProxyDefaultTargetGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ProxyDefaultTargetGroup resources.
type proxyDefaultTargetGroupState struct {
	// The Amazon Resource Name (ARN) representing the target group.
	Arn *string `pulumi:"arn"`
	// The settings that determine the size and behavior of the connection pool for the target group.
	ConnectionPoolConfig *ProxyDefaultTargetGroupConnectionPoolConfig `pulumi:"connectionPoolConfig"`
	// Name of the RDS DB Proxy.
	DbProxyName *string `pulumi:"dbProxyName"`
	// The name of the default target group.
	Name *string `pulumi:"name"`
}

type ProxyDefaultTargetGroupState struct {
	// The Amazon Resource Name (ARN) representing the target group.
	Arn pulumi.StringPtrInput
	// The settings that determine the size and behavior of the connection pool for the target group.
	ConnectionPoolConfig ProxyDefaultTargetGroupConnectionPoolConfigPtrInput
	// Name of the RDS DB Proxy.
	DbProxyName pulumi.StringPtrInput
	// The name of the default target group.
	Name pulumi.StringPtrInput
}

func (ProxyDefaultTargetGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*proxyDefaultTargetGroupState)(nil)).Elem()
}

type proxyDefaultTargetGroupArgs struct {
	// The settings that determine the size and behavior of the connection pool for the target group.
	ConnectionPoolConfig *ProxyDefaultTargetGroupConnectionPoolConfig `pulumi:"connectionPoolConfig"`
	// Name of the RDS DB Proxy.
	DbProxyName string `pulumi:"dbProxyName"`
}

// The set of arguments for constructing a ProxyDefaultTargetGroup resource.
type ProxyDefaultTargetGroupArgs struct {
	// The settings that determine the size and behavior of the connection pool for the target group.
	ConnectionPoolConfig ProxyDefaultTargetGroupConnectionPoolConfigPtrInput
	// Name of the RDS DB Proxy.
	DbProxyName pulumi.StringInput
}

func (ProxyDefaultTargetGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*proxyDefaultTargetGroupArgs)(nil)).Elem()
}

type ProxyDefaultTargetGroupInput interface {
	pulumi.Input

	ToProxyDefaultTargetGroupOutput() ProxyDefaultTargetGroupOutput
	ToProxyDefaultTargetGroupOutputWithContext(ctx context.Context) ProxyDefaultTargetGroupOutput
}

func (*ProxyDefaultTargetGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*ProxyDefaultTargetGroup)(nil))
}

func (i *ProxyDefaultTargetGroup) ToProxyDefaultTargetGroupOutput() ProxyDefaultTargetGroupOutput {
	return i.ToProxyDefaultTargetGroupOutputWithContext(context.Background())
}

func (i *ProxyDefaultTargetGroup) ToProxyDefaultTargetGroupOutputWithContext(ctx context.Context) ProxyDefaultTargetGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProxyDefaultTargetGroupOutput)
}

type ProxyDefaultTargetGroupOutput struct {
	*pulumi.OutputState
}

func (ProxyDefaultTargetGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProxyDefaultTargetGroup)(nil))
}

func (o ProxyDefaultTargetGroupOutput) ToProxyDefaultTargetGroupOutput() ProxyDefaultTargetGroupOutput {
	return o
}

func (o ProxyDefaultTargetGroupOutput) ToProxyDefaultTargetGroupOutputWithContext(ctx context.Context) ProxyDefaultTargetGroupOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ProxyDefaultTargetGroupOutput{})
}
