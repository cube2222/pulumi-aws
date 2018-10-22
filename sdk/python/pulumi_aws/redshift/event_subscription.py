# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class EventSubscription(pulumi.CustomResource):
    """
    Provides a Redshift event subscription resource.
    """
    def __init__(__self__, __name__, __opts__=None, enabled=None, event_categories=None, name=None, severity=None, sns_topic_arn=None, source_ids=None, source_type=None, tags=None):
        """Create a EventSubscription resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if enabled and not isinstance(enabled, bool):
            raise TypeError('Expected property enabled to be a bool')
        __self__.enabled = enabled
        """
        A boolean flag to enable/disable the subscription. Defaults to true.
        """
        __props__['enabled'] = enabled

        if event_categories and not isinstance(event_categories, list):
            raise TypeError('Expected property event_categories to be a list')
        __self__.event_categories = event_categories
        """
        A list of event categories for a SourceType that you want to subscribe to. See https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html or run `aws redshift describe-event-categories`.
        """
        __props__['eventCategories'] = event_categories

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the Redshift event subscription.
        """
        __props__['name'] = name

        if severity and not isinstance(severity, basestring):
            raise TypeError('Expected property severity to be a basestring')
        __self__.severity = severity
        """
        The event severity to be published by the notification subscription. Valid options are `INFO` or `ERROR`.
        """
        __props__['severity'] = severity

        if not sns_topic_arn:
            raise TypeError('Missing required property sns_topic_arn')
        elif not isinstance(sns_topic_arn, basestring):
            raise TypeError('Expected property sns_topic_arn to be a basestring')
        __self__.sns_topic_arn = sns_topic_arn
        """
        The ARN of the SNS topic to send events to.
        """
        __props__['snsTopicArn'] = sns_topic_arn

        if source_ids and not isinstance(source_ids, list):
            raise TypeError('Expected property source_ids to be a list')
        __self__.source_ids = source_ids
        """
        A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.
        """
        __props__['sourceIds'] = source_ids

        if source_type and not isinstance(source_type, basestring):
            raise TypeError('Expected property source_type to be a basestring')
        __self__.source_type = source_type
        """
        The type of source that will be generating the events. Valid options are `cluster`, `cluster-parameter-group`, `cluster-security-group`, or `cluster-snapshot`. If not set, all sources will be subscribed to.
        """
        __props__['sourceType'] = source_type

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.customer_aws_id = pulumi.runtime.UNKNOWN
        __self__.status = pulumi.runtime.UNKNOWN

        super(EventSubscription, __self__).__init__(
            'aws:redshift/eventSubscription:EventSubscription',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'customerAwsId' in outs:
            self.customer_aws_id = outs['customerAwsId']
        if 'enabled' in outs:
            self.enabled = outs['enabled']
        if 'eventCategories' in outs:
            self.event_categories = outs['eventCategories']
        if 'name' in outs:
            self.name = outs['name']
        if 'severity' in outs:
            self.severity = outs['severity']
        if 'snsTopicArn' in outs:
            self.sns_topic_arn = outs['snsTopicArn']
        if 'sourceIds' in outs:
            self.source_ids = outs['sourceIds']
        if 'sourceType' in outs:
            self.source_type = outs['sourceType']
        if 'status' in outs:
            self.status = outs['status']
        if 'tags' in outs:
            self.tags = outs['tags']
