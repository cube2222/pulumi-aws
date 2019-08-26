# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class QueryLog(pulumi.CustomResource):
    cloudwatch_log_group_arn: pulumi.Output[str]
    """
    CloudWatch log group ARN to send query logs.
    """
    zone_id: pulumi.Output[str]
    """
    Route53 hosted zone ID to enable query logs.
    """
    def __init__(__self__, resource_name, opts=None, cloudwatch_log_group_arn=None, zone_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Route53 query logging configuration resource.
        
        > **NOTE:** There are restrictions on the configuration of query logging. Notably,
        the CloudWatch log group must be in the `us-east-1` region,
        a permissive CloudWatch log resource policy must be in place, and
        the Route53 hosted zone must be public.
        See [Configuring Logging for DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring) for additional details.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_log_group_arn: CloudWatch log group ARN to send query logs.
        :param pulumi.Input[str] zone_id: Route53 hosted zone ID to enable query logs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_query_log.html.markdown.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if cloudwatch_log_group_arn is None:
                raise TypeError("Missing required property 'cloudwatch_log_group_arn'")
            __props__['cloudwatch_log_group_arn'] = cloudwatch_log_group_arn
            if zone_id is None:
                raise TypeError("Missing required property 'zone_id'")
            __props__['zone_id'] = zone_id
        super(QueryLog, __self__).__init__(
            'aws:route53/queryLog:QueryLog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cloudwatch_log_group_arn=None, zone_id=None):
        """
        Get an existing QueryLog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_log_group_arn: CloudWatch log group ARN to send query logs.
        :param pulumi.Input[str] zone_id: Route53 hosted zone ID to enable query logs.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_query_log.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["cloudwatch_log_group_arn"] = cloudwatch_log_group_arn
        __props__["zone_id"] = zone_id
        return QueryLog(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

