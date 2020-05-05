# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Grant(pulumi.CustomResource):
    constraints: pulumi.Output[list]
    """
    A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).

      * `encryptionContextEquals` (`dict`) - A list of key-value pairs that must match the encryption context in subsequent cryptographic operation requests. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint. Conflicts with `encryption_context_subset`.
      * `encryptionContextSubset` (`dict`) - A list of key-value pairs that must be included in the encryption context of subsequent cryptographic operation requests. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs. Conflicts with `encryption_context_equals`.
    """
    grant_creation_tokens: pulumi.Output[list]
    """
    A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
    """
    grant_id: pulumi.Output[str]
    """
    The unique identifier for the grant.
    """
    grant_token: pulumi.Output[str]
    """
    The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
    """
    grantee_principal: pulumi.Output[str]
    """
    The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
    """
    key_id: pulumi.Output[str]
    """
    The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
    """
    name: pulumi.Output[str]
    """
    A friendly name for identifying the grant.
    """
    operations: pulumi.Output[list]
    """
    A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`
    """
    retire_on_delete: pulumi.Output[bool]
    """
    -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
    See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
    """
    retiring_principal: pulumi.Output[str]
    """
    The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
    """
    def __init__(__self__, resource_name, opts=None, constraints=None, grant_creation_tokens=None, grantee_principal=None, key_id=None, name=None, operations=None, retire_on_delete=None, retiring_principal=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource-based access control mechanism for a KMS customer master key.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.kms.Key("key")
        role = aws.iam.Role("role", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "lambda.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        grant = aws.kms.Grant("grant",
            constraints=[{
                "encryptionContextEquals": {
                    "Department": "Finance",
                },
            }],
            grantee_principal=role.arn,
            key_id=key.key_id,
            operations=[
                "Encrypt",
                "Decrypt",
                "GenerateDataKey",
            ])
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[list] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[list] operations: A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`
        :param pulumi.Input[bool] retire_on_delete: -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.

        The **constraints** object supports the following:

          * `encryptionContextEquals` (`pulumi.Input[dict]`) - A list of key-value pairs that must match the encryption context in subsequent cryptographic operation requests. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint. Conflicts with `encryption_context_subset`.
          * `encryptionContextSubset` (`pulumi.Input[dict]`) - A list of key-value pairs that must be included in the encryption context of subsequent cryptographic operation requests. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs. Conflicts with `encryption_context_equals`.
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

            __props__['constraints'] = constraints
            __props__['grant_creation_tokens'] = grant_creation_tokens
            if grantee_principal is None:
                raise TypeError("Missing required property 'grantee_principal'")
            __props__['grantee_principal'] = grantee_principal
            if key_id is None:
                raise TypeError("Missing required property 'key_id'")
            __props__['key_id'] = key_id
            __props__['name'] = name
            if operations is None:
                raise TypeError("Missing required property 'operations'")
            __props__['operations'] = operations
            __props__['retire_on_delete'] = retire_on_delete
            __props__['retiring_principal'] = retiring_principal
            __props__['grant_id'] = None
            __props__['grant_token'] = None
        super(Grant, __self__).__init__(
            'aws:kms/grant:Grant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, constraints=None, grant_creation_tokens=None, grant_id=None, grant_token=None, grantee_principal=None, key_id=None, name=None, operations=None, retire_on_delete=None, retiring_principal=None):
        """
        Get an existing Grant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[list] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grant_id: The unique identifier for the grant.
        :param pulumi.Input[str] grant_token: The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[list] operations: A list of operations that the grant permits. The permitted values are: `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, ReEncryptFrom, ReEncryptTo, CreateGrant, RetireGrant, DescribeKey`
        :param pulumi.Input[bool] retire_on_delete: -(Defaults to false, Forces new resources) If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the state may not always be refreshed to reflect what is true in AWS.

        The **constraints** object supports the following:

          * `encryptionContextEquals` (`pulumi.Input[dict]`) - A list of key-value pairs that must match the encryption context in subsequent cryptographic operation requests. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint. Conflicts with `encryption_context_subset`.
          * `encryptionContextSubset` (`pulumi.Input[dict]`) - A list of key-value pairs that must be included in the encryption context of subsequent cryptographic operation requests. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs. Conflicts with `encryption_context_equals`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["constraints"] = constraints
        __props__["grant_creation_tokens"] = grant_creation_tokens
        __props__["grant_id"] = grant_id
        __props__["grant_token"] = grant_token
        __props__["grantee_principal"] = grantee_principal
        __props__["key_id"] = key_id
        __props__["name"] = name
        __props__["operations"] = operations
        __props__["retire_on_delete"] = retire_on_delete
        __props__["retiring_principal"] = retiring_principal
        return Grant(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

