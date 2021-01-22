// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Sagemaker.Inputs
{

    public sealed class FeatureGroupOnlineStoreConfigSecurityConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the AWS Key Management Service (AWS KMS) key that SageMaker Feature Store uses to encrypt the Amazon S3 objects at rest using Amazon S3 server-side encryption.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        public FeatureGroupOnlineStoreConfigSecurityConfigGetArgs()
        {
        }
    }
}
