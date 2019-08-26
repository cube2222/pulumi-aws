# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Budget(pulumi.CustomResource):
    account_id: pulumi.Output[str]
    """
    The ID of the target account for budget. Will use current user's account_id by default if omitted.
    """
    budget_type: pulumi.Output[str]
    """
    Whether this budget tracks monetary cost or usage.
    """
    cost_filters: pulumi.Output[dict]
    """
    Map of CostFilters key/value pairs to apply to the budget.
    """
    cost_types: pulumi.Output[dict]
    """
    Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
    """
    limit_amount: pulumi.Output[str]
    """
    The amount of cost or usage being measured for a budget.
    """
    limit_unit: pulumi.Output[str]
    """
    The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
    """
    name: pulumi.Output[str]
    """
    The name of a budget. Unique within accounts.
    """
    name_prefix: pulumi.Output[str]
    """
    The prefix of the name of a budget. Unique within accounts.
    """
    notifications: pulumi.Output[list]
    """
    Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
    """
    time_period_end: pulumi.Output[str]
    """
    The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
    """
    time_period_start: pulumi.Output[str]
    """
    The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
    """
    time_unit: pulumi.Output[str]
    """
    The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.
    """
    def __init__(__self__, resource_name, opts=None, account_id=None, budget_type=None, cost_filters=None, cost_types=None, limit_amount=None, limit_unit=None, name=None, name_prefix=None, notifications=None, time_period_end=None, time_period_start=None, time_unit=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the target account for budget. Will use current user's account_id by default if omitted.
        :param pulumi.Input[str] budget_type: Whether this budget tracks monetary cost or usage.
        :param pulumi.Input[dict] cost_filters: Map of CostFilters key/value pairs to apply to the budget.
        :param pulumi.Input[dict] cost_types: Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
        :param pulumi.Input[str] limit_amount: The amount of cost or usage being measured for a budget.
        :param pulumi.Input[str] limit_unit: The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
        :param pulumi.Input[str] name: The name of a budget. Unique within accounts.
        :param pulumi.Input[str] name_prefix: The prefix of the name of a budget. Unique within accounts.
        :param pulumi.Input[list] notifications: Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
        :param pulumi.Input[str] time_period_end: The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_period_start: The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_unit: The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/budgets_budget.html.markdown.
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

            __props__['account_id'] = account_id
            if budget_type is None:
                raise TypeError("Missing required property 'budget_type'")
            __props__['budget_type'] = budget_type
            __props__['cost_filters'] = cost_filters
            __props__['cost_types'] = cost_types
            if limit_amount is None:
                raise TypeError("Missing required property 'limit_amount'")
            __props__['limit_amount'] = limit_amount
            if limit_unit is None:
                raise TypeError("Missing required property 'limit_unit'")
            __props__['limit_unit'] = limit_unit
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['notifications'] = notifications
            __props__['time_period_end'] = time_period_end
            if time_period_start is None:
                raise TypeError("Missing required property 'time_period_start'")
            __props__['time_period_start'] = time_period_start
            if time_unit is None:
                raise TypeError("Missing required property 'time_unit'")
            __props__['time_unit'] = time_unit
        super(Budget, __self__).__init__(
            'aws:budgets/budget:Budget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, account_id=None, budget_type=None, cost_filters=None, cost_types=None, limit_amount=None, limit_unit=None, name=None, name_prefix=None, notifications=None, time_period_end=None, time_period_start=None, time_unit=None):
        """
        Get an existing Budget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the target account for budget. Will use current user's account_id by default if omitted.
        :param pulumi.Input[str] budget_type: Whether this budget tracks monetary cost or usage.
        :param pulumi.Input[dict] cost_filters: Map of CostFilters key/value pairs to apply to the budget.
        :param pulumi.Input[dict] cost_types: Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..
        :param pulumi.Input[str] limit_amount: The amount of cost or usage being measured for a budget.
        :param pulumi.Input[str] limit_unit: The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.
        :param pulumi.Input[str] name: The name of a budget. Unique within accounts.
        :param pulumi.Input[str] name_prefix: The prefix of the name of a budget. Unique within accounts.
        :param pulumi.Input[list] notifications: Object containing Budget Notifications. Can be used multiple times to define more than one budget notification
        :param pulumi.Input[str] time_period_end: The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_period_start: The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.
        :param pulumi.Input[str] time_unit: The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/budgets_budget.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["account_id"] = account_id
        __props__["budget_type"] = budget_type
        __props__["cost_filters"] = cost_filters
        __props__["cost_types"] = cost_types
        __props__["limit_amount"] = limit_amount
        __props__["limit_unit"] = limit_unit
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["notifications"] = notifications
        __props__["time_period_end"] = time_period_end
        __props__["time_period_start"] = time_period_start
        __props__["time_unit"] = time_unit
        return Budget(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

