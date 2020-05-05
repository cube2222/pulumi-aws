# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class FargateProfile(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the EKS Fargate Profile.
    """
    cluster_name: pulumi.Output[str]
    """
    Name of the EKS Cluster.
    """
    fargate_profile_name: pulumi.Output[str]
    """
    Name of the EKS Fargate Profile.
    """
    pod_execution_role_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Fargate Profile.
    """
    selectors: pulumi.Output[list]
    """
    Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Profile. Detailed below.

      * `labels` (`dict`) - Key-value map of Kubernetes labels for selection.
      * `namespace` (`str`) - Kubernetes namespace for selection.
    """
    status: pulumi.Output[str]
    """
    Status of the EKS Fargate Profile.
    """
    subnet_ids: pulumi.Output[list]
    """
    Identifiers of private EC2 Subnets to associate with the EKS Fargate Profile. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
    """
    tags: pulumi.Output[dict]
    """
    Key-value map of resource tags.
    """
    def __init__(__self__, resource_name, opts=None, cluster_name=None, fargate_profile_name=None, pod_execution_role_arn=None, selectors=None, subnet_ids=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an EKS Fargate Profile.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.eks.FargateProfile("example",
            cluster_name=aws_eks_cluster["example"]["name"],
            pod_execution_role_arn=aws_iam_role["example"]["arn"],
            subnet_ids=[__item["id"] for __item in aws_subnet["example"]],
            selector=[{
                "namespace": "example",
            }])
        ```

        ### Example IAM Role for EKS Fargate Profile

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example = aws.iam.Role("example", assume_role_policy=json.dumps({
            "Statement": [{
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "eks-fargate-pods.amazonaws.com",
                },
            }],
            "Version": "2012-10-17",
        }))
        example__amazon_eks_fargate_pod_execution_role_policy = aws.iam.RolePolicyAttachment("example-AmazonEKSFargatePodExecutionRolePolicy",
            policy_arn="arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy",
            role=example.name)
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster.
        :param pulumi.Input[str] fargate_profile_name: Name of the EKS Fargate Profile.
        :param pulumi.Input[str] pod_execution_role_arn: Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Fargate Profile.
        :param pulumi.Input[list] selectors: Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Profile. Detailed below.
        :param pulumi.Input[list] subnet_ids: Identifiers of private EC2 Subnets to associate with the EKS Fargate Profile. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
        :param pulumi.Input[dict] tags: Key-value map of resource tags.

        The **selectors** object supports the following:

          * `labels` (`pulumi.Input[dict]`) - Key-value map of Kubernetes labels for selection.
          * `namespace` (`pulumi.Input[str]`) - Kubernetes namespace for selection.
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

            if cluster_name is None:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['fargate_profile_name'] = fargate_profile_name
            if pod_execution_role_arn is None:
                raise TypeError("Missing required property 'pod_execution_role_arn'")
            __props__['pod_execution_role_arn'] = pod_execution_role_arn
            if selectors is None:
                raise TypeError("Missing required property 'selectors'")
            __props__['selectors'] = selectors
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['status'] = None
        super(FargateProfile, __self__).__init__(
            'aws:eks/fargateProfile:FargateProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, cluster_name=None, fargate_profile_name=None, pod_execution_role_arn=None, selectors=None, status=None, subnet_ids=None, tags=None):
        """
        Get an existing FargateProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the EKS Fargate Profile.
        :param pulumi.Input[str] cluster_name: Name of the EKS Cluster.
        :param pulumi.Input[str] fargate_profile_name: Name of the EKS Fargate Profile.
        :param pulumi.Input[str] pod_execution_role_arn: Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Fargate Profile.
        :param pulumi.Input[list] selectors: Configuration block(s) for selecting Kubernetes Pods to execute with this EKS Fargate Profile. Detailed below.
        :param pulumi.Input[str] status: Status of the EKS Fargate Profile.
        :param pulumi.Input[list] subnet_ids: Identifiers of private EC2 Subnets to associate with the EKS Fargate Profile. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
        :param pulumi.Input[dict] tags: Key-value map of resource tags.

        The **selectors** object supports the following:

          * `labels` (`pulumi.Input[dict]`) - Key-value map of Kubernetes labels for selection.
          * `namespace` (`pulumi.Input[str]`) - Kubernetes namespace for selection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["cluster_name"] = cluster_name
        __props__["fargate_profile_name"] = fargate_profile_name
        __props__["pod_execution_role_arn"] = pod_execution_role_arn
        __props__["selectors"] = selectors
        __props__["status"] = status
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        return FargateProfile(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

