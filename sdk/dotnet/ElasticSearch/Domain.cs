// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ElasticSearch
{
    /// <summary>
    /// Manages an AWS Elasticsearch Domain.
    /// 
    /// ## Example Usage
    /// ### Basic Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.ElasticSearch.Domain("example", new Aws.ElasticSearch.DomainArgs
    ///         {
    ///             ClusterConfig = new Aws.ElasticSearch.Inputs.DomainClusterConfigArgs
    ///             {
    ///                 InstanceType = "r4.large.elasticsearch",
    ///             },
    ///             ElasticsearchVersion = "1.5",
    ///             SnapshotOptions = new Aws.ElasticSearch.Inputs.DomainSnapshotOptionsArgs
    ///             {
    ///                 AutomatedSnapshotStartHour = 23,
    ///             },
    ///             Tags = 
    ///             {
    ///                 { "Domain", "TestDomain" },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Access Policy
    /// 
    /// &gt; See also: `aws.elasticsearch.DomainPolicy` resource
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var config = new Config();
    ///         var domain = config.Get("domain") ?? "tf-test";
    ///         var currentRegion = Output.Create(Aws.GetRegion.InvokeAsync());
    ///         var currentCallerIdentity = Output.Create(Aws.GetCallerIdentity.InvokeAsync());
    ///         var example = new Aws.ElasticSearch.Domain("example", new Aws.ElasticSearch.DomainArgs
    ///         {
    ///             AccessPolicies = Output.Tuple(currentRegion, currentCallerIdentity).Apply(values =&gt;
    ///             {
    ///                 var currentRegion = values.Item1;
    ///                 var currentCallerIdentity = values.Item2;
    ///                 return @$"{{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {{
    ///       ""Action"": ""es:*"",
    ///       ""Principal"": ""*"",
    ///       ""Effect"": ""Allow"",
    ///       ""Resource"": ""arn:aws:es:{currentRegion.Name}:{currentCallerIdentity.AccountId}:domain/{domain}/*"",
    ///       ""Condition"": {{
    ///         ""IpAddress"": {{""aws:SourceIp"": [""66.193.100.22/32""]}}
    ///       }}
    ///     }}
    ///   ]
    /// }}
    /// ";
    ///             }),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Log Publishing to CloudWatch Logs
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleLogGroup = new Aws.CloudWatch.LogGroup("exampleLogGroup", new Aws.CloudWatch.LogGroupArgs
    ///         {
    ///         });
    ///         var exampleLogResourcePolicy = new Aws.CloudWatch.LogResourcePolicy("exampleLogResourcePolicy", new Aws.CloudWatch.LogResourcePolicyArgs
    ///         {
    ///             PolicyName = "example",
    ///             PolicyDocument = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {
    ///       ""Effect"": ""Allow"",
    ///       ""Principal"": {
    ///         ""Service"": ""es.amazonaws.com""
    ///       },
    ///       ""Action"": [
    ///         ""logs:PutLogEvents"",
    ///         ""logs:PutLogEventsBatch"",
    ///         ""logs:CreateLogStream""
    ///       ],
    ///       ""Resource"": ""arn:aws:logs:*""
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///         // .. other configuration ...
    ///         var exampleDomain = new Aws.ElasticSearch.Domain("exampleDomain", new Aws.ElasticSearch.DomainArgs
    ///         {
    ///             LogPublishingOptions = 
    ///             {
    ///                 new Aws.ElasticSearch.Inputs.DomainLogPublishingOptionArgs
    ///                 {
    ///                     CloudwatchLogGroupArn = exampleLogGroup.Arn,
    ///                     LogType = "INDEX_SLOW_LOGS",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### VPC based ES
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var config = new Config();
    ///         var vpc = config.RequireObject&lt;dynamic&gt;("vpc");
    ///         var domain = config.Get("domain") ?? "tf-test";
    ///         var selectedVpc = Output.Create(Aws.Ec2.GetVpc.InvokeAsync(new Aws.Ec2.GetVpcArgs
    ///         {
    ///             Tags = 
    ///             {
    ///                 { "Name", vpc },
    ///             },
    ///         }));
    ///         var selectedSubnetIds = selectedVpc.Apply(selectedVpc =&gt; Output.Create(Aws.Ec2.GetSubnetIds.InvokeAsync(new Aws.Ec2.GetSubnetIdsArgs
    ///         {
    ///             VpcId = selectedVpc.Id,
    ///             Tags = 
    ///             {
    ///                 { "Tier", "private" },
    ///             },
    ///         })));
    ///         var currentRegion = Output.Create(Aws.GetRegion.InvokeAsync());
    ///         var currentCallerIdentity = Output.Create(Aws.GetCallerIdentity.InvokeAsync());
    ///         var esSecurityGroup = new Aws.Ec2.SecurityGroup("esSecurityGroup", new Aws.Ec2.SecurityGroupArgs
    ///         {
    ///             Description = "Managed by Pulumi",
    ///             VpcId = selectedVpc.Apply(selectedVpc =&gt; selectedVpc.Id),
    ///             Ingress = 
    ///             {
    ///                 new Aws.Ec2.Inputs.SecurityGroupIngressArgs
    ///                 {
    ///                     FromPort = 443,
    ///                     ToPort = 443,
    ///                     Protocol = "tcp",
    ///                     CidrBlocks = 
    ///                     {
    ///                         selectedVpc.Apply(selectedVpc =&gt; selectedVpc.CidrBlock),
    ///                     },
    ///                 },
    ///             },
    ///         });
    ///         var esServiceLinkedRole = new Aws.Iam.ServiceLinkedRole("esServiceLinkedRole", new Aws.Iam.ServiceLinkedRoleArgs
    ///         {
    ///             AwsServiceName = "es.amazonaws.com",
    ///         });
    ///         var esDomain = new Aws.ElasticSearch.Domain("esDomain", new Aws.ElasticSearch.DomainArgs
    ///         {
    ///             ElasticsearchVersion = "6.3",
    ///             ClusterConfig = new Aws.ElasticSearch.Inputs.DomainClusterConfigArgs
    ///             {
    ///                 InstanceType = "m4.large.elasticsearch",
    ///             },
    ///             VpcOptions = new Aws.ElasticSearch.Inputs.DomainVpcOptionsArgs
    ///             {
    ///                 SubnetIds = 
    ///                 {
    ///                     selectedSubnetIds.Apply(selectedSubnetIds =&gt; selectedSubnetIds.Ids[0]),
    ///                     selectedSubnetIds.Apply(selectedSubnetIds =&gt; selectedSubnetIds.Ids[1]),
    ///                 },
    ///                 SecurityGroupIds = 
    ///                 {
    ///                     esSecurityGroup.Id,
    ///                 },
    ///             },
    ///             AdvancedOptions = 
    ///             {
    ///                 { "rest.action.multi.allow_explicit_index", "true" },
    ///             },
    ///             AccessPolicies = Output.Tuple(currentRegion, currentCallerIdentity).Apply(values =&gt;
    ///             {
    ///                 var currentRegion = values.Item1;
    ///                 var currentCallerIdentity = values.Item2;
    ///                 return @$"{{
    /// 	""Version"": ""2012-10-17"",
    /// 	""Statement"": [
    /// 		{{
    /// 			""Action"": ""es:*"",
    /// 			""Principal"": ""*"",
    /// 			""Effect"": ""Allow"",
    /// 			""Resource"": ""arn:aws:es:{currentRegion.Name}:{currentCallerIdentity.AccountId}:domain/{domain}/*""
    /// 		}}
    /// 	]
    /// }}
    /// ";
    ///             }),
    ///             SnapshotOptions = new Aws.ElasticSearch.Inputs.DomainSnapshotOptionsArgs
    ///             {
    ///                 AutomatedSnapshotStartHour = 23,
    ///             },
    ///             Tags = 
    ///             {
    ///                 { "Domain", "TestDomain" },
    ///             },
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 esServiceLinkedRole,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Elasticsearch domains can be imported using the `domain_name`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import aws:elasticsearch/domain:Domain example domain_name
    /// ```
    /// </summary>
    [AwsResourceType("aws:elasticsearch/domain:Domain")]
    public partial class Domain : Pulumi.CustomResource
    {
        /// <summary>
        /// IAM policy document specifying the access policies for the domain
        /// </summary>
        [Output("accessPolicies")]
        public Output<string> AccessPolicies { get; private set; } = null!;

        /// <summary>
        /// Key-value string pairs to specify advanced configuration options.
        /// Note that the values for these configuration options must be strings (wrapped in quotes) or they
        /// may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
        /// domain on every apply.
        /// </summary>
        [Output("advancedOptions")]
        public Output<ImmutableDictionary<string, string>> AdvancedOptions { get; private set; } = null!;

        /// <summary>
        /// Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        /// </summary>
        [Output("advancedSecurityOptions")]
        public Output<Outputs.DomainAdvancedSecurityOptions> AdvancedSecurityOptions { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name (ARN) of the domain.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Cluster configuration of the domain, see below.
        /// </summary>
        [Output("clusterConfig")]
        public Output<Outputs.DomainClusterConfig> ClusterConfig { get; private set; } = null!;

        /// <summary>
        /// Options for authenticating Kibana with Cognito. See below.
        /// </summary>
        [Output("cognitoOptions")]
        public Output<Outputs.DomainCognitoOptions?> CognitoOptions { get; private set; } = null!;

        /// <summary>
        /// Domain endpoint HTTP(S) related options. See below.
        /// </summary>
        [Output("domainEndpointOptions")]
        public Output<Outputs.DomainDomainEndpointOptions> DomainEndpointOptions { get; private set; } = null!;

        /// <summary>
        /// Unique identifier for the domain.
        /// </summary>
        [Output("domainId")]
        public Output<string> DomainId { get; private set; } = null!;

        /// <summary>
        /// Name of the domain.
        /// </summary>
        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        /// <summary>
        /// EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        /// </summary>
        [Output("ebsOptions")]
        public Output<Outputs.DomainEbsOptions> EbsOptions { get; private set; } = null!;

        /// <summary>
        /// The version of Elasticsearch to deploy. Defaults to `1.5`
        /// </summary>
        [Output("elasticsearchVersion")]
        public Output<string?> ElasticsearchVersion { get; private set; } = null!;

        /// <summary>
        /// Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        /// </summary>
        [Output("encryptAtRest")]
        public Output<Outputs.DomainEncryptAtRest> EncryptAtRest { get; private set; } = null!;

        /// <summary>
        /// Domain-specific endpoint used to submit index, search, and data upload requests.
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// Domain-specific endpoint for kibana without https scheme.
        /// * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
        /// * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
        /// </summary>
        [Output("kibanaEndpoint")]
        public Output<string> KibanaEndpoint { get; private set; } = null!;

        /// <summary>
        /// Options for publishing slow  and application logs to CloudWatch Logs. This block can be declared multiple times, for each log_type, within the same resource.
        /// </summary>
        [Output("logPublishingOptions")]
        public Output<ImmutableArray<Outputs.DomainLogPublishingOption>> LogPublishingOptions { get; private set; } = null!;

        /// <summary>
        /// Node-to-node encryption options. See below.
        /// </summary>
        [Output("nodeToNodeEncryption")]
        public Output<Outputs.DomainNodeToNodeEncryption> NodeToNodeEncryption { get; private set; } = null!;

        /// <summary>
        /// Snapshot related options, see below.
        /// </summary>
        [Output("snapshotOptions")]
        public Output<Outputs.DomainSnapshotOptions?> SnapshotOptions { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the resource
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        /// </summary>
        [Output("vpcOptions")]
        public Output<Outputs.DomainVpcOptions?> VpcOptions { get; private set; } = null!;


        /// <summary>
        /// Create a Domain resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Domain(string name, DomainArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:elasticsearch/domain:Domain", name, args ?? new DomainArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Domain(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
            : base("aws:elasticsearch/domain:Domain", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Domain resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Domain Get(string name, Input<string> id, DomainState? state = null, CustomResourceOptions? options = null)
        {
            return new Domain(name, id, state, options);
        }
    }

    public sealed class DomainArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// IAM policy document specifying the access policies for the domain
        /// </summary>
        [Input("accessPolicies")]
        public Input<string>? AccessPolicies { get; set; }

        [Input("advancedOptions")]
        private InputMap<string>? _advancedOptions;

        /// <summary>
        /// Key-value string pairs to specify advanced configuration options.
        /// Note that the values for these configuration options must be strings (wrapped in quotes) or they
        /// may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
        /// domain on every apply.
        /// </summary>
        public InputMap<string> AdvancedOptions
        {
            get => _advancedOptions ?? (_advancedOptions = new InputMap<string>());
            set => _advancedOptions = value;
        }

        /// <summary>
        /// Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        /// </summary>
        [Input("advancedSecurityOptions")]
        public Input<Inputs.DomainAdvancedSecurityOptionsArgs>? AdvancedSecurityOptions { get; set; }

        /// <summary>
        /// Cluster configuration of the domain, see below.
        /// </summary>
        [Input("clusterConfig")]
        public Input<Inputs.DomainClusterConfigArgs>? ClusterConfig { get; set; }

        /// <summary>
        /// Options for authenticating Kibana with Cognito. See below.
        /// </summary>
        [Input("cognitoOptions")]
        public Input<Inputs.DomainCognitoOptionsArgs>? CognitoOptions { get; set; }

        /// <summary>
        /// Domain endpoint HTTP(S) related options. See below.
        /// </summary>
        [Input("domainEndpointOptions")]
        public Input<Inputs.DomainDomainEndpointOptionsArgs>? DomainEndpointOptions { get; set; }

        /// <summary>
        /// Name of the domain.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        /// <summary>
        /// EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        /// </summary>
        [Input("ebsOptions")]
        public Input<Inputs.DomainEbsOptionsArgs>? EbsOptions { get; set; }

        /// <summary>
        /// The version of Elasticsearch to deploy. Defaults to `1.5`
        /// </summary>
        [Input("elasticsearchVersion")]
        public Input<string>? ElasticsearchVersion { get; set; }

        /// <summary>
        /// Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        /// </summary>
        [Input("encryptAtRest")]
        public Input<Inputs.DomainEncryptAtRestArgs>? EncryptAtRest { get; set; }

        [Input("logPublishingOptions")]
        private InputList<Inputs.DomainLogPublishingOptionArgs>? _logPublishingOptions;

        /// <summary>
        /// Options for publishing slow  and application logs to CloudWatch Logs. This block can be declared multiple times, for each log_type, within the same resource.
        /// </summary>
        public InputList<Inputs.DomainLogPublishingOptionArgs> LogPublishingOptions
        {
            get => _logPublishingOptions ?? (_logPublishingOptions = new InputList<Inputs.DomainLogPublishingOptionArgs>());
            set => _logPublishingOptions = value;
        }

        /// <summary>
        /// Node-to-node encryption options. See below.
        /// </summary>
        [Input("nodeToNodeEncryption")]
        public Input<Inputs.DomainNodeToNodeEncryptionArgs>? NodeToNodeEncryption { get; set; }

        /// <summary>
        /// Snapshot related options, see below.
        /// </summary>
        [Input("snapshotOptions")]
        public Input<Inputs.DomainSnapshotOptionsArgs>? SnapshotOptions { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        /// </summary>
        [Input("vpcOptions")]
        public Input<Inputs.DomainVpcOptionsArgs>? VpcOptions { get; set; }

        public DomainArgs()
        {
        }
    }

    public sealed class DomainState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// IAM policy document specifying the access policies for the domain
        /// </summary>
        [Input("accessPolicies")]
        public Input<string>? AccessPolicies { get; set; }

        [Input("advancedOptions")]
        private InputMap<string>? _advancedOptions;

        /// <summary>
        /// Key-value string pairs to specify advanced configuration options.
        /// Note that the values for these configuration options must be strings (wrapped in quotes) or they
        /// may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
        /// domain on every apply.
        /// </summary>
        public InputMap<string> AdvancedOptions
        {
            get => _advancedOptions ?? (_advancedOptions = new InputMap<string>());
            set => _advancedOptions = value;
        }

        /// <summary>
        /// Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        /// </summary>
        [Input("advancedSecurityOptions")]
        public Input<Inputs.DomainAdvancedSecurityOptionsGetArgs>? AdvancedSecurityOptions { get; set; }

        /// <summary>
        /// Amazon Resource Name (ARN) of the domain.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Cluster configuration of the domain, see below.
        /// </summary>
        [Input("clusterConfig")]
        public Input<Inputs.DomainClusterConfigGetArgs>? ClusterConfig { get; set; }

        /// <summary>
        /// Options for authenticating Kibana with Cognito. See below.
        /// </summary>
        [Input("cognitoOptions")]
        public Input<Inputs.DomainCognitoOptionsGetArgs>? CognitoOptions { get; set; }

        /// <summary>
        /// Domain endpoint HTTP(S) related options. See below.
        /// </summary>
        [Input("domainEndpointOptions")]
        public Input<Inputs.DomainDomainEndpointOptionsGetArgs>? DomainEndpointOptions { get; set; }

        /// <summary>
        /// Unique identifier for the domain.
        /// </summary>
        [Input("domainId")]
        public Input<string>? DomainId { get; set; }

        /// <summary>
        /// Name of the domain.
        /// </summary>
        [Input("domainName")]
        public Input<string>? DomainName { get; set; }

        /// <summary>
        /// EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        /// </summary>
        [Input("ebsOptions")]
        public Input<Inputs.DomainEbsOptionsGetArgs>? EbsOptions { get; set; }

        /// <summary>
        /// The version of Elasticsearch to deploy. Defaults to `1.5`
        /// </summary>
        [Input("elasticsearchVersion")]
        public Input<string>? ElasticsearchVersion { get; set; }

        /// <summary>
        /// Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        /// </summary>
        [Input("encryptAtRest")]
        public Input<Inputs.DomainEncryptAtRestGetArgs>? EncryptAtRest { get; set; }

        /// <summary>
        /// Domain-specific endpoint used to submit index, search, and data upload requests.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// Domain-specific endpoint for kibana without https scheme.
        /// * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
        /// * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
        /// </summary>
        [Input("kibanaEndpoint")]
        public Input<string>? KibanaEndpoint { get; set; }

        [Input("logPublishingOptions")]
        private InputList<Inputs.DomainLogPublishingOptionGetArgs>? _logPublishingOptions;

        /// <summary>
        /// Options for publishing slow  and application logs to CloudWatch Logs. This block can be declared multiple times, for each log_type, within the same resource.
        /// </summary>
        public InputList<Inputs.DomainLogPublishingOptionGetArgs> LogPublishingOptions
        {
            get => _logPublishingOptions ?? (_logPublishingOptions = new InputList<Inputs.DomainLogPublishingOptionGetArgs>());
            set => _logPublishingOptions = value;
        }

        /// <summary>
        /// Node-to-node encryption options. See below.
        /// </summary>
        [Input("nodeToNodeEncryption")]
        public Input<Inputs.DomainNodeToNodeEncryptionGetArgs>? NodeToNodeEncryption { get; set; }

        /// <summary>
        /// Snapshot related options, see below.
        /// </summary>
        [Input("snapshotOptions")]
        public Input<Inputs.DomainSnapshotOptionsGetArgs>? SnapshotOptions { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        /// </summary>
        [Input("vpcOptions")]
        public Input<Inputs.DomainVpcOptionsGetArgs>? VpcOptions { get; set; }

        public DomainState()
        {
        }
    }
}
