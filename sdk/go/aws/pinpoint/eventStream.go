// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type EventStream struct {
	s *pulumi.ResourceState
}

// NewEventStream registers a new resource with the given unique name, arguments, and options.
func NewEventStream(ctx *pulumi.Context,
	name string, args *EventStreamArgs, opts ...pulumi.ResourceOpt) (*EventStream, error) {
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	if args == nil || args.DestinationStreamArn == nil {
		return nil, errors.New("missing required argument 'DestinationStreamArn'")
	}
	if args == nil || args.RoleArn == nil {
		return nil, errors.New("missing required argument 'RoleArn'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applicationId"] = nil
		inputs["destinationStreamArn"] = nil
		inputs["roleArn"] = nil
	} else {
		inputs["applicationId"] = args.ApplicationId
		inputs["destinationStreamArn"] = args.DestinationStreamArn
		inputs["roleArn"] = args.RoleArn
	}
	s, err := ctx.RegisterResource("aws:pinpoint/eventStream:EventStream", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &EventStream{s: s}, nil
}

// GetEventStream gets an existing EventStream resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventStream(ctx *pulumi.Context,
	name string, id pulumi.ID, state *EventStreamState, opts ...pulumi.ResourceOpt) (*EventStream, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["applicationId"] = state.ApplicationId
		inputs["destinationStreamArn"] = state.DestinationStreamArn
		inputs["roleArn"] = state.RoleArn
	}
	s, err := ctx.ReadResource("aws:pinpoint/eventStream:EventStream", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &EventStream{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *EventStream) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *EventStream) ID() *pulumi.IDOutput {
	return r.s.ID
}

func (r *EventStream) ApplicationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["applicationId"])
}

func (r *EventStream) DestinationStreamArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["destinationStreamArn"])
}

func (r *EventStream) RoleArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["roleArn"])
}

// Input properties used for looking up and filtering EventStream resources.
type EventStreamState struct {
	ApplicationId interface{}
	DestinationStreamArn interface{}
	RoleArn interface{}
}

// The set of arguments for constructing a EventStream resource.
type EventStreamArgs struct {
	ApplicationId interface{}
	DestinationStreamArn interface{}
	RoleArn interface{}
}
