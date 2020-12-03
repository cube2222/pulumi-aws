# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Authorizer']


class Authorizer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizer_credentials: Optional[pulumi.Input[str]] = None,
                 authorizer_result_ttl_in_seconds: Optional[pulumi.Input[int]] = None,
                 authorizer_uri: Optional[pulumi.Input[str]] = None,
                 identity_source: Optional[pulumi.Input[str]] = None,
                 identity_validation_expression: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rest_api: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an API Gateway Authorizer.

        ## Import

        AWS API Gateway Authorizer can be imported using the `REST-API-ID/AUTHORIZER-ID`, e.g.

        ```sh
         $ pulumi import aws:apigateway/authorizer:Authorizer authorizer 12345abcde/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorizer_credentials: The credentials required for the authorizer. To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
        :param pulumi.Input[int] authorizer_result_ttl_in_seconds: The TTL of cached authorizer results in seconds. Defaults to `300`.
        :param pulumi.Input[str] authorizer_uri: The authorizer's Uniform Resource Identifier (URI). This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
               e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
        :param pulumi.Input[str] identity_source: The source of the identity in an incoming request. Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`
        :param pulumi.Input[str] identity_validation_expression: A validation expression for the incoming identity. For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched against this expression, and will proceed if the token matches. If the token doesn't match, the client receives a 401 Unauthorized response.
        :param pulumi.Input[str] name: The name of the authorizer
        :param pulumi.Input[Sequence[pulumi.Input[str]]] provider_arns: A list of the Amazon Cognito user pool ARNs. Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] type: The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool. Defaults to `TOKEN`.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['authorizer_credentials'] = authorizer_credentials
            __props__['authorizer_result_ttl_in_seconds'] = authorizer_result_ttl_in_seconds
            __props__['authorizer_uri'] = authorizer_uri
            __props__['identity_source'] = identity_source
            __props__['identity_validation_expression'] = identity_validation_expression
            __props__['name'] = name
            __props__['provider_arns'] = provider_arns
            if rest_api is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api'")
            __props__['rest_api'] = rest_api
            __props__['type'] = type
        super(Authorizer, __self__).__init__(
            'aws:apigateway/authorizer:Authorizer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorizer_credentials: Optional[pulumi.Input[str]] = None,
            authorizer_result_ttl_in_seconds: Optional[pulumi.Input[int]] = None,
            authorizer_uri: Optional[pulumi.Input[str]] = None,
            identity_source: Optional[pulumi.Input[str]] = None,
            identity_validation_expression: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            provider_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            rest_api: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Authorizer':
        """
        Get an existing Authorizer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorizer_credentials: The credentials required for the authorizer. To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
        :param pulumi.Input[int] authorizer_result_ttl_in_seconds: The TTL of cached authorizer results in seconds. Defaults to `300`.
        :param pulumi.Input[str] authorizer_uri: The authorizer's Uniform Resource Identifier (URI). This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
               e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
        :param pulumi.Input[str] identity_source: The source of the identity in an incoming request. Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`
        :param pulumi.Input[str] identity_validation_expression: A validation expression for the incoming identity. For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched against this expression, and will proceed if the token matches. If the token doesn't match, the client receives a 401 Unauthorized response.
        :param pulumi.Input[str] name: The name of the authorizer
        :param pulumi.Input[Sequence[pulumi.Input[str]]] provider_arns: A list of the Amazon Cognito user pool ARNs. Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] type: The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool. Defaults to `TOKEN`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authorizer_credentials"] = authorizer_credentials
        __props__["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        __props__["authorizer_uri"] = authorizer_uri
        __props__["identity_source"] = identity_source
        __props__["identity_validation_expression"] = identity_validation_expression
        __props__["name"] = name
        __props__["provider_arns"] = provider_arns
        __props__["rest_api"] = rest_api
        __props__["type"] = type
        return Authorizer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizerCredentials")
    def authorizer_credentials(self) -> pulumi.Output[Optional[str]]:
        """
        The credentials required for the authorizer. To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
        """
        return pulumi.get(self, "authorizer_credentials")

    @property
    @pulumi.getter(name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The TTL of cached authorizer results in seconds. Defaults to `300`.
        """
        return pulumi.get(self, "authorizer_result_ttl_in_seconds")

    @property
    @pulumi.getter(name="authorizerUri")
    def authorizer_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The authorizer's Uniform Resource Identifier (URI). This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
        e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
        """
        return pulumi.get(self, "authorizer_uri")

    @property
    @pulumi.getter(name="identitySource")
    def identity_source(self) -> pulumi.Output[Optional[str]]:
        """
        The source of the identity in an incoming request. Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`
        """
        return pulumi.get(self, "identity_source")

    @property
    @pulumi.getter(name="identityValidationExpression")
    def identity_validation_expression(self) -> pulumi.Output[Optional[str]]:
        """
        A validation expression for the incoming identity. For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched against this expression, and will proceed if the token matches. If the token doesn't match, the client receives a 401 Unauthorized response.
        """
        return pulumi.get(self, "identity_validation_expression")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the authorizer
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerArns")
    def provider_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of the Amazon Cognito user pool ARNs. Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
        """
        return pulumi.get(self, "provider_arns")

    @property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[str]:
        """
        The ID of the associated REST API
        """
        return pulumi.get(self, "rest_api")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool. Defaults to `TOKEN`.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

