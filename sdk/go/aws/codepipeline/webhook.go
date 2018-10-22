// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codepipeline

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a CodePipeline Webhook.
type Webhook struct {
	s *pulumi.ResourceState
}

// NewWebhook registers a new resource with the given unique name, arguments, and options.
func NewWebhook(ctx *pulumi.Context,
	name string, args *WebhookArgs, opts ...pulumi.ResourceOpt) (*Webhook, error) {
	if args == nil || args.Authentication == nil {
		return nil, errors.New("missing required argument 'Authentication'")
	}
	if args == nil || args.Filters == nil {
		return nil, errors.New("missing required argument 'Filters'")
	}
	if args == nil || args.TargetAction == nil {
		return nil, errors.New("missing required argument 'TargetAction'")
	}
	if args == nil || args.TargetPipeline == nil {
		return nil, errors.New("missing required argument 'TargetPipeline'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["authentication"] = nil
		inputs["authenticationConfiguration"] = nil
		inputs["filters"] = nil
		inputs["name"] = nil
		inputs["targetAction"] = nil
		inputs["targetPipeline"] = nil
	} else {
		inputs["authentication"] = args.Authentication
		inputs["authenticationConfiguration"] = args.AuthenticationConfiguration
		inputs["filters"] = args.Filters
		inputs["name"] = args.Name
		inputs["targetAction"] = args.TargetAction
		inputs["targetPipeline"] = args.TargetPipeline
	}
	inputs["url"] = nil
	s, err := ctx.RegisterResource("aws:codepipeline/webhook:Webhook", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Webhook{s: s}, nil
}

// GetWebhook gets an existing Webhook resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWebhook(ctx *pulumi.Context,
	name string, id pulumi.ID, state *WebhookState, opts ...pulumi.ResourceOpt) (*Webhook, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["authentication"] = state.Authentication
		inputs["authenticationConfiguration"] = state.AuthenticationConfiguration
		inputs["filters"] = state.Filters
		inputs["name"] = state.Name
		inputs["targetAction"] = state.TargetAction
		inputs["targetPipeline"] = state.TargetPipeline
		inputs["url"] = state.Url
	}
	s, err := ctx.ReadResource("aws:codepipeline/webhook:Webhook", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Webhook{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Webhook) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Webhook) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
func (r *Webhook) Authentication() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["authentication"])
}

// An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
func (r *Webhook) AuthenticationConfiguration() *pulumi.Output {
	return r.s.State["authenticationConfiguration"]
}

// One or more `filter` blocks. Filter blocks are documented below.
func (r *Webhook) Filters() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["filters"])
}

// The name of the webhook.
func (r *Webhook) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
func (r *Webhook) TargetAction() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["targetAction"])
}

// The name of the pipeline.
func (r *Webhook) TargetPipeline() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["targetPipeline"])
}

// The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.
func (r *Webhook) Url() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["url"])
}

// Input properties used for looking up and filtering Webhook resources.
type WebhookState struct {
	// The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
	Authentication interface{}
	// An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
	AuthenticationConfiguration interface{}
	// One or more `filter` blocks. Filter blocks are documented below.
	Filters interface{}
	// The name of the webhook.
	Name interface{}
	// The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
	TargetAction interface{}
	// The name of the pipeline.
	TargetPipeline interface{}
	// The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.
	Url interface{}
}

// The set of arguments for constructing a Webhook resource.
type WebhookArgs struct {
	// The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
	Authentication interface{}
	// An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
	AuthenticationConfiguration interface{}
	// One or more `filter` blocks. Filter blocks are documented below.
	Filters interface{}
	// The name of the webhook.
	Name interface{}
	// The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
	TargetAction interface{}
	// The name of the pipeline.
	TargetPipeline interface{}
}
