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

__all__ = ['Instance']


class Instance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_version: Optional[pulumi.Input[str]] = None,
                 ami_id: Optional[pulumi.Input[str]] = None,
                 architecture: Optional[pulumi.Input[str]] = None,
                 auto_scaling_type: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 delete_ebs: Optional[pulumi.Input[bool]] = None,
                 delete_eip: Optional[pulumi.Input[bool]] = None,
                 ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEbsBlockDeviceArgs']]]]] = None,
                 ebs_optimized: Optional[pulumi.Input[bool]] = None,
                 ecs_cluster_arn: Optional[pulumi.Input[str]] = None,
                 elastic_ip: Optional[pulumi.Input[str]] = None,
                 ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEphemeralBlockDeviceArgs']]]]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 infrastructure_class: Optional[pulumi.Input[str]] = None,
                 install_updates_on_boot: Optional[pulumi.Input[bool]] = None,
                 instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 last_service_error_id: Optional[pulumi.Input[str]] = None,
                 layer_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 os: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 private_dns: Optional[pulumi.Input[str]] = None,
                 private_ip: Optional[pulumi.Input[str]] = None,
                 public_dns: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 registered_by: Optional[pulumi.Input[str]] = None,
                 reported_agent_version: Optional[pulumi.Input[str]] = None,
                 reported_os_family: Optional[pulumi.Input[str]] = None,
                 reported_os_name: Optional[pulumi.Input[str]] = None,
                 reported_os_version: Optional[pulumi.Input[str]] = None,
                 root_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceRootBlockDeviceArgs']]]]] = None,
                 root_device_type: Optional[pulumi.Input[str]] = None,
                 root_device_volume_id: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ssh_host_dsa_key_fingerprint: Optional[pulumi.Input[str]] = None,
                 ssh_host_rsa_key_fingerprint: Optional[pulumi.Input[str]] = None,
                 ssh_key_name: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tenancy: Optional[pulumi.Input[str]] = None,
                 virtualization_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an OpsWorks instance resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_instance = aws.opsworks.Instance("my-instance",
            stack_id=aws_opsworks_stack["main"]["id"],
            layer_ids=[aws_opsworks_custom_layer["my-layer"]["id"]],
            instance_type="t2.micro",
            os="Amazon Linux 2015.09",
            state="stopped")
        ```
        ## Block devices

        Each of the `*_block_device` attributes controls a portion of the AWS
        Instance's "Block Device Mapping". It's a good idea to familiarize yourself with [AWS's Block Device
        Mapping docs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html)
        to understand the implications of using these attributes.

        The `root_block_device` mapping supports the following:

        * `volume_type` - (Optional) The type of volume. Can be `"standard"`, `"gp2"`,
          or `"io1"`. (Default: `"standard"`).
        * `volume_size` - (Optional) The size of the volume in gigabytes.
        * `iops` - (Optional) The amount of provisioned
          [IOPS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
          This must be set with a `volume_type` of `"io1"`.
        * `delete_on_termination` - (Optional) Whether the volume should be destroyed
          on instance termination (Default: `true`).

        Modifying any of the `root_block_device` settings requires resource
        replacement.

        Each `ebs_block_device` supports the following:

        * `device_name` - The name of the device to mount.
        * `snapshot_id` - (Optional) The Snapshot ID to mount.
        * `volume_type` - (Optional) The type of volume. Can be `"standard"`, `"gp2"`,
          or `"io1"`. (Default: `"standard"`).
        * `volume_size` - (Optional) The size of the volume in gigabytes.
        * `iops` - (Optional) The amount of provisioned
          [IOPS](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
          This must be set with a `volume_type` of `"io1"`.
        * `delete_on_termination` - (Optional) Whether the volume should be destroyed
          on instance termination (Default: `true`).

        Modifying any `ebs_block_device` currently requires resource replacement.

        Each `ephemeral_block_device` supports the following:

        * `device_name` - The name of the block device to mount on the instance.
        * `virtual_name` - The [Instance Store Device
          Name](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
          (e.g. `"ephemeral0"`)

        Each AWS Instance type has a different set of Instance Store block devices
        available for attachment. AWS [publishes a
        list](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#StorageOnInstanceTypes)
        of which ephemeral devices are available on each type. The devices are always
        identified by the `virtual_name` in the format `"ephemeral{0..N}"`.

        > **NOTE:** Currently, changes to `*_block_device` configuration of _existing_
        resources cannot be automatically detected by this provider. After making updates
        to block device configuration, resource recreation can be manually triggered by
        using the [`up` command with the --replace argument](https://www.pulumi.com/docs/reference/cli/pulumi_up/).

        ## Import

        Opsworks Instances can be imported using the `instance id`, e.g.

        ```sh
         $ pulumi import aws:opsworks/instance:Instance my_instance 4d6d1710-ded9-42a1-b08e-b043ad7af1e2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_version: The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.
        :param pulumi.Input[str] ami_id: The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.
        :param pulumi.Input[str] architecture: Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`
        :param pulumi.Input[str] auto_scaling_type: Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.
        :param pulumi.Input[str] availability_zone: Name of the availability zone where instances will be created
               by default.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEbsBlockDeviceArgs']]]] ebs_block_devices: Additional EBS block devices to attach to the
               instance.  See Block Devices below for details.
        :param pulumi.Input[bool] ebs_optimized: If true, the launched EC2 instance will be EBS-optimized.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEphemeralBlockDeviceArgs']]]] ephemeral_block_devices: Customize Ephemeral (also known as
               "Instance Store") volumes on the instance. See Block Devices below for details.
        :param pulumi.Input[str] hostname: The instance's host name.
        :param pulumi.Input[bool] install_updates_on_boot: Controls where to install OS and package updates when the instance boots.  Defaults to `true`.
        :param pulumi.Input[str] instance_type: The type of instance to start
        :param pulumi.Input[Sequence[pulumi.Input[str]]] layer_ids: The ids of the layers the instance will belong to.
        :param pulumi.Input[str] os: Name of operating system that will be installed.
        :param pulumi.Input[str] private_dns: The private DNS name assigned to the instance. Can only be
               used inside the Amazon EC2, and only available if you've enabled DNS hostnames
               for your VPC
        :param pulumi.Input[str] private_ip: The private IP address assigned to the instance
        :param pulumi.Input[str] public_dns: The public DNS name assigned to the instance. For EC2-VPC, this
               is only available if you've enabled DNS hostnames for your VPC
        :param pulumi.Input[str] public_ip: The public IP address assigned to the instance, if applicable.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceRootBlockDeviceArgs']]]] root_block_devices: Customize details about the root block
               device of the instance. See Block Devices below for details.
        :param pulumi.Input[str] root_device_type: Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The associated security groups.
        :param pulumi.Input[str] ssh_key_name: Name of the SSH keypair that instances will have by default.
        :param pulumi.Input[str] stack_id: The id of the stack the instance will belong to.
        :param pulumi.Input[str] state: The desired state of the instance.  Can be either `"running"` or `"stopped"`.
        :param pulumi.Input[str] subnet_id: Subnet ID to attach to
        :param pulumi.Input[str] tenancy: Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`
        :param pulumi.Input[str] virtualization_type: Keyword to choose what virtualization mode created instances
               will use. Can be either `"paravirtual"` or `"hvm"`.
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

            __props__['agent_version'] = agent_version
            __props__['ami_id'] = ami_id
            __props__['architecture'] = architecture
            __props__['auto_scaling_type'] = auto_scaling_type
            __props__['availability_zone'] = availability_zone
            __props__['created_at'] = created_at
            __props__['delete_ebs'] = delete_ebs
            __props__['delete_eip'] = delete_eip
            __props__['ebs_block_devices'] = ebs_block_devices
            __props__['ebs_optimized'] = ebs_optimized
            __props__['ecs_cluster_arn'] = ecs_cluster_arn
            __props__['elastic_ip'] = elastic_ip
            __props__['ephemeral_block_devices'] = ephemeral_block_devices
            __props__['hostname'] = hostname
            __props__['infrastructure_class'] = infrastructure_class
            __props__['install_updates_on_boot'] = install_updates_on_boot
            __props__['instance_profile_arn'] = instance_profile_arn
            __props__['instance_type'] = instance_type
            __props__['last_service_error_id'] = last_service_error_id
            if layer_ids is None and not opts.urn:
                raise TypeError("Missing required property 'layer_ids'")
            __props__['layer_ids'] = layer_ids
            __props__['os'] = os
            __props__['platform'] = platform
            __props__['private_dns'] = private_dns
            __props__['private_ip'] = private_ip
            __props__['public_dns'] = public_dns
            __props__['public_ip'] = public_ip
            __props__['registered_by'] = registered_by
            __props__['reported_agent_version'] = reported_agent_version
            __props__['reported_os_family'] = reported_os_family
            __props__['reported_os_name'] = reported_os_name
            __props__['reported_os_version'] = reported_os_version
            __props__['root_block_devices'] = root_block_devices
            __props__['root_device_type'] = root_device_type
            __props__['root_device_volume_id'] = root_device_volume_id
            __props__['security_group_ids'] = security_group_ids
            __props__['ssh_host_dsa_key_fingerprint'] = ssh_host_dsa_key_fingerprint
            __props__['ssh_host_rsa_key_fingerprint'] = ssh_host_rsa_key_fingerprint
            __props__['ssh_key_name'] = ssh_key_name
            if stack_id is None and not opts.urn:
                raise TypeError("Missing required property 'stack_id'")
            __props__['stack_id'] = stack_id
            __props__['state'] = state
            __props__['status'] = status
            __props__['subnet_id'] = subnet_id
            __props__['tenancy'] = tenancy
            __props__['virtualization_type'] = virtualization_type
            __props__['ec2_instance_id'] = None
        super(Instance, __self__).__init__(
            'aws:opsworks/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_version: Optional[pulumi.Input[str]] = None,
            ami_id: Optional[pulumi.Input[str]] = None,
            architecture: Optional[pulumi.Input[str]] = None,
            auto_scaling_type: Optional[pulumi.Input[str]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            delete_ebs: Optional[pulumi.Input[bool]] = None,
            delete_eip: Optional[pulumi.Input[bool]] = None,
            ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEbsBlockDeviceArgs']]]]] = None,
            ebs_optimized: Optional[pulumi.Input[bool]] = None,
            ec2_instance_id: Optional[pulumi.Input[str]] = None,
            ecs_cluster_arn: Optional[pulumi.Input[str]] = None,
            elastic_ip: Optional[pulumi.Input[str]] = None,
            ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEphemeralBlockDeviceArgs']]]]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            infrastructure_class: Optional[pulumi.Input[str]] = None,
            install_updates_on_boot: Optional[pulumi.Input[bool]] = None,
            instance_profile_arn: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            last_service_error_id: Optional[pulumi.Input[str]] = None,
            layer_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            os: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None,
            private_dns: Optional[pulumi.Input[str]] = None,
            private_ip: Optional[pulumi.Input[str]] = None,
            public_dns: Optional[pulumi.Input[str]] = None,
            public_ip: Optional[pulumi.Input[str]] = None,
            registered_by: Optional[pulumi.Input[str]] = None,
            reported_agent_version: Optional[pulumi.Input[str]] = None,
            reported_os_family: Optional[pulumi.Input[str]] = None,
            reported_os_name: Optional[pulumi.Input[str]] = None,
            reported_os_version: Optional[pulumi.Input[str]] = None,
            root_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceRootBlockDeviceArgs']]]]] = None,
            root_device_type: Optional[pulumi.Input[str]] = None,
            root_device_volume_id: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ssh_host_dsa_key_fingerprint: Optional[pulumi.Input[str]] = None,
            ssh_host_rsa_key_fingerprint: Optional[pulumi.Input[str]] = None,
            ssh_key_name: Optional[pulumi.Input[str]] = None,
            stack_id: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tenancy: Optional[pulumi.Input[str]] = None,
            virtualization_type: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_version: The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.
        :param pulumi.Input[str] ami_id: The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.
        :param pulumi.Input[str] architecture: Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`
        :param pulumi.Input[str] auto_scaling_type: Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.
        :param pulumi.Input[str] availability_zone: Name of the availability zone where instances will be created
               by default.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEbsBlockDeviceArgs']]]] ebs_block_devices: Additional EBS block devices to attach to the
               instance.  See Block Devices below for details.
        :param pulumi.Input[bool] ebs_optimized: If true, the launched EC2 instance will be EBS-optimized.
        :param pulumi.Input[str] ec2_instance_id: EC2 instance ID
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceEphemeralBlockDeviceArgs']]]] ephemeral_block_devices: Customize Ephemeral (also known as
               "Instance Store") volumes on the instance. See Block Devices below for details.
        :param pulumi.Input[str] hostname: The instance's host name.
        :param pulumi.Input[bool] install_updates_on_boot: Controls where to install OS and package updates when the instance boots.  Defaults to `true`.
        :param pulumi.Input[str] instance_type: The type of instance to start
        :param pulumi.Input[Sequence[pulumi.Input[str]]] layer_ids: The ids of the layers the instance will belong to.
        :param pulumi.Input[str] os: Name of operating system that will be installed.
        :param pulumi.Input[str] private_dns: The private DNS name assigned to the instance. Can only be
               used inside the Amazon EC2, and only available if you've enabled DNS hostnames
               for your VPC
        :param pulumi.Input[str] private_ip: The private IP address assigned to the instance
        :param pulumi.Input[str] public_dns: The public DNS name assigned to the instance. For EC2-VPC, this
               is only available if you've enabled DNS hostnames for your VPC
        :param pulumi.Input[str] public_ip: The public IP address assigned to the instance, if applicable.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceRootBlockDeviceArgs']]]] root_block_devices: Customize details about the root block
               device of the instance. See Block Devices below for details.
        :param pulumi.Input[str] root_device_type: Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The associated security groups.
        :param pulumi.Input[str] ssh_key_name: Name of the SSH keypair that instances will have by default.
        :param pulumi.Input[str] stack_id: The id of the stack the instance will belong to.
        :param pulumi.Input[str] state: The desired state of the instance.  Can be either `"running"` or `"stopped"`.
        :param pulumi.Input[str] subnet_id: Subnet ID to attach to
        :param pulumi.Input[str] tenancy: Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`
        :param pulumi.Input[str] virtualization_type: Keyword to choose what virtualization mode created instances
               will use. Can be either `"paravirtual"` or `"hvm"`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["agent_version"] = agent_version
        __props__["ami_id"] = ami_id
        __props__["architecture"] = architecture
        __props__["auto_scaling_type"] = auto_scaling_type
        __props__["availability_zone"] = availability_zone
        __props__["created_at"] = created_at
        __props__["delete_ebs"] = delete_ebs
        __props__["delete_eip"] = delete_eip
        __props__["ebs_block_devices"] = ebs_block_devices
        __props__["ebs_optimized"] = ebs_optimized
        __props__["ec2_instance_id"] = ec2_instance_id
        __props__["ecs_cluster_arn"] = ecs_cluster_arn
        __props__["elastic_ip"] = elastic_ip
        __props__["ephemeral_block_devices"] = ephemeral_block_devices
        __props__["hostname"] = hostname
        __props__["infrastructure_class"] = infrastructure_class
        __props__["install_updates_on_boot"] = install_updates_on_boot
        __props__["instance_profile_arn"] = instance_profile_arn
        __props__["instance_type"] = instance_type
        __props__["last_service_error_id"] = last_service_error_id
        __props__["layer_ids"] = layer_ids
        __props__["os"] = os
        __props__["platform"] = platform
        __props__["private_dns"] = private_dns
        __props__["private_ip"] = private_ip
        __props__["public_dns"] = public_dns
        __props__["public_ip"] = public_ip
        __props__["registered_by"] = registered_by
        __props__["reported_agent_version"] = reported_agent_version
        __props__["reported_os_family"] = reported_os_family
        __props__["reported_os_name"] = reported_os_name
        __props__["reported_os_version"] = reported_os_version
        __props__["root_block_devices"] = root_block_devices
        __props__["root_device_type"] = root_device_type
        __props__["root_device_volume_id"] = root_device_volume_id
        __props__["security_group_ids"] = security_group_ids
        __props__["ssh_host_dsa_key_fingerprint"] = ssh_host_dsa_key_fingerprint
        __props__["ssh_host_rsa_key_fingerprint"] = ssh_host_rsa_key_fingerprint
        __props__["ssh_key_name"] = ssh_key_name
        __props__["stack_id"] = stack_id
        __props__["state"] = state
        __props__["status"] = status
        __props__["subnet_id"] = subnet_id
        __props__["tenancy"] = tenancy
        __props__["virtualization_type"] = virtualization_type
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.
        """
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter(name="amiId")
    def ami_id(self) -> pulumi.Output[str]:
        """
        The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.
        """
        return pulumi.get(self, "ami_id")

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional[str]]:
        """
        Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter(name="autoScalingType")
    def auto_scaling_type(self) -> pulumi.Output[Optional[str]]:
        """
        Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.
        """
        return pulumi.get(self, "auto_scaling_type")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        Name of the availability zone where instances will be created
        by default.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deleteEbs")
    def delete_ebs(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_ebs")

    @property
    @pulumi.getter(name="deleteEip")
    def delete_eip(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_eip")

    @property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> pulumi.Output[Sequence['outputs.InstanceEbsBlockDevice']]:
        """
        Additional EBS block devices to attach to the
        instance.  See Block Devices below for details.
        """
        return pulumi.get(self, "ebs_block_devices")

    @property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, the launched EC2 instance will be EBS-optimized.
        """
        return pulumi.get(self, "ebs_optimized")

    @property
    @pulumi.getter(name="ec2InstanceId")
    def ec2_instance_id(self) -> pulumi.Output[str]:
        """
        EC2 instance ID
        """
        return pulumi.get(self, "ec2_instance_id")

    @property
    @pulumi.getter(name="ecsClusterArn")
    def ecs_cluster_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ecs_cluster_arn")

    @property
    @pulumi.getter(name="elasticIp")
    def elastic_ip(self) -> pulumi.Output[str]:
        return pulumi.get(self, "elastic_ip")

    @property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> pulumi.Output[Sequence['outputs.InstanceEphemeralBlockDevice']]:
        """
        Customize Ephemeral (also known as
        "Instance Store") volumes on the instance. See Block Devices below for details.
        """
        return pulumi.get(self, "ephemeral_block_devices")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        The instance's host name.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="infrastructureClass")
    def infrastructure_class(self) -> pulumi.Output[str]:
        return pulumi.get(self, "infrastructure_class")

    @property
    @pulumi.getter(name="installUpdatesOnBoot")
    def install_updates_on_boot(self) -> pulumi.Output[Optional[bool]]:
        """
        Controls where to install OS and package updates when the instance boots.  Defaults to `true`.
        """
        return pulumi.get(self, "install_updates_on_boot")

    @property
    @pulumi.getter(name="instanceProfileArn")
    def instance_profile_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_profile_arn")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of instance to start
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="lastServiceErrorId")
    def last_service_error_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_service_error_id")

    @property
    @pulumi.getter(name="layerIds")
    def layer_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The ids of the layers the instance will belong to.
        """
        return pulumi.get(self, "layer_ids")

    @property
    @pulumi.getter
    def os(self) -> pulumi.Output[str]:
        """
        Name of operating system that will be installed.
        """
        return pulumi.get(self, "os")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> pulumi.Output[str]:
        """
        The private DNS name assigned to the instance. Can only be
        used inside the Amazon EC2, and only available if you've enabled DNS hostnames
        for your VPC
        """
        return pulumi.get(self, "private_dns")

    @property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> pulumi.Output[str]:
        """
        The private IP address assigned to the instance
        """
        return pulumi.get(self, "private_ip")

    @property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> pulumi.Output[str]:
        """
        The public DNS name assigned to the instance. For EC2-VPC, this
        is only available if you've enabled DNS hostnames for your VPC
        """
        return pulumi.get(self, "public_dns")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        """
        The public IP address assigned to the instance, if applicable.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="registeredBy")
    def registered_by(self) -> pulumi.Output[str]:
        return pulumi.get(self, "registered_by")

    @property
    @pulumi.getter(name="reportedAgentVersion")
    def reported_agent_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "reported_agent_version")

    @property
    @pulumi.getter(name="reportedOsFamily")
    def reported_os_family(self) -> pulumi.Output[str]:
        return pulumi.get(self, "reported_os_family")

    @property
    @pulumi.getter(name="reportedOsName")
    def reported_os_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "reported_os_name")

    @property
    @pulumi.getter(name="reportedOsVersion")
    def reported_os_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "reported_os_version")

    @property
    @pulumi.getter(name="rootBlockDevices")
    def root_block_devices(self) -> pulumi.Output[Sequence['outputs.InstanceRootBlockDevice']]:
        """
        Customize details about the root block
        device of the instance. See Block Devices below for details.
        """
        return pulumi.get(self, "root_block_devices")

    @property
    @pulumi.getter(name="rootDeviceType")
    def root_device_type(self) -> pulumi.Output[str]:
        """
        Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`
        """
        return pulumi.get(self, "root_device_type")

    @property
    @pulumi.getter(name="rootDeviceVolumeId")
    def root_device_volume_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "root_device_volume_id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The associated security groups.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="sshHostDsaKeyFingerprint")
    def ssh_host_dsa_key_fingerprint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ssh_host_dsa_key_fingerprint")

    @property
    @pulumi.getter(name="sshHostRsaKeyFingerprint")
    def ssh_host_rsa_key_fingerprint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ssh_host_rsa_key_fingerprint")

    @property
    @pulumi.getter(name="sshKeyName")
    def ssh_key_name(self) -> pulumi.Output[str]:
        """
        Name of the SSH keypair that instances will have by default.
        """
        return pulumi.get(self, "ssh_key_name")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        """
        The id of the stack the instance will belong to.
        """
        return pulumi.get(self, "stack_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        The desired state of the instance.  Can be either `"running"` or `"stopped"`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Subnet ID to attach to
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tenancy(self) -> pulumi.Output[str]:
        """
        Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`
        """
        return pulumi.get(self, "tenancy")

    @property
    @pulumi.getter(name="virtualizationType")
    def virtualization_type(self) -> pulumi.Output[str]:
        """
        Keyword to choose what virtualization mode created instances
        will use. Can be either `"paravirtual"` or `"hvm"`.
        """
        return pulumi.get(self, "virtualization_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

