# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Webhook(pulumi.CustomResource):
    """
    Provides a CodePipeline Webhook.
    """
    def __init__(__self__, __name__, __opts__=None, authentication=None, authentication_configuration=None, filters=None, name=None, target_action=None, target_pipeline=None):
        """Create a Webhook resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not authentication:
            raise TypeError('Missing required property authentication')
        __props__['authentication'] = authentication

        __props__['authenticationConfiguration'] = authentication_configuration

        if not filters:
            raise TypeError('Missing required property filters')
        __props__['filters'] = filters

        __props__['name'] = name

        if not target_action:
            raise TypeError('Missing required property target_action')
        __props__['targetAction'] = target_action

        if not target_pipeline:
            raise TypeError('Missing required property target_pipeline')
        __props__['targetPipeline'] = target_pipeline

        __props__['url'] = None

        super(Webhook, __self__).__init__(
            'aws:codepipeline/webhook:Webhook',
            __name__,
            __props__,
            __opts__)
