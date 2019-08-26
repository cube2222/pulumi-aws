# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class InstanceProfile(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN assigned by AWS to the instance profile.
    """
    create_date: pulumi.Output[str]
    """
    The creation timestamp of the instance profile.
    """
    name: pulumi.Output[str]
    """
    The profile's name. If omitted, this provider will assign a random, unique name.
    """
    name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the specified prefix. Conflicts with `name`.
    """
    path: pulumi.Output[str]
    """
    Path in which to create the profile.
    """
    role: pulumi.Output[str]
    """
    The role name to include in the profile.
    """
    roles: pulumi.Output[list]
    """
    
    A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.
    """
    unique_id: pulumi.Output[str]
    """
    The [unique ID][1] assigned by AWS.
    """
    def __init__(__self__, resource_name, opts=None, name=None, name_prefix=None, path=None, role=None, roles=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an IAM instance profile.
        
        > **NOTE:** Either `role` or `roles` (**deprecated**) must be specified.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The profile's name. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] path: Path in which to create the profile.
        :param pulumi.Input[str] role: The role name to include in the profile.
        :param pulumi.Input[list] roles: 
               A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown.
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

            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['path'] = path
            __props__['role'] = role
            __props__['roles'] = roles
            __props__['arn'] = None
            __props__['create_date'] = None
            __props__['unique_id'] = None
        super(InstanceProfile, __self__).__init__(
            'aws:iam/instanceProfile:InstanceProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, create_date=None, name=None, name_prefix=None, path=None, role=None, roles=None, unique_id=None):
        """
        Get an existing InstanceProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN assigned by AWS to the instance profile.
        :param pulumi.Input[str] create_date: The creation timestamp of the instance profile.
        :param pulumi.Input[str] name: The profile's name. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] path: Path in which to create the profile.
        :param pulumi.Input[str] role: The role name to include in the profile.
        :param pulumi.Input[list] roles: 
               A list of role names to include in the profile.  The current default is 1.  If you see an error message similar to `Cannot exceed quota for InstanceSessionsPerInstanceProfile: 1`, then you must contact AWS support and ask for a limit increase.
        :param pulumi.Input[str] unique_id: The [unique ID][1] assigned by AWS.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_instance_profile.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["arn"] = arn
        __props__["create_date"] = create_date
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["path"] = path
        __props__["role"] = role
        __props__["roles"] = roles
        __props__["unique_id"] = unique_id
        return InstanceProfile(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

