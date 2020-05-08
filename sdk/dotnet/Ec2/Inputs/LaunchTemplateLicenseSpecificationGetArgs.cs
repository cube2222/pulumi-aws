// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2.Inputs
{

    public sealed class LaunchTemplateLicenseSpecificationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ARN of the license configuration.
        /// </summary>
        [Input("licenseConfigurationArn", required: true)]
        public Input<string> LicenseConfigurationArn { get; set; } = null!;

        public LaunchTemplateLicenseSpecificationGetArgs()
        {
        }
    }
}