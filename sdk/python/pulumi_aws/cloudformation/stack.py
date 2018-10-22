# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Stack(pulumi.CustomResource):
    """
    Provides a CloudFormation Stack resource.
    """
    def __init__(__self__, __name__, __opts__=None, capabilities=None, disable_rollback=None, iam_role_arn=None, name=None, notification_arns=None, on_failure=None, parameters=None, policy_body=None, policy_url=None, tags=None, template_body=None, template_url=None, timeout_in_minutes=None):
        """Create a Stack resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if capabilities and not isinstance(capabilities, list):
            raise TypeError('Expected property capabilities to be a list')
        __self__.capabilities = capabilities
        """
        A list of capabilities.
        Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`
        """
        __props__['capabilities'] = capabilities

        if disable_rollback and not isinstance(disable_rollback, bool):
            raise TypeError('Expected property disable_rollback to be a bool')
        __self__.disable_rollback = disable_rollback
        """
        Set to true to disable rollback of the stack if stack creation failed.
        Conflicts with `on_failure`.
        """
        __props__['disableRollback'] = disable_rollback

        if iam_role_arn and not isinstance(iam_role_arn, basestring):
            raise TypeError('Expected property iam_role_arn to be a basestring')
        __self__.iam_role_arn = iam_role_arn
        """
        The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.
        """
        __props__['iamRoleArn'] = iam_role_arn

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Stack name.
        """
        __props__['name'] = name

        if notification_arns and not isinstance(notification_arns, list):
            raise TypeError('Expected property notification_arns to be a list')
        __self__.notification_arns = notification_arns
        """
        A list of SNS topic ARNs to publish stack related events.
        """
        __props__['notificationArns'] = notification_arns

        if on_failure and not isinstance(on_failure, basestring):
            raise TypeError('Expected property on_failure to be a basestring')
        __self__.on_failure = on_failure
        """
        Action to be taken if stack creation fails. This must be
        one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `disable_rollback`.
        """
        __props__['onFailure'] = on_failure

        if parameters and not isinstance(parameters, dict):
            raise TypeError('Expected property parameters to be a dict')
        __self__.parameters = parameters
        """
        A map of Parameter structures that specify input parameters for the stack.
        """
        __props__['parameters'] = parameters

        if policy_body and not isinstance(policy_body, basestring):
            raise TypeError('Expected property policy_body to be a basestring')
        __self__.policy_body = policy_body
        """
        Structure containing the stack policy body.
        Conflicts w/ `policy_url`.
        """
        __props__['policyBody'] = policy_body

        if policy_url and not isinstance(policy_url, basestring):
            raise TypeError('Expected property policy_url to be a basestring')
        __self__.policy_url = policy_url
        """
        Location of a file containing the stack policy.
        Conflicts w/ `policy_body`.
        """
        __props__['policyUrl'] = policy_url

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A list of tags to associate with this stack.
        """
        __props__['tags'] = tags

        if template_body and not isinstance(template_body, basestring):
            raise TypeError('Expected property template_body to be a basestring')
        __self__.template_body = template_body
        """
        Structure containing the template body (max size: 51,200 bytes).
        """
        __props__['templateBody'] = template_body

        if template_url and not isinstance(template_url, basestring):
            raise TypeError('Expected property template_url to be a basestring')
        __self__.template_url = template_url
        """
        Location of a file containing the template body (max size: 460,800 bytes).
        """
        __props__['templateUrl'] = template_url

        if timeout_in_minutes and not isinstance(timeout_in_minutes, int):
            raise TypeError('Expected property timeout_in_minutes to be a int')
        __self__.timeout_in_minutes = timeout_in_minutes
        """
        The amount of time that can pass before the stack status becomes `CREATE_FAILED`.
        """
        __props__['timeoutInMinutes'] = timeout_in_minutes

        __self__.outputs = pulumi.runtime.UNKNOWN
        """
        A map of outputs from the stack.
        """

        super(Stack, __self__).__init__(
            'aws:cloudformation/stack:Stack',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'capabilities' in outs:
            self.capabilities = outs['capabilities']
        if 'disableRollback' in outs:
            self.disable_rollback = outs['disableRollback']
        if 'iamRoleArn' in outs:
            self.iam_role_arn = outs['iamRoleArn']
        if 'name' in outs:
            self.name = outs['name']
        if 'notificationArns' in outs:
            self.notification_arns = outs['notificationArns']
        if 'onFailure' in outs:
            self.on_failure = outs['onFailure']
        if 'outputs' in outs:
            self.outputs = outs['outputs']
        if 'parameters' in outs:
            self.parameters = outs['parameters']
        if 'policyBody' in outs:
            self.policy_body = outs['policyBody']
        if 'policyUrl' in outs:
            self.policy_url = outs['policyUrl']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'templateBody' in outs:
            self.template_body = outs['templateBody']
        if 'templateUrl' in outs:
            self.template_url = outs['templateUrl']
        if 'timeoutInMinutes' in outs:
            self.timeout_in_minutes = outs['timeoutInMinutes']
