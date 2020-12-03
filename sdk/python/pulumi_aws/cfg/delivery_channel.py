# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['DeliveryChannel']


class DeliveryChannel(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 s3_bucket_name: Optional[pulumi.Input[str]] = None,
                 s3_key_prefix: Optional[pulumi.Input[str]] = None,
                 snapshot_delivery_properties: Optional[pulumi.Input[pulumi.InputType['DeliveryChannelSnapshotDeliveryPropertiesArgs']]] = None,
                 sns_topic_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an AWS Config Delivery Channel.

        > **Note:** Delivery Channel requires a `Configuration Recorder` to be present. Use of `depends_on` (as shown below) is recommended to avoid race conditions.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bucket = aws.s3.Bucket("bucket", force_destroy=True)
        role = aws.iam.Role("role", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "config.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }
        \"\"\")
        foo_recorder = aws.cfg.Recorder("fooRecorder", role_arn=role.arn)
        foo_delivery_channel = aws.cfg.DeliveryChannel("fooDeliveryChannel", s3_bucket_name=bucket.bucket,
        opts=pulumi.ResourceOptions(depends_on=[foo_recorder]))
        role_policy = aws.iam.RolePolicy("rolePolicy",
            role=role.id,
            policy=pulumi.Output.all(bucket.arn, bucket.arn).apply(lambda bucketArn, bucketArn1: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Action": [
                "s3:*"
              ],
              "Effect": "Allow",
              "Resource": [
                "{bucket_arn}",
                "{bucket_arn1}/*"
              ]
            }}
          ]
        }}
        \"\"\"))
        ```

        ## Import

        Delivery Channel can be imported using the name, e.g.

        ```sh
         $ pulumi import aws:cfg/deliveryChannel:DeliveryChannel foo example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
        :param pulumi.Input[str] s3_bucket_name: The name of the S3 bucket used to store the configuration history.
        :param pulumi.Input[str] s3_key_prefix: The prefix for the specified S3 bucket.
        :param pulumi.Input[pulumi.InputType['DeliveryChannelSnapshotDeliveryPropertiesArgs']] snapshot_delivery_properties: Options for how AWS Config delivers configuration snapshots. See below
        :param pulumi.Input[str] sns_topic_arn: The ARN of the SNS topic that AWS Config delivers notifications to.
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

            __props__['name'] = name
            if s3_bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 's3_bucket_name'")
            __props__['s3_bucket_name'] = s3_bucket_name
            __props__['s3_key_prefix'] = s3_key_prefix
            __props__['snapshot_delivery_properties'] = snapshot_delivery_properties
            __props__['sns_topic_arn'] = sns_topic_arn
        super(DeliveryChannel, __self__).__init__(
            'aws:cfg/deliveryChannel:DeliveryChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            s3_bucket_name: Optional[pulumi.Input[str]] = None,
            s3_key_prefix: Optional[pulumi.Input[str]] = None,
            snapshot_delivery_properties: Optional[pulumi.Input[pulumi.InputType['DeliveryChannelSnapshotDeliveryPropertiesArgs']]] = None,
            sns_topic_arn: Optional[pulumi.Input[str]] = None) -> 'DeliveryChannel':
        """
        Get an existing DeliveryChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
        :param pulumi.Input[str] s3_bucket_name: The name of the S3 bucket used to store the configuration history.
        :param pulumi.Input[str] s3_key_prefix: The prefix for the specified S3 bucket.
        :param pulumi.Input[pulumi.InputType['DeliveryChannelSnapshotDeliveryPropertiesArgs']] snapshot_delivery_properties: Options for how AWS Config delivers configuration snapshots. See below
        :param pulumi.Input[str] sns_topic_arn: The ARN of the SNS topic that AWS Config delivers notifications to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["name"] = name
        __props__["s3_bucket_name"] = s3_bucket_name
        __props__["s3_key_prefix"] = s3_key_prefix
        __props__["snapshot_delivery_properties"] = snapshot_delivery_properties
        __props__["sns_topic_arn"] = sns_topic_arn
        return DeliveryChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the delivery channel. Defaults to `default`. Changing it recreates the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Output[str]:
        """
        The name of the S3 bucket used to store the configuration history.
        """
        return pulumi.get(self, "s3_bucket_name")

    @property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The prefix for the specified S3 bucket.
        """
        return pulumi.get(self, "s3_key_prefix")

    @property
    @pulumi.getter(name="snapshotDeliveryProperties")
    def snapshot_delivery_properties(self) -> pulumi.Output[Optional['outputs.DeliveryChannelSnapshotDeliveryProperties']]:
        """
        Options for how AWS Config delivers configuration snapshots. See below
        """
        return pulumi.get(self, "snapshot_delivery_properties")

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of the SNS topic that AWS Config delivers notifications to.
        """
        return pulumi.get(self, "sns_topic_arn")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

