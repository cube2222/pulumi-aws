// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ElastiCache
{
    /// <summary>
    /// Provides an ElastiCache Replication Group resource.
    /// For working with Memcached or single primary Redis instances (Cluster Mode Disabled), see the
    /// `aws.elasticache.Cluster` resource.
    /// 
    /// &gt; **Note:** When you change an attribute, such as `engine_version`, by
    /// default the ElastiCache API applies it in the next maintenance window. Because
    /// of this, this provider may report a difference in its planning phase because the
    /// actual modification has not yet taken place. You can use the
    /// `apply_immediately` flag to instruct the service to apply the change
    /// immediately. Using `apply_immediately` can result in a brief downtime as
    /// servers reboots.
    /// 
    /// ## Example Usage
    /// ### Redis Cluster Mode Disabled
    /// 
    /// To create a single shard primary with single read replica:
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.ElastiCache.ReplicationGroup("example", new Aws.ElastiCache.ReplicationGroupArgs
    ///         {
    ///             AutomaticFailoverEnabled = true,
    ///             AvailabilityZones = 
    ///             {
    ///                 "us-west-2a",
    ///                 "us-west-2b",
    ///             },
    ///             NodeType = "cache.m4.large",
    ///             NumberCacheClusters = 2,
    ///             ParameterGroupName = "default.redis3.2",
    ///             Port = 6379,
    ///             ReplicationGroupDescription = "test description",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// You have two options for adjusting the number of replicas:
    /// 
    /// * Adjusting `number_cache_clusters` directly. This will attempt to automatically add or remove replicas, but provides no granular control (e.g. preferred availability zone, cache cluster ID) for the added or removed replicas. This also currently expects cache cluster IDs in the form of `replication_group_id-00#`.
    /// * Otherwise for fine grained control of the underlying cache clusters, they can be added or removed with the `aws.elasticache.Cluster` resource and its `replication_group_id` attribute. In this situation, you will need to utilize [`ignoreChanges`](https://www.pulumi.com/docs/intro/concepts/programming-model/#ignorechanges) to prevent perpetual differences with the `number_cache_cluster` attribute.
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.ElastiCache.ReplicationGroup("example", new Aws.ElastiCache.ReplicationGroupArgs
    ///         {
    ///             AutomaticFailoverEnabled = true,
    ///             AvailabilityZones = 
    ///             {
    ///                 "us-west-2a",
    ///                 "us-west-2b",
    ///             },
    ///             ReplicationGroupDescription = "test description",
    ///             NodeType = "cache.m4.large",
    ///             NumberCacheClusters = 2,
    ///             ParameterGroupName = "default.redis3.2",
    ///             Port = 6379,
    ///         });
    ///         var replica = new List&lt;Aws.ElastiCache.Cluster&gt;();
    ///         for (var rangeIndex = 0; rangeIndex &lt; (1 == true); rangeIndex++)
    ///         {
    ///             var range = new { Value = rangeIndex };
    ///             replica.Add(new Aws.ElastiCache.Cluster($"replica-{range.Value}", new Aws.ElastiCache.ClusterArgs
    ///             {
    ///                 ReplicationGroupId = example.Id,
    ///             }));
    ///         }
    ///     }
    /// 
    /// }
    /// ```
    /// ### Redis Cluster Mode Enabled
    /// 
    /// To create two shards with a primary and a single read replica each:
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var baz = new Aws.ElastiCache.ReplicationGroup("baz", new Aws.ElastiCache.ReplicationGroupArgs
    ///         {
    ///             AutomaticFailoverEnabled = true,
    ///             ClusterMode = new Aws.ElastiCache.Inputs.ReplicationGroupClusterModeArgs
    ///             {
    ///                 NumNodeGroups = 2,
    ///                 ReplicasPerNodeGroup = 1,
    ///             },
    ///             NodeType = "cache.t2.small",
    ///             ParameterGroupName = "default.redis3.2.cluster.on",
    ///             Port = 6379,
    ///             ReplicationGroupDescription = "test description",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// &gt; **Note:** We currently do not support passing a `primary_cluster_id` in order to create the Replication Group.
    /// 
    /// &gt; **Note:** Automatic Failover is unavailable for Redis versions earlier than 2.8.6,
    /// and unavailable on T1 node types. For T2 node types, it is only available on Redis version 3.2.4 or later with cluster mode enabled. See the [High Availability Using Replication Groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.html) guide
    /// for full details on using Replication Groups.
    /// 
    /// ## Import
    /// 
    /// ElastiCache Replication Groups can be imported using the `replication_group_id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import aws:elasticache/replicationGroup:ReplicationGroup my_replication_group replication-group-1
    /// ```
    /// </summary>
    [AwsResourceType("aws:elasticache/replicationGroup:ReplicationGroup")]
    public partial class ReplicationGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.
        /// </summary>
        [Output("applyImmediately")]
        public Output<bool> ApplyImmediately { get; private set; } = null!;

        /// <summary>
        /// Whether to enable encryption at rest.
        /// </summary>
        [Output("atRestEncryptionEnabled")]
        public Output<bool?> AtRestEncryptionEnabled { get; private set; } = null!;

        /// <summary>
        /// The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.
        /// </summary>
        [Output("authToken")]
        public Output<string?> AuthToken { get; private set; } = null!;

        /// <summary>
        /// Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. This parameter is currently not supported by the AWS API. Defaults to `true`.
        /// </summary>
        [Output("autoMinorVersionUpgrade")]
        public Output<bool?> AutoMinorVersionUpgrade { get; private set; } = null!;

        /// <summary>
        /// Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
        /// </summary>
        [Output("automaticFailoverEnabled")]
        public Output<bool?> AutomaticFailoverEnabled { get; private set; } = null!;

        /// <summary>
        /// A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
        /// </summary>
        [Output("availabilityZones")]
        public Output<ImmutableArray<string>> AvailabilityZones { get; private set; } = null!;

        /// <summary>
        /// Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.
        /// </summary>
        [Output("clusterMode")]
        public Output<Outputs.ReplicationGroupClusterMode> ClusterMode { get; private set; } = null!;

        /// <summary>
        /// The address of the replication group configuration endpoint when cluster mode is enabled.
        /// </summary>
        [Output("configurationEndpointAddress")]
        public Output<string> ConfigurationEndpointAddress { get; private set; } = null!;

        /// <summary>
        /// The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`
        /// </summary>
        [Output("engine")]
        public Output<string?> Engine { get; private set; } = null!;

        /// <summary>
        /// The version number of the cache engine to be used for the cache clusters in this replication group.
        /// </summary>
        [Output("engineVersion")]
        public Output<string> EngineVersion { get; private set; } = null!;

        /// <summary>
        /// The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if `at_rest_encryption_enabled = true`.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// Specifies the weekly time range for when maintenance
        /// on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
        /// The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
        /// </summary>
        [Output("maintenanceWindow")]
        public Output<string> MaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// The identifiers of all the nodes that are part of this replication group.
        /// </summary>
        [Output("memberClusters")]
        public Output<ImmutableArray<string>> MemberClusters { get; private set; } = null!;

        /// <summary>
        /// The compute and memory capacity of the nodes in the node group.
        /// </summary>
        [Output("nodeType")]
        public Output<string> NodeType { get; private set; } = null!;

        /// <summary>
        /// An Amazon Resource Name (ARN) of an
        /// SNS topic to send ElastiCache notifications to. Example:
        /// `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
        /// </summary>
        [Output("notificationTopicArn")]
        public Output<string?> NotificationTopicArn { get; private set; } = null!;

        /// <summary>
        /// The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.
        /// </summary>
        [Output("numberCacheClusters")]
        public Output<int> NumberCacheClusters { get; private set; } = null!;

        /// <summary>
        /// The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
        /// </summary>
        [Output("parameterGroupName")]
        public Output<string> ParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.
        /// </summary>
        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        /// <summary>
        /// (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.
        /// </summary>
        [Output("primaryEndpointAddress")]
        public Output<string> PrimaryEndpointAddress { get; private set; } = null!;

        /// <summary>
        /// A user-created description for the replication group.
        /// </summary>
        [Output("replicationGroupDescription")]
        public Output<string> ReplicationGroupDescription { get; private set; } = null!;

        /// <summary>
        /// The replication group identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Output("replicationGroupId")]
        public Output<string> ReplicationGroupId { get; private set; } = null!;

        /// <summary>
        /// One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// A list of cache security group names to associate with this replication group.
        /// </summary>
        [Output("securityGroupNames")]
        public Output<ImmutableArray<string>> SecurityGroupNames { get; private set; } = null!;

        /// <summary>
        /// A single-element string list containing an
        /// Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
        /// Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        /// </summary>
        [Output("snapshotArns")]
        public Output<ImmutableArray<string>> SnapshotArns { get; private set; } = null!;

        /// <summary>
        /// The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.
        /// </summary>
        [Output("snapshotName")]
        public Output<string?> SnapshotName { get; private set; } = null!;

        /// <summary>
        /// The number of days for which ElastiCache will
        /// retain automatic cache cluster snapshots before deleting them. For example, if you set
        /// SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
        /// before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
        /// Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro cache nodes
        /// </summary>
        [Output("snapshotRetentionLimit")]
        public Output<int?> SnapshotRetentionLimit { get; private set; } = null!;

        /// <summary>
        /// The daily time range (in UTC) during which ElastiCache will
        /// begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`
        /// </summary>
        [Output("snapshotWindow")]
        public Output<string> SnapshotWindow { get; private set; } = null!;

        /// <summary>
        /// The name of the cache subnet group to be used for the replication group.
        /// </summary>
        [Output("subnetGroupName")]
        public Output<string> SubnetGroupName { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the resource. Adding tags to this resource will add or overwrite any existing tags on the clusters in the replication group and not to the group itself.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// Whether to enable encryption in transit.
        /// </summary>
        [Output("transitEncryptionEnabled")]
        public Output<bool?> TransitEncryptionEnabled { get; private set; } = null!;


        /// <summary>
        /// Create a ReplicationGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReplicationGroup(string name, ReplicationGroupArgs args, CustomResourceOptions? options = null)
            : base("aws:elasticache/replicationGroup:ReplicationGroup", name, args ?? new ReplicationGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReplicationGroup(string name, Input<string> id, ReplicationGroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:elasticache/replicationGroup:ReplicationGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ReplicationGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReplicationGroup Get(string name, Input<string> id, ReplicationGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new ReplicationGroup(name, id, state, options);
        }
    }

    public sealed class ReplicationGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.
        /// </summary>
        [Input("applyImmediately")]
        public Input<bool>? ApplyImmediately { get; set; }

        /// <summary>
        /// Whether to enable encryption at rest.
        /// </summary>
        [Input("atRestEncryptionEnabled")]
        public Input<bool>? AtRestEncryptionEnabled { get; set; }

        /// <summary>
        /// The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.
        /// </summary>
        [Input("authToken")]
        public Input<string>? AuthToken { get; set; }

        /// <summary>
        /// Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. This parameter is currently not supported by the AWS API. Defaults to `true`.
        /// </summary>
        [Input("autoMinorVersionUpgrade")]
        public Input<bool>? AutoMinorVersionUpgrade { get; set; }

        /// <summary>
        /// Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
        /// </summary>
        [Input("automaticFailoverEnabled")]
        public Input<bool>? AutomaticFailoverEnabled { get; set; }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;

        /// <summary>
        /// A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
        /// </summary>
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        /// <summary>
        /// Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.
        /// </summary>
        [Input("clusterMode")]
        public Input<Inputs.ReplicationGroupClusterModeArgs>? ClusterMode { get; set; }

        /// <summary>
        /// The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// The version number of the cache engine to be used for the cache clusters in this replication group.
        /// </summary>
        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        /// <summary>
        /// The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if `at_rest_encryption_enabled = true`.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// Specifies the weekly time range for when maintenance
        /// on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
        /// The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<string>? MaintenanceWindow { get; set; }

        /// <summary>
        /// The compute and memory capacity of the nodes in the node group.
        /// </summary>
        [Input("nodeType")]
        public Input<string>? NodeType { get; set; }

        /// <summary>
        /// An Amazon Resource Name (ARN) of an
        /// SNS topic to send ElastiCache notifications to. Example:
        /// `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
        /// </summary>
        [Input("notificationTopicArn")]
        public Input<string>? NotificationTopicArn { get; set; }

        /// <summary>
        /// The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.
        /// </summary>
        [Input("numberCacheClusters")]
        public Input<int>? NumberCacheClusters { get; set; }

        /// <summary>
        /// The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
        /// </summary>
        [Input("parameterGroupName")]
        public Input<string>? ParameterGroupName { get; set; }

        /// <summary>
        /// The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// A user-created description for the replication group.
        /// </summary>
        [Input("replicationGroupDescription", required: true)]
        public Input<string> ReplicationGroupDescription { get; set; } = null!;

        /// <summary>
        /// The replication group identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("replicationGroupId")]
        public Input<string>? ReplicationGroupId { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("securityGroupNames")]
        private InputList<string>? _securityGroupNames;

        /// <summary>
        /// A list of cache security group names to associate with this replication group.
        /// </summary>
        public InputList<string> SecurityGroupNames
        {
            get => _securityGroupNames ?? (_securityGroupNames = new InputList<string>());
            set => _securityGroupNames = value;
        }

        [Input("snapshotArns")]
        private InputList<string>? _snapshotArns;

        /// <summary>
        /// A single-element string list containing an
        /// Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
        /// Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        /// </summary>
        public InputList<string> SnapshotArns
        {
            get => _snapshotArns ?? (_snapshotArns = new InputList<string>());
            set => _snapshotArns = value;
        }

        /// <summary>
        /// The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.
        /// </summary>
        [Input("snapshotName")]
        public Input<string>? SnapshotName { get; set; }

        /// <summary>
        /// The number of days for which ElastiCache will
        /// retain automatic cache cluster snapshots before deleting them. For example, if you set
        /// SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
        /// before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
        /// Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro cache nodes
        /// </summary>
        [Input("snapshotRetentionLimit")]
        public Input<int>? SnapshotRetentionLimit { get; set; }

        /// <summary>
        /// The daily time range (in UTC) during which ElastiCache will
        /// begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`
        /// </summary>
        [Input("snapshotWindow")]
        public Input<string>? SnapshotWindow { get; set; }

        /// <summary>
        /// The name of the cache subnet group to be used for the replication group.
        /// </summary>
        [Input("subnetGroupName")]
        public Input<string>? SubnetGroupName { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource. Adding tags to this resource will add or overwrite any existing tags on the clusters in the replication group and not to the group itself.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// Whether to enable encryption in transit.
        /// </summary>
        [Input("transitEncryptionEnabled")]
        public Input<bool>? TransitEncryptionEnabled { get; set; }

        public ReplicationGroupArgs()
        {
        }
    }

    public sealed class ReplicationGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether any modifications are applied immediately, or during the next maintenance window. Default is `false`.
        /// </summary>
        [Input("applyImmediately")]
        public Input<bool>? ApplyImmediately { get; set; }

        /// <summary>
        /// Whether to enable encryption at rest.
        /// </summary>
        [Input("atRestEncryptionEnabled")]
        public Input<bool>? AtRestEncryptionEnabled { get; set; }

        /// <summary>
        /// The password used to access a password protected server. Can be specified only if `transit_encryption_enabled = true`.
        /// </summary>
        [Input("authToken")]
        public Input<string>? AuthToken { get; set; }

        /// <summary>
        /// Specifies whether a minor engine upgrades will be applied automatically to the underlying Cache Cluster instances during the maintenance window. This parameter is currently not supported by the AWS API. Defaults to `true`.
        /// </summary>
        [Input("autoMinorVersionUpgrade")]
        public Input<bool>? AutoMinorVersionUpgrade { get; set; }

        /// <summary>
        /// Specifies whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails. If true, Multi-AZ is enabled for this replication group. If false, Multi-AZ is disabled for this replication group. Must be enabled for Redis (cluster mode enabled) replication groups. Defaults to `false`.
        /// </summary>
        [Input("automaticFailoverEnabled")]
        public Input<bool>? AutomaticFailoverEnabled { get; set; }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;

        /// <summary>
        /// A list of EC2 availability zones in which the replication group's cache clusters will be created. The order of the availability zones in the list is not important.
        /// </summary>
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        /// <summary>
        /// Create a native redis cluster. `automatic_failover_enabled` must be set to true. Cluster Mode documented below. Only 1 `cluster_mode` block is allowed.
        /// </summary>
        [Input("clusterMode")]
        public Input<Inputs.ReplicationGroupClusterModeGetArgs>? ClusterMode { get; set; }

        /// <summary>
        /// The address of the replication group configuration endpoint when cluster mode is enabled.
        /// </summary>
        [Input("configurationEndpointAddress")]
        public Input<string>? ConfigurationEndpointAddress { get; set; }

        /// <summary>
        /// The name of the cache engine to be used for the clusters in this replication group. e.g. `redis`
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// The version number of the cache engine to be used for the cache clusters in this replication group.
        /// </summary>
        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        /// <summary>
        /// The ARN of the key that you wish to use if encrypting at rest. If not supplied, uses service managed encryption. Can be specified only if `at_rest_encryption_enabled = true`.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// Specifies the weekly time range for when maintenance
        /// on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
        /// The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<string>? MaintenanceWindow { get; set; }

        [Input("memberClusters")]
        private InputList<string>? _memberClusters;

        /// <summary>
        /// The identifiers of all the nodes that are part of this replication group.
        /// </summary>
        public InputList<string> MemberClusters
        {
            get => _memberClusters ?? (_memberClusters = new InputList<string>());
            set => _memberClusters = value;
        }

        /// <summary>
        /// The compute and memory capacity of the nodes in the node group.
        /// </summary>
        [Input("nodeType")]
        public Input<string>? NodeType { get; set; }

        /// <summary>
        /// An Amazon Resource Name (ARN) of an
        /// SNS topic to send ElastiCache notifications to. Example:
        /// `arn:aws:sns:us-east-1:012345678999:my_sns_topic`
        /// </summary>
        [Input("notificationTopicArn")]
        public Input<string>? NotificationTopicArn { get; set; }

        /// <summary>
        /// The number of cache clusters (primary and replicas) this replication group will have. If Multi-AZ is enabled, the value of this parameter must be at least 2. Updates will occur before other modifications.
        /// </summary>
        [Input("numberCacheClusters")]
        public Input<int>? NumberCacheClusters { get; set; }

        /// <summary>
        /// The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
        /// </summary>
        [Input("parameterGroupName")]
        public Input<string>? ParameterGroupName { get; set; }

        /// <summary>
        /// The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// (Redis only) The address of the endpoint for the primary node in the replication group, if the cluster mode is disabled.
        /// </summary>
        [Input("primaryEndpointAddress")]
        public Input<string>? PrimaryEndpointAddress { get; set; }

        /// <summary>
        /// A user-created description for the replication group.
        /// </summary>
        [Input("replicationGroupDescription")]
        public Input<string>? ReplicationGroupDescription { get; set; }

        /// <summary>
        /// The replication group identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("replicationGroupId")]
        public Input<string>? ReplicationGroupId { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// One or more Amazon VPC security groups associated with this replication group. Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("securityGroupNames")]
        private InputList<string>? _securityGroupNames;

        /// <summary>
        /// A list of cache security group names to associate with this replication group.
        /// </summary>
        public InputList<string> SecurityGroupNames
        {
            get => _securityGroupNames ?? (_securityGroupNames = new InputList<string>());
            set => _securityGroupNames = value;
        }

        [Input("snapshotArns")]
        private InputList<string>? _snapshotArns;

        /// <summary>
        /// A single-element string list containing an
        /// Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
        /// Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
        /// </summary>
        public InputList<string> SnapshotArns
        {
            get => _snapshotArns ?? (_snapshotArns = new InputList<string>());
            set => _snapshotArns = value;
        }

        /// <summary>
        /// The name of a snapshot from which to restore data into the new node group. Changing the `snapshot_name` forces a new resource.
        /// </summary>
        [Input("snapshotName")]
        public Input<string>? SnapshotName { get; set; }

        /// <summary>
        /// The number of days for which ElastiCache will
        /// retain automatic cache cluster snapshots before deleting them. For example, if you set
        /// SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
        /// before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
        /// Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro cache nodes
        /// </summary>
        [Input("snapshotRetentionLimit")]
        public Input<int>? SnapshotRetentionLimit { get; set; }

        /// <summary>
        /// The daily time range (in UTC) during which ElastiCache will
        /// begin taking a daily snapshot of your cache cluster. The minimum snapshot window is a 60 minute period. Example: `05:00-09:00`
        /// </summary>
        [Input("snapshotWindow")]
        public Input<string>? SnapshotWindow { get; set; }

        /// <summary>
        /// The name of the cache subnet group to be used for the replication group.
        /// </summary>
        [Input("subnetGroupName")]
        public Input<string>? SubnetGroupName { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource. Adding tags to this resource will add or overwrite any existing tags on the clusters in the replication group and not to the group itself.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// Whether to enable encryption in transit.
        /// </summary>
        [Input("transitEncryptionEnabled")]
        public Input<bool>? TransitEncryptionEnabled { get; set; }

        public ReplicationGroupState()
        {
        }
    }
}
