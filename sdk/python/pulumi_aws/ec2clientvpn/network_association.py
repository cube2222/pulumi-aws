# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['NetworkAssociation']


class NetworkAssociation(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides network associations for AWS Client VPN endpoints. For more information on usage, please see the
        [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

        ## Example Usage
        ### Using default security group

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2clientvpn.NetworkAssociation("example",
            client_vpn_endpoint_id=aws_ec2_client_vpn_endpoint["example"]["id"],
            subnet_id=aws_subnet["example"]["id"])
        ```
        ### Using custom security groups

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2clientvpn.NetworkAssociation("example",
            client_vpn_endpoint_id=aws_ec2_client_vpn_endpoint["example"]["id"],
            subnet_id=aws_subnet["example"]["id"],
            security_groups=[
                aws_security_group["example1"]["id"],
                aws_security_group["example2"]["id"],
            ])
        ```

        ## Import

        AWS Client VPN network associations can be imported using the endpoint ID and the association ID. Values are separated by a `,`.

        ```sh
         $ pulumi import aws:ec2clientvpn/networkAssociation:NetworkAssociation example cvpn-endpoint-0ac3a1abbccddd666,vpn-assoc-0b8db902465d069ad
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: A list of up to five custom security groups to apply to the target network. If not specified, the VPC's default security group is assigned.
        :param pulumi.Input[str] subnet_id: The ID of the subnet to associate with the Client VPN endpoint.
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

            if client_vpn_endpoint_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_vpn_endpoint_id'")
            __props__['client_vpn_endpoint_id'] = client_vpn_endpoint_id
            __props__['security_groups'] = security_groups
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
            __props__['association_id'] = None
            __props__['status'] = None
            __props__['vpc_id'] = None
        super(NetworkAssociation, __self__).__init__(
            'aws:ec2clientvpn/networkAssociation:NetworkAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            association_id: Optional[pulumi.Input[str]] = None,
            client_vpn_endpoint_id: Optional[pulumi.Input[str]] = None,
            security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'NetworkAssociation':
        """
        Get an existing NetworkAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] association_id: The unique ID of the target network association.
        :param pulumi.Input[str] client_vpn_endpoint_id: The ID of the Client VPN endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: A list of up to five custom security groups to apply to the target network. If not specified, the VPC's default security group is assigned.
        :param pulumi.Input[str] status: The current state of the target network association.
        :param pulumi.Input[str] subnet_id: The ID of the subnet to associate with the Client VPN endpoint.
        :param pulumi.Input[str] vpc_id: The ID of the VPC in which the target subnet is located.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["association_id"] = association_id
        __props__["client_vpn_endpoint_id"] = client_vpn_endpoint_id
        __props__["security_groups"] = security_groups
        __props__["status"] = status
        __props__["subnet_id"] = subnet_id
        __props__["vpc_id"] = vpc_id
        return NetworkAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[str]:
        """
        The unique ID of the target network association.
        """
        return pulumi.get(self, "association_id")

    @property
    @pulumi.getter(name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> pulumi.Output[str]:
        """
        The ID of the Client VPN endpoint.
        """
        return pulumi.get(self, "client_vpn_endpoint_id")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of up to five custom security groups to apply to the target network. If not specified, the VPC's default security group is assigned.
        """
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The current state of the target network association.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet to associate with the Client VPN endpoint.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC in which the target subnet is located.
        """
        return pulumi.get(self, "vpc_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

