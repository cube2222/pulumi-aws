# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, id=None, secrets=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if secrets and not isinstance(secrets, list):
            raise TypeError("Expected argument 'secrets' to be a list")
        __self__.secrets = secrets
class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            id=self.id,
            secrets=self.secrets)

def get_secret(secrets=None,opts=None):
    """
    !> **WARNING:** This data source was removed in version 2.0.0 of the AWS Provider. You can migrate existing configurations to the [`kms.getSecrets` data source](https://www.terraform.io/docs/providers/aws/d/kms_secrets.html) following instructions available in the [Version 2 Upgrade Guide](https://www.terraform.io/docs/providers/aws/guides/version-2-upgrade.html#data-source-aws_kms_secret).



    The **secrets** object supports the following:

      * `context` (`dict`)
      * `grantTokens` (`list`)
      * `name` (`str`)
      * `payload` (`str`)
    """
    __args__ = dict()


    __args__['secrets'] = secrets
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kms/getSecret:getSecret', __args__, opts=opts).value

    return AwaitableGetSecretResult(
        id=__ret__.get('id'),
        secrets=__ret__.get('secrets'))
