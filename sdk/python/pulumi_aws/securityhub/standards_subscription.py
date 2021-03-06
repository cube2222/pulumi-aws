# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['StandardsSubscription']


class StandardsSubscription(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 standards_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Subscribes to a Security Hub standard.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.securityhub.Account("example")
        cis = aws.securityhub.StandardsSubscription("cis", standards_arn="arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
        opts=pulumi.ResourceOptions(depends_on=[example]))
        pci321 = aws.securityhub.StandardsSubscription("pci321", standards_arn="arn:aws:securityhub:us-east-1::standards/pci-dss/v/3.2.1",
        opts=pulumi.ResourceOptions(depends_on=[example]))
        ```

        ## Import

        Security Hub standards subscriptions can be imported using the standards subscription ARN, e.g.

        ```sh
         $ pulumi import aws:securityhub/standardsSubscription:StandardsSubscription cis arn:aws:securityhub:eu-west-1:123456789012:subscription/cis-aws-foundations-benchmark/v/1.2.0
        ```

        ```sh
         $ pulumi import aws:securityhub/standardsSubscription:StandardsSubscription pci_321 arn:aws:securityhub:eu-west-1:123456789012:subscription/pci-dss/v/3.2.1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] standards_arn: The ARN of a standard - see below.
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

            if standards_arn is None and not opts.urn:
                raise TypeError("Missing required property 'standards_arn'")
            __props__['standards_arn'] = standards_arn
        super(StandardsSubscription, __self__).__init__(
            'aws:securityhub/standardsSubscription:StandardsSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            standards_arn: Optional[pulumi.Input[str]] = None) -> 'StandardsSubscription':
        """
        Get an existing StandardsSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] standards_arn: The ARN of a standard - see below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["standards_arn"] = standards_arn
        return StandardsSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="standardsArn")
    def standards_arn(self) -> pulumi.Output[str]:
        """
        The ARN of a standard - see below.
        """
        return pulumi.get(self, "standards_arn")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

