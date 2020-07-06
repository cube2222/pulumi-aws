// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Iot.Inputs
{

    public sealed class TopicRuleErrorActionElasticsearchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The endpoint of your Elasticsearch domain.
        /// </summary>
        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        /// <summary>
        /// The unique identifier for the document you are storing.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// The Elasticsearch index where you want to store your data.
        /// </summary>
        [Input("index", required: true)]
        public Input<string> Index { get; set; } = null!;

        /// <summary>
        /// The IAM role ARN that has access to Elasticsearch.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        /// <summary>
        /// The type of document you are storing.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public TopicRuleErrorActionElasticsearchArgs()
        {
        }
    }
}