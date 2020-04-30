# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class RoleAssociation(pulumi.CustomResource):
    db_instance_identifier: pulumi.Output[str]
    """
    DB Instance Identifier to associate with the IAM Role.
    """
    feature_name: pulumi.Output[str]
    """
    Name of the feature for association. This can be found in the AWS documentation relevant to the integration or a full list is available in the `SupportedFeatureNames` list returned by [AWS CLI rds describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html).
    """
    role_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the IAM Role to associate with the DB Instance.
    """
    def __init__(__self__, resource_name, opts=None, db_instance_identifier=None, feature_name=None, role_arn=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a RDS DB Instance association with an IAM Role. Example use cases:

        * [Amazon RDS Oracle integration with Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html)
        * [Importing Amazon S3 Data into an RDS PostgreSQL DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.html)

        > To manage the RDS DB Instance IAM Role for [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html), see the `rds.Instance` resource `monitoring_role_arn` argument instead.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.rds.RoleAssociation("example",
            db_instance_identifier=aws_db_instance["example"]["id"],
            feature_name="S3_INTEGRATION",
            role_arn=aws_iam_role["example"]["id"])
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_instance_identifier: DB Instance Identifier to associate with the IAM Role.
        :param pulumi.Input[str] feature_name: Name of the feature for association. This can be found in the AWS documentation relevant to the integration or a full list is available in the `SupportedFeatureNames` list returned by [AWS CLI rds describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html).
        :param pulumi.Input[str] role_arn: Amazon Resource Name (ARN) of the IAM Role to associate with the DB Instance.
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

            if db_instance_identifier is None:
                raise TypeError("Missing required property 'db_instance_identifier'")
            __props__['db_instance_identifier'] = db_instance_identifier
            if feature_name is None:
                raise TypeError("Missing required property 'feature_name'")
            __props__['feature_name'] = feature_name
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
        super(RoleAssociation, __self__).__init__(
            'aws:rds/roleAssociation:RoleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, db_instance_identifier=None, feature_name=None, role_arn=None):
        """
        Get an existing RoleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_instance_identifier: DB Instance Identifier to associate with the IAM Role.
        :param pulumi.Input[str] feature_name: Name of the feature for association. This can be found in the AWS documentation relevant to the integration or a full list is available in the `SupportedFeatureNames` list returned by [AWS CLI rds describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html).
        :param pulumi.Input[str] role_arn: Amazon Resource Name (ARN) of the IAM Role to associate with the DB Instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["db_instance_identifier"] = db_instance_identifier
        __props__["feature_name"] = feature_name
        __props__["role_arn"] = role_arn
        return RoleAssociation(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

