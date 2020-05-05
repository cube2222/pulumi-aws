# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ProductSubscription(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
    """
    product_arn: pulumi.Output[str]
    """
    The ARN of the product that generates findings that you want to import into Security Hub - see below.
    """
    def __init__(__self__, resource_name, opts=None, product_arn=None, __props__=None, __name__=None, __opts__=None):
        """
        Subscribes to a Security Hub product.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        example_account = aws.securityhub.Account("exampleAccount")
        current = aws.get_region()
        example_product_subscription = aws.securityhub.ProductSubscription("exampleProductSubscription", product_arn=f"arn:aws:securityhub:{current.name}:733251395267:product/alertlogic/althreatmanagement")
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] product_arn: The ARN of the product that generates findings that you want to import into Security Hub - see below.
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

            if product_arn is None:
                raise TypeError("Missing required property 'product_arn'")
            __props__['product_arn'] = product_arn
            __props__['arn'] = None
        super(ProductSubscription, __self__).__init__(
            'aws:securityhub/productSubscription:ProductSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, product_arn=None):
        """
        Get an existing ProductSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
        :param pulumi.Input[str] product_arn: The ARN of the product that generates findings that you want to import into Security Hub - see below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["product_arn"] = product_arn
        return ProductSubscription(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

