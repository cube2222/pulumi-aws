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

__all__ = ['NodeGroup']


class NodeGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ami_type: Optional[pulumi.Input[str]] = None,
                 capacity_type: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 force_update_version: Optional[pulumi.Input[bool]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 launch_template: Optional[pulumi.Input[pulumi.InputType['NodeGroupLaunchTemplateArgs']]] = None,
                 node_group_name: Optional[pulumi.Input[str]] = None,
                 node_role_arn: Optional[pulumi.Input[str]] = None,
                 release_version: Optional[pulumi.Input[str]] = None,
                 remote_access: Optional[pulumi.Input[pulumi.InputType['NodeGroupRemoteAccessArgs']]] = None,
                 scaling_config: Optional[pulumi.Input[pulumi.InputType['NodeGroupScalingConfigArgs']]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EKS Node Group, which can provision and optionally update an Auto Scaling Group of Kubernetes worker nodes compatible with EKS. Additional documentation about this functionality can be found in the [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.eks.NodeGroup("example",
            cluster_name=aws_eks_cluster["example"]["name"],
            node_role_arn=aws_iam_role["example"]["arn"],
            subnet_ids=[__item["id"] for __item in aws_subnet["example"]],
            scaling_config=aws.eks.NodeGroupScalingConfigArgs(
                desired_size=1,
                max_size=1,
                min_size=1,
            ),
            opts=pulumi.ResourceOptions(depends_on=[
                    aws_iam_role_policy_attachment["example-AmazonEKSWorkerNodePolicy"],
                    aws_iam_role_policy_attachment["example-AmazonEKS_CNI_Policy"],
                    aws_iam_role_policy_attachment["example-AmazonEC2ContainerRegistryReadOnly"],
                ]))
        ```
        ### Ignoring Changes to Desired Size

        You can utilize [ignoreChanges](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) create an EKS Node Group with an initial size of running instances, then ignore any changes to that count caused externally (e.g. Application Autoscaling).

        ```python
        import pulumi
        import pulumi_aws as aws

        # ... other configurations ...
        example = aws.eks.NodeGroup("example", scaling_config=aws.eks.NodeGroupScalingConfigArgs(
            desired_size=2,
        ))
        ```
        ### Example IAM Role for EKS Node Group

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example = aws.iam.Role("example", assume_role_policy=json.dumps({
            "Statement": [{
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com",
                },
            }],
            "Version": "2012-10-17",
        }))
        example__amazon_eks_worker_node_policy = aws.iam.RolePolicyAttachment("example-AmazonEKSWorkerNodePolicy",
            policy_arn="arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
            role=example.name)
        example__amazon_ekscni_policy = aws.iam.RolePolicyAttachment("example-AmazonEKSCNIPolicy",
            policy_arn="arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
            role=example.name)
        example__amazon_ec2_container_registry_read_only = aws.iam.RolePolicyAttachment("example-AmazonEC2ContainerRegistryReadOnly",
            policy_arn="arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
            role=example.name)
        ```

        ## Import

        EKS Node Groups can be imported using the `cluster_name` and `node_group_name` separated by a colon (`:`), e.g.

        ```sh
         $ pulumi import aws:eks/nodeGroup:NodeGroup my_node_group my_cluster:my_node_group
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ami_type: Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to `AL2_x86_64`. Valid values: `AL2_x86_64`, `AL2_x86_64_GPU`, `AL2_ARM_64`. This provider will only perform drift detection if a configuration value is provided.
        :param pulumi.Input[str] capacity_type: Type of capacity associated with the EKS Node Group. Defaults to `ON_DEMAND`. Valid values: `ON_DEMAND`, `SPOT`.
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster.
        :param pulumi.Input[int] disk_size: Disk size in GiB for worker nodes. Defaults to `20`. This provider will only perform drift detection if a configuration value is provided.
        :param pulumi.Input[bool] force_update_version: Force version update if existing pods are unable to be drained due to a pod disruption budget issue.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_types: List of instance types associated with the EKS Node Group. Defaults to `["t3.medium"]`. This provider will only perform drift detection if a configuration value is provided.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        :param pulumi.Input[pulumi.InputType['NodeGroupLaunchTemplateArgs']] launch_template: Configuration block with Launch Template settings. Detailed below.
        :param pulumi.Input[str] node_group_name: Name of the EKS Node Group.
        :param pulumi.Input[str] node_role_arn: Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
        :param pulumi.Input[str] release_version: AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
        :param pulumi.Input[pulumi.InputType['NodeGroupRemoteAccessArgs']] remote_access: Configuration block with remote access settings. Detailed below.
        :param pulumi.Input[pulumi.InputType['NodeGroupScalingConfigArgs']] scaling_config: Configuration block with scaling settings. Detailed below.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags.
        :param pulumi.Input[str] version: EC2 Launch Template version number. While the API accepts values like `$Default` and `$Latest`, the API will convert the value to the associated version number (e.g. `1`) on read and This provider will show a difference on next plan. Using the `default_version` or `latest_version` attribute of the `ec2.LaunchTemplate` resource or data source is recommended for this argument.
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

            __props__['ami_type'] = ami_type
            __props__['capacity_type'] = capacity_type
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['disk_size'] = disk_size
            __props__['force_update_version'] = force_update_version
            __props__['instance_types'] = instance_types
            __props__['labels'] = labels
            __props__['launch_template'] = launch_template
            __props__['node_group_name'] = node_group_name
            if node_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'node_role_arn'")
            __props__['node_role_arn'] = node_role_arn
            __props__['release_version'] = release_version
            __props__['remote_access'] = remote_access
            if scaling_config is None and not opts.urn:
                raise TypeError("Missing required property 'scaling_config'")
            __props__['scaling_config'] = scaling_config
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['version'] = version
            __props__['arn'] = None
            __props__['resources'] = None
            __props__['status'] = None
        super(NodeGroup, __self__).__init__(
            'aws:eks/nodeGroup:NodeGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ami_type: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            capacity_type: Optional[pulumi.Input[str]] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            disk_size: Optional[pulumi.Input[int]] = None,
            force_update_version: Optional[pulumi.Input[bool]] = None,
            instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            launch_template: Optional[pulumi.Input[pulumi.InputType['NodeGroupLaunchTemplateArgs']]] = None,
            node_group_name: Optional[pulumi.Input[str]] = None,
            node_role_arn: Optional[pulumi.Input[str]] = None,
            release_version: Optional[pulumi.Input[str]] = None,
            remote_access: Optional[pulumi.Input[pulumi.InputType['NodeGroupRemoteAccessArgs']]] = None,
            resources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NodeGroupResourceArgs']]]]] = None,
            scaling_config: Optional[pulumi.Input[pulumi.InputType['NodeGroupScalingConfigArgs']]] = None,
            status: Optional[pulumi.Input[str]] = None,
            subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'NodeGroup':
        """
        Get an existing NodeGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ami_type: Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to `AL2_x86_64`. Valid values: `AL2_x86_64`, `AL2_x86_64_GPU`, `AL2_ARM_64`. This provider will only perform drift detection if a configuration value is provided.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the EKS Node Group.
        :param pulumi.Input[str] capacity_type: Type of capacity associated with the EKS Node Group. Defaults to `ON_DEMAND`. Valid values: `ON_DEMAND`, `SPOT`.
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster.
        :param pulumi.Input[int] disk_size: Disk size in GiB for worker nodes. Defaults to `20`. This provider will only perform drift detection if a configuration value is provided.
        :param pulumi.Input[bool] force_update_version: Force version update if existing pods are unable to be drained due to a pod disruption budget issue.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_types: List of instance types associated with the EKS Node Group. Defaults to `["t3.medium"]`. This provider will only perform drift detection if a configuration value is provided.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        :param pulumi.Input[pulumi.InputType['NodeGroupLaunchTemplateArgs']] launch_template: Configuration block with Launch Template settings. Detailed below.
        :param pulumi.Input[str] node_group_name: Name of the EKS Node Group.
        :param pulumi.Input[str] node_role_arn: Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
        :param pulumi.Input[str] release_version: AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
        :param pulumi.Input[pulumi.InputType['NodeGroupRemoteAccessArgs']] remote_access: Configuration block with remote access settings. Detailed below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NodeGroupResourceArgs']]]] resources: List of objects containing information about underlying resources.
        :param pulumi.Input[pulumi.InputType['NodeGroupScalingConfigArgs']] scaling_config: Configuration block with scaling settings. Detailed below.
        :param pulumi.Input[str] status: Status of the EKS Node Group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value mapping of resource tags.
        :param pulumi.Input[str] version: EC2 Launch Template version number. While the API accepts values like `$Default` and `$Latest`, the API will convert the value to the associated version number (e.g. `1`) on read and This provider will show a difference on next plan. Using the `default_version` or `latest_version` attribute of the `ec2.LaunchTemplate` resource or data source is recommended for this argument.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["ami_type"] = ami_type
        __props__["arn"] = arn
        __props__["capacity_type"] = capacity_type
        __props__["cluster_name"] = cluster_name
        __props__["disk_size"] = disk_size
        __props__["force_update_version"] = force_update_version
        __props__["instance_types"] = instance_types
        __props__["labels"] = labels
        __props__["launch_template"] = launch_template
        __props__["node_group_name"] = node_group_name
        __props__["node_role_arn"] = node_role_arn
        __props__["release_version"] = release_version
        __props__["remote_access"] = remote_access
        __props__["resources"] = resources
        __props__["scaling_config"] = scaling_config
        __props__["status"] = status
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        __props__["version"] = version
        return NodeGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="amiType")
    def ami_type(self) -> pulumi.Output[str]:
        """
        Type of Amazon Machine Image (AMI) associated with the EKS Node Group. Defaults to `AL2_x86_64`. Valid values: `AL2_x86_64`, `AL2_x86_64_GPU`, `AL2_ARM_64`. This provider will only perform drift detection if a configuration value is provided.
        """
        return pulumi.get(self, "ami_type")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the EKS Node Group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of capacity associated with the EKS Node Group. Defaults to `ON_DEMAND`. Valid values: `ON_DEMAND`, `SPOT`.
        """
        return pulumi.get(self, "capacity_type")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Name of the EKS Cluster.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> pulumi.Output[int]:
        """
        Disk size in GiB for worker nodes. Defaults to `20`. This provider will only perform drift detection if a configuration value is provided.
        """
        return pulumi.get(self, "disk_size")

    @property
    @pulumi.getter(name="forceUpdateVersion")
    def force_update_version(self) -> pulumi.Output[Optional[bool]]:
        """
        Force version update if existing pods are unable to be drained due to a pod disruption budget issue.
        """
        return pulumi.get(self, "force_update_version")

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> pulumi.Output[Sequence[str]]:
        """
        List of instance types associated with the EKS Node Group. Defaults to `["t3.medium"]`. This provider will only perform drift detection if a configuration value is provided.
        """
        return pulumi.get(self, "instance_types")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> pulumi.Output[Optional['outputs.NodeGroupLaunchTemplate']]:
        """
        Configuration block with Launch Template settings. Detailed below.
        """
        return pulumi.get(self, "launch_template")

    @property
    @pulumi.getter(name="nodeGroupName")
    def node_group_name(self) -> pulumi.Output[str]:
        """
        Name of the EKS Node Group.
        """
        return pulumi.get(self, "node_group_name")

    @property
    @pulumi.getter(name="nodeRoleArn")
    def node_role_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
        """
        return pulumi.get(self, "node_role_arn")

    @property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> pulumi.Output[str]:
        """
        AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
        """
        return pulumi.get(self, "release_version")

    @property
    @pulumi.getter(name="remoteAccess")
    def remote_access(self) -> pulumi.Output[Optional['outputs.NodeGroupRemoteAccess']]:
        """
        Configuration block with remote access settings. Detailed below.
        """
        return pulumi.get(self, "remote_access")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence['outputs.NodeGroupResource']]:
        """
        List of objects containing information about underlying resources.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> pulumi.Output['outputs.NodeGroupScalingConfig']:
        """
        Configuration block with scaling settings. Detailed below.
        """
        return pulumi.get(self, "scaling_config")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the EKS Node Group.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value mapping of resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        EC2 Launch Template version number. While the API accepts values like `$Default` and `$Latest`, the API will convert the value to the associated version number (e.g. `1`) on read and This provider will show a difference on next plan. Using the `default_version` or `latest_version` attribute of the `ec2.LaunchTemplate` resource or data source is recommended for this argument.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

