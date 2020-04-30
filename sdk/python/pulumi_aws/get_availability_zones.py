# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetAvailabilityZonesResult:
    """
    A collection of values returned by getAvailabilityZones.
    """
    def __init__(__self__, all_availability_zones=None, blacklisted_names=None, blacklisted_zone_ids=None, filters=None, group_names=None, id=None, names=None, state=None, zone_ids=None):
        if all_availability_zones and not isinstance(all_availability_zones, bool):
            raise TypeError("Expected argument 'all_availability_zones' to be a bool")
        __self__.all_availability_zones = all_availability_zones
        if blacklisted_names and not isinstance(blacklisted_names, list):
            raise TypeError("Expected argument 'blacklisted_names' to be a list")
        __self__.blacklisted_names = blacklisted_names
        if blacklisted_zone_ids and not isinstance(blacklisted_zone_ids, list):
            raise TypeError("Expected argument 'blacklisted_zone_ids' to be a list")
        __self__.blacklisted_zone_ids = blacklisted_zone_ids
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if group_names and not isinstance(group_names, list):
            raise TypeError("Expected argument 'group_names' to be a list")
        __self__.group_names = group_names
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of the Availability Zone names available to the account.
        """
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        __self__.state = state
        if zone_ids and not isinstance(zone_ids, list):
            raise TypeError("Expected argument 'zone_ids' to be a list")
        __self__.zone_ids = zone_ids
        """
        A list of the Availability Zone IDs available to the account.
        """
class AwaitableGetAvailabilityZonesResult(GetAvailabilityZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailabilityZonesResult(
            all_availability_zones=self.all_availability_zones,
            blacklisted_names=self.blacklisted_names,
            blacklisted_zone_ids=self.blacklisted_zone_ids,
            filters=self.filters,
            group_names=self.group_names,
            id=self.id,
            names=self.names,
            state=self.state,
            zone_ids=self.zone_ids)

def get_availability_zones(all_availability_zones=None,blacklisted_names=None,blacklisted_zone_ids=None,filters=None,group_names=None,state=None,opts=None):
    """
    The Availability Zones data source allows access to the list of AWS
    Availability Zones which can be accessed by an AWS account within the region
    configured in the provider.

    This is different from the `.getAvailabilityZone` (singular) data source,
    which provides some details about a specific availability zone.

    > When [Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) are enabled in a region, by default the API and this data source include both Local Zones and Availability Zones. To return only Availability Zones, see the example section below.

    ## Example Usage

    ### By State

    ```python
    import pulumi
    import pulumi_aws as aws

    available = aws.get_availability_zones(state="available")
    primary = aws.ec2.Subnet("primary", availability_zone=available.names[0])
    # ...
    secondary = aws.ec2.Subnet("secondary", availability_zone=available.names[1])
    # ...
    ```



    :param bool all_availability_zones: Set to `true` to include all Availability Zones and Local Zones regardless of your opt in status.
    :param list blacklisted_names: List of blacklisted Availability Zone names.
    :param list blacklisted_zone_ids: List of blacklisted Availability Zone IDs.
    :param list filters: Configuration block(s) for filtering. Detailed below.
    :param str state: Allows to filter list of Availability Zones based on their
           current state. Can be either `"available"`, `"information"`, `"impaired"` or
           `"unavailable"`. By default the list includes a complete set of Availability Zones
           to which the underlying AWS account has access, regardless of their state.

    The **filters** object supports the following:

      * `name` (`str`) - The name of the filter field. Valid values can be found in the [EC2 DescribeAvailabilityZones API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html).
      * `values` (`list`) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
    """
    __args__ = dict()


    __args__['allAvailabilityZones'] = all_availability_zones
    __args__['blacklistedNames'] = blacklisted_names
    __args__['blacklistedZoneIds'] = blacklisted_zone_ids
    __args__['filters'] = filters
    __args__['groupNames'] = group_names
    __args__['state'] = state
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getAvailabilityZones:getAvailabilityZones', __args__, opts=opts).value

    return AwaitableGetAvailabilityZonesResult(
        all_availability_zones=__ret__.get('allAvailabilityZones'),
        blacklisted_names=__ret__.get('blacklistedNames'),
        blacklisted_zone_ids=__ret__.get('blacklistedZoneIds'),
        filters=__ret__.get('filters'),
        group_names=__ret__.get('groupNames'),
        id=__ret__.get('id'),
        names=__ret__.get('names'),
        state=__ret__.get('state'),
        zone_ids=__ret__.get('zoneIds'))
