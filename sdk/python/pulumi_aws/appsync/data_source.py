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

__all__ = ['DataSource']


class DataSource(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dynamodb_config: Optional[pulumi.Input[pulumi.InputType['DataSourceDynamodbConfigArgs']]] = None,
                 elasticsearch_config: Optional[pulumi.Input[pulumi.InputType['DataSourceElasticsearchConfigArgs']]] = None,
                 http_config: Optional[pulumi.Input[pulumi.InputType['DataSourceHttpConfigArgs']]] = None,
                 lambda_config: Optional[pulumi.Input[pulumi.InputType['DataSourceLambdaConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an AppSync DataSource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_table = aws.dynamodb.Table("exampleTable",
            read_capacity=1,
            write_capacity=1,
            hash_key="UserId",
            attributes=[aws.dynamodb.TableAttributeArgs(
                name="UserId",
                type="S",
            )])
        example_role = aws.iam.Role("exampleRole", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "appsync.amazonaws.com"
              },
              "Effect": "Allow"
            }
          ]
        }
        \"\"\")
        example_role_policy = aws.iam.RolePolicy("exampleRolePolicy",
            role=example_role.id,
            policy=example_table.arn.apply(lambda arn: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Action": [
                "dynamodb:*"
              ],
              "Effect": "Allow",
              "Resource": [
                "{arn}"
              ]
            }}
          ]
        }}
        \"\"\"))
        example_graph_ql_api = aws.appsync.GraphQLApi("exampleGraphQLApi", authentication_type="API_KEY")
        example_data_source = aws.appsync.DataSource("exampleDataSource",
            api_id=example_graph_ql_api.id,
            name="tf_appsync_example",
            service_role_arn=example_role.arn,
            type="AMAZON_DYNAMODB",
            dynamodb_config=aws.appsync.DataSourceDynamodbConfigArgs(
                table_name=example_table.name,
            ))
        ```

        ## Import

        `aws_appsync_datasource` can be imported with their `api_id`, a hyphen, and `name`, e.g.

        ```sh
         $ pulumi import aws:appsync/dataSource:DataSource example abcdef123456-example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API ID for the GraphQL API for the DataSource.
        :param pulumi.Input[str] description: A description of the DataSource.
        :param pulumi.Input[pulumi.InputType['DataSourceDynamodbConfigArgs']] dynamodb_config: DynamoDB settings. See below
        :param pulumi.Input[pulumi.InputType['DataSourceElasticsearchConfigArgs']] elasticsearch_config: Amazon Elasticsearch settings. See below
        :param pulumi.Input[pulumi.InputType['DataSourceHttpConfigArgs']] http_config: HTTP settings. See below
        :param pulumi.Input[pulumi.InputType['DataSourceLambdaConfigArgs']] lambda_config: AWS Lambda settings. See below
        :param pulumi.Input[str] name: A user-supplied name for the DataSource.
        :param pulumi.Input[str] service_role_arn: The IAM service role ARN for the data source.
        :param pulumi.Input[str] type: The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['description'] = description
            __props__['dynamodb_config'] = dynamodb_config
            __props__['elasticsearch_config'] = elasticsearch_config
            __props__['http_config'] = http_config
            __props__['lambda_config'] = lambda_config
            __props__['name'] = name
            __props__['service_role_arn'] = service_role_arn
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['arn'] = None
        super(DataSource, __self__).__init__(
            'aws:appsync/dataSource:DataSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dynamodb_config: Optional[pulumi.Input[pulumi.InputType['DataSourceDynamodbConfigArgs']]] = None,
            elasticsearch_config: Optional[pulumi.Input[pulumi.InputType['DataSourceElasticsearchConfigArgs']]] = None,
            http_config: Optional[pulumi.Input[pulumi.InputType['DataSourceHttpConfigArgs']]] = None,
            lambda_config: Optional[pulumi.Input[pulumi.InputType['DataSourceLambdaConfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            service_role_arn: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'DataSource':
        """
        Get an existing DataSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API ID for the GraphQL API for the DataSource.
        :param pulumi.Input[str] arn: The ARN
        :param pulumi.Input[str] description: A description of the DataSource.
        :param pulumi.Input[pulumi.InputType['DataSourceDynamodbConfigArgs']] dynamodb_config: DynamoDB settings. See below
        :param pulumi.Input[pulumi.InputType['DataSourceElasticsearchConfigArgs']] elasticsearch_config: Amazon Elasticsearch settings. See below
        :param pulumi.Input[pulumi.InputType['DataSourceHttpConfigArgs']] http_config: HTTP settings. See below
        :param pulumi.Input[pulumi.InputType['DataSourceLambdaConfigArgs']] lambda_config: AWS Lambda settings. See below
        :param pulumi.Input[str] name: A user-supplied name for the DataSource.
        :param pulumi.Input[str] service_role_arn: The IAM service role ARN for the data source.
        :param pulumi.Input[str] type: The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["dynamodb_config"] = dynamodb_config
        __props__["elasticsearch_config"] = elasticsearch_config
        __props__["http_config"] = http_config
        __props__["lambda_config"] = lambda_config
        __props__["name"] = name
        __props__["service_role_arn"] = service_role_arn
        __props__["type"] = type
        return DataSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API ID for the GraphQL API for the DataSource.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the DataSource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dynamodbConfig")
    def dynamodb_config(self) -> pulumi.Output[Optional['outputs.DataSourceDynamodbConfig']]:
        """
        DynamoDB settings. See below
        """
        return pulumi.get(self, "dynamodb_config")

    @property
    @pulumi.getter(name="elasticsearchConfig")
    def elasticsearch_config(self) -> pulumi.Output[Optional['outputs.DataSourceElasticsearchConfig']]:
        """
        Amazon Elasticsearch settings. See below
        """
        return pulumi.get(self, "elasticsearch_config")

    @property
    @pulumi.getter(name="httpConfig")
    def http_config(self) -> pulumi.Output[Optional['outputs.DataSourceHttpConfig']]:
        """
        HTTP settings. See below
        """
        return pulumi.get(self, "http_config")

    @property
    @pulumi.getter(name="lambdaConfig")
    def lambda_config(self) -> pulumi.Output[Optional['outputs.DataSourceLambdaConfig']]:
        """
        AWS Lambda settings. See below
        """
        return pulumi.get(self, "lambda_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-supplied name for the DataSource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The IAM service role ARN for the data source.
        """
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

