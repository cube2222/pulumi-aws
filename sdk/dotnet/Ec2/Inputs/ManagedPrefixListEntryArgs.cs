// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2.Inputs
{

    public sealed class ManagedPrefixListEntryArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The CIDR block of this entry.
        /// </summary>
        [Input("cidr", required: true)]
        public Input<string> Cidr { get; set; } = null!;

        /// <summary>
        /// Description of this entry.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        public ManagedPrefixListEntryArgs()
        {
        }
    }
}
