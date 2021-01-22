// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Sagemaker.Outputs
{

    [OutputType]
    public sealed class UserProfileUserSettingsKernelGatewayAppSettings
    {
        /// <summary>
        /// A list of custom SageMaker images that are configured to run as a KernelGateway app. see Custom Image below.
        /// </summary>
        public readonly ImmutableArray<Outputs.UserProfileUserSettingsKernelGatewayAppSettingsCustomImage> CustomImages;
        /// <summary>
        /// The default instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance. see Default Resource Spec below.
        /// </summary>
        public readonly Outputs.UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec DefaultResourceSpec;

        [OutputConstructor]
        private UserProfileUserSettingsKernelGatewayAppSettings(
            ImmutableArray<Outputs.UserProfileUserSettingsKernelGatewayAppSettingsCustomImage> customImages,

            Outputs.UserProfileUserSettingsKernelGatewayAppSettingsDefaultResourceSpec defaultResourceSpec)
        {
            CustomImages = customImages;
            DefaultResourceSpec = defaultResourceSpec;
        }
    }
}
