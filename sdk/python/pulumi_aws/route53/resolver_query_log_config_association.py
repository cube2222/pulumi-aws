# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ResolverQueryLogConfigAssociation']


class ResolverQueryLogConfigAssociation(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Route 53 Resolver query logging configuration association resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53.ResolverQueryLogConfigAssociation("example",
            resolver_query_log_config_id=aws_route53_resolver_query_log_config["example"]["id"],
            resource_id=aws_vpc["example"]["id"])
        ```

        ## Import

         Route 53 Resolver query logging configuration associations can be imported using the Route 53 Resolver query logging configuration association ID, e.g.

        ```sh
         $ pulumi import aws:route53/resolverQueryLogConfigAssociation:ResolverQueryLogConfigAssociation example rqlca-b320624fef3c4d70
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resolver_query_log_config_id: The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        :param pulumi.Input[str] resource_id: The ID of a VPC that you want this query logging configuration to log queries for.
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

            if resolver_query_log_config_id is None and not opts.urn:
                raise TypeError("Missing required property 'resolver_query_log_config_id'")
            __props__['resolver_query_log_config_id'] = resolver_query_log_config_id
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__['resource_id'] = resource_id
        super(ResolverQueryLogConfigAssociation, __self__).__init__(
            'aws:route53/resolverQueryLogConfigAssociation:ResolverQueryLogConfigAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None) -> 'ResolverQueryLogConfigAssociation':
        """
        Get an existing ResolverQueryLogConfigAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resolver_query_log_config_id: The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        :param pulumi.Input[str] resource_id: The ID of a VPC that you want this query logging configuration to log queries for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["resolver_query_log_config_id"] = resolver_query_log_config_id
        __props__["resource_id"] = resource_id
        return ResolverQueryLogConfigAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> pulumi.Output[str]:
        """
        The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        """
        return pulumi.get(self, "resolver_query_log_config_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of a VPC that you want this query logging configuration to log queries for.
        """
        return pulumi.get(self, "resource_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

