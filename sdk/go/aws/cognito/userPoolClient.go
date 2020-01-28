// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cognito

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Cognito User Pool Client resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cognito_user_pool_client.html.markdown.
type UserPoolClient struct {
	s *pulumi.ResourceState
}

// NewUserPoolClient registers a new resource with the given unique name, arguments, and options.
func NewUserPoolClient(ctx *pulumi.Context,
	name string, args *UserPoolClientArgs, opts ...pulumi.ResourceOpt) (*UserPoolClient, error) {
	if args == nil || args.UserPoolId == nil {
		return nil, errors.New("missing required argument 'UserPoolId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["allowedOauthFlows"] = nil
		inputs["allowedOauthFlowsUserPoolClient"] = nil
		inputs["allowedOauthScopes"] = nil
		inputs["callbackUrls"] = nil
		inputs["defaultRedirectUri"] = nil
		inputs["explicitAuthFlows"] = nil
		inputs["generateSecret"] = nil
		inputs["logoutUrls"] = nil
		inputs["name"] = nil
		inputs["readAttributes"] = nil
		inputs["refreshTokenValidity"] = nil
		inputs["supportedIdentityProviders"] = nil
		inputs["userPoolId"] = nil
		inputs["writeAttributes"] = nil
	} else {
		inputs["allowedOauthFlows"] = args.AllowedOauthFlows
		inputs["allowedOauthFlowsUserPoolClient"] = args.AllowedOauthFlowsUserPoolClient
		inputs["allowedOauthScopes"] = args.AllowedOauthScopes
		inputs["callbackUrls"] = args.CallbackUrls
		inputs["defaultRedirectUri"] = args.DefaultRedirectUri
		inputs["explicitAuthFlows"] = args.ExplicitAuthFlows
		inputs["generateSecret"] = args.GenerateSecret
		inputs["logoutUrls"] = args.LogoutUrls
		inputs["name"] = args.Name
		inputs["readAttributes"] = args.ReadAttributes
		inputs["refreshTokenValidity"] = args.RefreshTokenValidity
		inputs["supportedIdentityProviders"] = args.SupportedIdentityProviders
		inputs["userPoolId"] = args.UserPoolId
		inputs["writeAttributes"] = args.WriteAttributes
	}
	inputs["clientSecret"] = nil
	s, err := ctx.RegisterResource("aws:cognito/userPoolClient:UserPoolClient", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPoolClient{s: s}, nil
}

// GetUserPoolClient gets an existing UserPoolClient resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPoolClient(ctx *pulumi.Context,
	name string, id pulumi.ID, state *UserPoolClientState, opts ...pulumi.ResourceOpt) (*UserPoolClient, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allowedOauthFlows"] = state.AllowedOauthFlows
		inputs["allowedOauthFlowsUserPoolClient"] = state.AllowedOauthFlowsUserPoolClient
		inputs["allowedOauthScopes"] = state.AllowedOauthScopes
		inputs["callbackUrls"] = state.CallbackUrls
		inputs["clientSecret"] = state.ClientSecret
		inputs["defaultRedirectUri"] = state.DefaultRedirectUri
		inputs["explicitAuthFlows"] = state.ExplicitAuthFlows
		inputs["generateSecret"] = state.GenerateSecret
		inputs["logoutUrls"] = state.LogoutUrls
		inputs["name"] = state.Name
		inputs["readAttributes"] = state.ReadAttributes
		inputs["refreshTokenValidity"] = state.RefreshTokenValidity
		inputs["supportedIdentityProviders"] = state.SupportedIdentityProviders
		inputs["userPoolId"] = state.UserPoolId
		inputs["writeAttributes"] = state.WriteAttributes
	}
	s, err := ctx.ReadResource("aws:cognito/userPoolClient:UserPoolClient", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPoolClient{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *UserPoolClient) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *UserPoolClient) ID() pulumi.IDOutput {
	return r.s.ID()
}

// List of allowed OAuth flows (code, implicit, client_credentials).
func (r *UserPoolClient) AllowedOauthFlows() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["allowedOauthFlows"])
}

// Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
func (r *UserPoolClient) AllowedOauthFlowsUserPoolClient() pulumi.BoolOutput {
	return (pulumi.BoolOutput)(r.s.State["allowedOauthFlowsUserPoolClient"])
}

// List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
func (r *UserPoolClient) AllowedOauthScopes() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["allowedOauthScopes"])
}

// List of allowed callback URLs for the identity providers.
func (r *UserPoolClient) CallbackUrls() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["callbackUrls"])
}

// The client secret of the user pool client.
func (r *UserPoolClient) ClientSecret() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["clientSecret"])
}

// The default redirect URI. Must be in the list of callback URLs.
func (r *UserPoolClient) DefaultRedirectUri() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["defaultRedirectUri"])
}

// List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
func (r *UserPoolClient) ExplicitAuthFlows() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["explicitAuthFlows"])
}

// Should an application secret be generated.
func (r *UserPoolClient) GenerateSecret() pulumi.BoolOutput {
	return (pulumi.BoolOutput)(r.s.State["generateSecret"])
}

// List of allowed logout URLs for the identity providers.
func (r *UserPoolClient) LogoutUrls() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["logoutUrls"])
}

// The name of the application client.
func (r *UserPoolClient) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// List of user pool attributes the application client can read from.
func (r *UserPoolClient) ReadAttributes() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["readAttributes"])
}

// The time limit in days refresh tokens are valid for.
func (r *UserPoolClient) RefreshTokenValidity() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["refreshTokenValidity"])
}

// List of provider names for the identity providers that are supported on this client.
func (r *UserPoolClient) SupportedIdentityProviders() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["supportedIdentityProviders"])
}

// The user pool the client belongs to.
func (r *UserPoolClient) UserPoolId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["userPoolId"])
}

// List of user pool attributes the application client can write to.
func (r *UserPoolClient) WriteAttributes() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["writeAttributes"])
}

// Input properties used for looking up and filtering UserPoolClient resources.
type UserPoolClientState struct {
	// List of allowed OAuth flows (code, implicit, client_credentials).
	AllowedOauthFlows interface{}
	// Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
	AllowedOauthFlowsUserPoolClient interface{}
	// List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
	AllowedOauthScopes interface{}
	// List of allowed callback URLs for the identity providers.
	CallbackUrls interface{}
	// The client secret of the user pool client.
	ClientSecret interface{}
	// The default redirect URI. Must be in the list of callback URLs.
	DefaultRedirectUri interface{}
	// List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
	ExplicitAuthFlows interface{}
	// Should an application secret be generated.
	GenerateSecret interface{}
	// List of allowed logout URLs for the identity providers.
	LogoutUrls interface{}
	// The name of the application client.
	Name interface{}
	// List of user pool attributes the application client can read from.
	ReadAttributes interface{}
	// The time limit in days refresh tokens are valid for.
	RefreshTokenValidity interface{}
	// List of provider names for the identity providers that are supported on this client.
	SupportedIdentityProviders interface{}
	// The user pool the client belongs to.
	UserPoolId interface{}
	// List of user pool attributes the application client can write to.
	WriteAttributes interface{}
}

// The set of arguments for constructing a UserPoolClient resource.
type UserPoolClientArgs struct {
	// List of allowed OAuth flows (code, implicit, client_credentials).
	AllowedOauthFlows interface{}
	// Whether the client is allowed to follow the OAuth protocol when interacting with Cognito user pools.
	AllowedOauthFlowsUserPoolClient interface{}
	// List of allowed OAuth scopes (phone, email, openid, profile, and aws.cognito.signin.user.admin).
	AllowedOauthScopes interface{}
	// List of allowed callback URLs for the identity providers.
	CallbackUrls interface{}
	// The default redirect URI. Must be in the list of callback URLs.
	DefaultRedirectUri interface{}
	// List of authentication flows (ADMIN_NO_SRP_AUTH, CUSTOM_AUTH_FLOW_ONLY,  USER_PASSWORD_AUTH, ALLOW_ADMIN_USER_PASSWORD_AUTH, ALLOW_CUSTOM_AUTH, ALLOW_USER_PASSWORD_AUTH, ALLOW_USER_SRP_AUTH, ALLOW_REFRESH_TOKEN_AUTH).
	ExplicitAuthFlows interface{}
	// Should an application secret be generated.
	GenerateSecret interface{}
	// List of allowed logout URLs for the identity providers.
	LogoutUrls interface{}
	// The name of the application client.
	Name interface{}
	// List of user pool attributes the application client can read from.
	ReadAttributes interface{}
	// The time limit in days refresh tokens are valid for.
	RefreshTokenValidity interface{}
	// List of provider names for the identity providers that are supported on this client.
	SupportedIdentityProviders interface{}
	// The user pool the client belongs to.
	UserPoolId interface{}
	// List of user pool attributes the application client can write to.
	WriteAttributes interface{}
}
