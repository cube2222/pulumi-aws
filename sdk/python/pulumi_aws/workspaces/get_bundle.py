# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetBundleResult(object):
    """
    A collection of values returned by getBundle.
    """
    def __init__(__self__, compute_types=None, description=None, name=None, owner=None, root_storages=None, user_storages=None, id=None):
        if compute_types and not isinstance(compute_types, list):
            raise TypeError('Expected argument compute_types to be a list')
        __self__.compute_types = compute_types
        """
        The compute type. See supported fields below.
        """
        if description and not isinstance(description, basestring):
            raise TypeError('Expected argument description to be a basestring')
        __self__.description = description
        """
        The description of the bundle.
        """
        if name and not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        """
        The name of the compute type.
        """
        if owner and not isinstance(owner, basestring):
            raise TypeError('Expected argument owner to be a basestring')
        __self__.owner = owner
        """
        The owner of the bundle.
        """
        if root_storages and not isinstance(root_storages, list):
            raise TypeError('Expected argument root_storages to be a list')
        __self__.root_storages = root_storages
        """
        The root volume. See supported fields below.
        """
        if user_storages and not isinstance(user_storages, list):
            raise TypeError('Expected argument user_storages to be a list')
        __self__.user_storages = user_storages
        """
        The user storage. See supported fields below.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_bundle(bundle_id=None):
    """
    Use this data source to get information about a Workspaces Bundle.
    """
    __args__ = dict()

    __args__['bundleId'] = bundle_id
    __ret__ = pulumi.runtime.invoke('aws:workspaces/getBundle:getBundle', __args__)

    return GetBundleResult(
        compute_types=__ret__.get('computeTypes'),
        description=__ret__.get('description'),
        name=__ret__.get('name'),
        owner=__ret__.get('owner'),
        root_storages=__ret__.get('rootStorages'),
        user_storages=__ret__.get('userStorages'),
        id=__ret__.get('id'))
