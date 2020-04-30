# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetDirectoryResult:
    """
    A collection of values returned by getDirectory.
    """
    def __init__(__self__, access_url=None, alias=None, connect_settings=None, description=None, directory_id=None, dns_ip_addresses=None, edition=None, enable_sso=None, id=None, name=None, security_group_id=None, short_name=None, size=None, tags=None, type=None, vpc_settings=None):
        if access_url and not isinstance(access_url, str):
            raise TypeError("Expected argument 'access_url' to be a str")
        __self__.access_url = access_url
        """
        The access URL for the directory/connector, such as http://alias.awsapps.com.
        """
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        __self__.alias = alias
        """
        The alias for the directory/connector, such as `d-991708b282.awsapps.com`.
        """
        if connect_settings and not isinstance(connect_settings, list):
            raise TypeError("Expected argument 'connect_settings' to be a list")
        __self__.connect_settings = connect_settings
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        A textual description for the directory/connector.
        """
        if directory_id and not isinstance(directory_id, str):
            raise TypeError("Expected argument 'directory_id' to be a str")
        __self__.directory_id = directory_id
        if dns_ip_addresses and not isinstance(dns_ip_addresses, list):
            raise TypeError("Expected argument 'dns_ip_addresses' to be a list")
        __self__.dns_ip_addresses = dns_ip_addresses
        """
        A list of IP addresses of the DNS servers for the directory/connector.
        """
        if edition and not isinstance(edition, str):
            raise TypeError("Expected argument 'edition' to be a str")
        __self__.edition = edition
        """
        (for `MicrosoftAD`) The Microsoft AD edition (`Standard` or `Enterprise`).
        """
        if enable_sso and not isinstance(enable_sso, bool):
            raise TypeError("Expected argument 'enable_sso' to be a bool")
        __self__.enable_sso = enable_sso
        """
        The directory/connector single-sign on status.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The fully qualified name for the directory/connector.
        """
        if security_group_id and not isinstance(security_group_id, str):
            raise TypeError("Expected argument 'security_group_id' to be a str")
        __self__.security_group_id = security_group_id
        """
        The ID of the security group created by the directory/connector.
        """
        if short_name and not isinstance(short_name, str):
            raise TypeError("Expected argument 'short_name' to be a str")
        __self__.short_name = short_name
        """
        The short name of the directory/connector, such as `CORP`.
        """
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        __self__.size = size
        """
        (for `SimpleAD` and `ADConnector`) The size of the directory/connector (`Small` or `Large`).
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A mapping of tags assigned to the directory/connector.
        """
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        """
        The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD`).
        """
        if vpc_settings and not isinstance(vpc_settings, list):
            raise TypeError("Expected argument 'vpc_settings' to be a list")
        __self__.vpc_settings = vpc_settings
class AwaitableGetDirectoryResult(GetDirectoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDirectoryResult(
            access_url=self.access_url,
            alias=self.alias,
            connect_settings=self.connect_settings,
            description=self.description,
            directory_id=self.directory_id,
            dns_ip_addresses=self.dns_ip_addresses,
            edition=self.edition,
            enable_sso=self.enable_sso,
            id=self.id,
            name=self.name,
            security_group_id=self.security_group_id,
            short_name=self.short_name,
            size=self.size,
            tags=self.tags,
            type=self.type,
            vpc_settings=self.vpc_settings)

def get_directory(directory_id=None,tags=None,opts=None):
    """
    Get attributes of AWS Directory Service directory (SimpleAD, Managed AD, AD Connector). It's especially useful to refer AWS Managed AD or on-premise AD in AD Connector configuration. 




    :param str directory_id: The ID of the directory.
    :param dict tags: A mapping of tags assigned to the directory/connector.
    """
    __args__ = dict()


    __args__['directoryId'] = directory_id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:directoryservice/getDirectory:getDirectory', __args__, opts=opts).value

    return AwaitableGetDirectoryResult(
        access_url=__ret__.get('accessUrl'),
        alias=__ret__.get('alias'),
        connect_settings=__ret__.get('connectSettings'),
        description=__ret__.get('description'),
        directory_id=__ret__.get('directoryId'),
        dns_ip_addresses=__ret__.get('dnsIpAddresses'),
        edition=__ret__.get('edition'),
        enable_sso=__ret__.get('enableSso'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        security_group_id=__ret__.get('securityGroupId'),
        short_name=__ret__.get('shortName'),
        size=__ret__.get('size'),
        tags=__ret__.get('tags'),
        type=__ret__.get('type'),
        vpc_settings=__ret__.get('vpcSettings'))
