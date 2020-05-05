# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SnapshotCreateVolumePermission(pulumi.CustomResource):
    account_id: pulumi.Output[str]
    """
    An AWS Account ID to add create volume permissions
    """
    snapshot_id: pulumi.Output[str]
    """
    A snapshot ID
    """
    def __init__(__self__, resource_name, opts=None, account_id=None, snapshot_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Adds permission to create volumes off of a given EBS Snapshot.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ebs.Volume("example",
            availability_zone="us-west-2a",
            size=40)
        example_snapshot = aws.ebs.Snapshot("exampleSnapshot", volume_id=example.id)
        example_perm = aws.ec2.SnapshotCreateVolumePermission("examplePerm",
            account_id="12345678",
            snapshot_id=example_snapshot.id)
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: An AWS Account ID to add create volume permissions
        :param pulumi.Input[str] snapshot_id: A snapshot ID
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

            if account_id is None:
                raise TypeError("Missing required property 'account_id'")
            __props__['account_id'] = account_id
            if snapshot_id is None:
                raise TypeError("Missing required property 'snapshot_id'")
            __props__['snapshot_id'] = snapshot_id
        super(SnapshotCreateVolumePermission, __self__).__init__(
            'aws:ec2/snapshotCreateVolumePermission:SnapshotCreateVolumePermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, account_id=None, snapshot_id=None):
        """
        Get an existing SnapshotCreateVolumePermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: An AWS Account ID to add create volume permissions
        :param pulumi.Input[str] snapshot_id: A snapshot ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["snapshot_id"] = snapshot_id
        return SnapshotCreateVolumePermission(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

