# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Cluster(pulumi.CustomResource):
    """
    Manages a [RDS Aurora Cluster][2]. To manage cluster instances that inherit configuration from the cluster (when not running the cluster in `serverless` engine mode), see the [`aws_rds_cluster_instance` resource](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html). To manage non-Aurora databases (e.g. MySQL, PostgreSQL, SQL Server, etc.), see the [`aws_db_instance` resource](https://www.terraform.io/docs/providers/aws/r/db_instance.html).
    
    For information on the difference between the available Aurora MySQL engines
    see [Comparison between Aurora MySQL 1 and Aurora MySQL 2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AuroraMySQL.Updates.20180206.html)
    in the Amazon RDS User Guide.
    
    Changes to a RDS Cluster can occur when you manually change a
    parameter, such as `port`, and are reflected in the next maintenance
    window. Because of this, Terraform may report a difference in its planning
    phase because a modification has not yet taken place. You can use the
    `apply_immediately` flag to instruct the service to apply the change immediately
    (see documentation below).
    
    ~> **Note:** using `apply_immediately` can result in a
    brief downtime as the server reboots. See the AWS Docs on [RDS Maintenance][4]
    for more information.
    
    ~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, apply_immediately=None, availability_zones=None, backtrack_window=None, backup_retention_period=None, cluster_identifier=None, cluster_identifier_prefix=None, cluster_members=None, database_name=None, db_cluster_parameter_group_name=None, db_subnet_group_name=None, deletion_protection=None, enabled_cloudwatch_logs_exports=None, engine=None, engine_mode=None, engine_version=None, final_snapshot_identifier=None, iam_database_authentication_enabled=None, iam_roles=None, kms_key_id=None, master_password=None, master_username=None, port=None, preferred_backup_window=None, preferred_maintenance_window=None, replication_source_identifier=None, s3_import=None, scaling_configuration=None, skip_final_snapshot=None, snapshot_identifier=None, source_region=None, storage_encrypted=None, tags=None, vpc_security_group_ids=None):
        """Create a Cluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if apply_immediately and not isinstance(apply_immediately, bool):
            raise TypeError('Expected property apply_immediately to be a bool')
        __self__.apply_immediately = apply_immediately
        """
        Specifies whether any cluster modifications
        are applied immediately, or during the next maintenance window. Default is
        `false`. See [Amazon RDS Documentation for more information.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)
        """
        __props__['applyImmediately'] = apply_immediately

        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError('Expected property availability_zones to be a list')
        __self__.availability_zones = availability_zones
        """
        A list of EC2 Availability Zones that
        instances in the DB cluster can be created in
        """
        __props__['availabilityZones'] = availability_zones

        if backtrack_window and not isinstance(backtrack_window, int):
            raise TypeError('Expected property backtrack_window to be a int')
        __self__.backtrack_window = backtrack_window
        """
        The target backtrack window, in seconds. Only available for `aurora` engine currently. To disable backtracking, set this value to `0`. Defaults to `0`. Must be between `0` and `259200` (72 hours)
        """
        __props__['backtrackWindow'] = backtrack_window

        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError('Expected property backup_retention_period to be a int')
        __self__.backup_retention_period = backup_retention_period
        """
        The days to retain backups for. Default `1`
        """
        __props__['backupRetentionPeriod'] = backup_retention_period

        if cluster_identifier and not isinstance(cluster_identifier, basestring):
            raise TypeError('Expected property cluster_identifier to be a basestring')
        __self__.cluster_identifier = cluster_identifier
        """
        The cluster identifier. If omitted, Terraform will assign a random, unique identifier.
        """
        __props__['clusterIdentifier'] = cluster_identifier

        if cluster_identifier_prefix and not isinstance(cluster_identifier_prefix, basestring):
            raise TypeError('Expected property cluster_identifier_prefix to be a basestring')
        __self__.cluster_identifier_prefix = cluster_identifier_prefix
        """
        Creates a unique cluster identifier beginning with the specified prefix. Conflicts with `cluster_identifer`.
        """
        __props__['clusterIdentifierPrefix'] = cluster_identifier_prefix

        if cluster_members and not isinstance(cluster_members, list):
            raise TypeError('Expected property cluster_members to be a list')
        __self__.cluster_members = cluster_members
        """
        List of RDS Instances that are a part of this cluster
        """
        __props__['clusterMembers'] = cluster_members

        if database_name and not isinstance(database_name, basestring):
            raise TypeError('Expected property database_name to be a basestring')
        __self__.database_name = database_name
        """
        Name for an automatically created database on cluster creation. There are different naming restrictions per database engine: [RDS Naming Constraints][5]
        """
        __props__['databaseName'] = database_name

        if db_cluster_parameter_group_name and not isinstance(db_cluster_parameter_group_name, basestring):
            raise TypeError('Expected property db_cluster_parameter_group_name to be a basestring')
        __self__.db_cluster_parameter_group_name = db_cluster_parameter_group_name
        """
        A cluster parameter group to associate with the cluster.
        """
        __props__['dbClusterParameterGroupName'] = db_cluster_parameter_group_name

        if db_subnet_group_name and not isinstance(db_subnet_group_name, basestring):
            raise TypeError('Expected property db_subnet_group_name to be a basestring')
        __self__.db_subnet_group_name = db_subnet_group_name
        """
        A DB subnet group to associate with this DB instance. **NOTE:** This must match the `db_subnet_group_name` specified on every [`aws_rds_cluster_instance`](https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html) in the cluster.
        """
        __props__['dbSubnetGroupName'] = db_subnet_group_name

        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError('Expected property deletion_protection to be a bool')
        __self__.deletion_protection = deletion_protection
        """
        If the DB instance should have deletion protection enabled. The database can't be deleted when this value is set to `true`. The default is `false`.
        """
        __props__['deletionProtection'] = deletion_protection

        if enabled_cloudwatch_logs_exports and not isinstance(enabled_cloudwatch_logs_exports, list):
            raise TypeError('Expected property enabled_cloudwatch_logs_exports to be a list')
        __self__.enabled_cloudwatch_logs_exports = enabled_cloudwatch_logs_exports
        """
        List of log types to export to cloudwatch. If omitted, no logs will be exported.
        The following log types are supported: `audit`, `error`, `general`, `slowquery`.
        """
        __props__['enabledCloudwatchLogsExports'] = enabled_cloudwatch_logs_exports

        if engine and not isinstance(engine, basestring):
            raise TypeError('Expected property engine to be a basestring')
        __self__.engine = engine
        """
        The name of the database engine to be used for this DB cluster. Defaults to `aurora`. Valid Values: `aurora`, `aurora-mysql`, `aurora-postgresql`
        """
        __props__['engine'] = engine

        if engine_mode and not isinstance(engine_mode, basestring):
            raise TypeError('Expected property engine_mode to be a basestring')
        __self__.engine_mode = engine_mode
        """
        The database engine mode. Valid values: `parallelquery`, `provisioned`, `serverless`. Defaults to: `provisioned`. See the [RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-serverless.html) for limitations when using `serverless`.
        """
        __props__['engineMode'] = engine_mode

        if engine_version and not isinstance(engine_version, basestring):
            raise TypeError('Expected property engine_version to be a basestring')
        __self__.engine_version = engine_version
        """
        The database engine version. Updating this argument results in an outage.
        """
        __props__['engineVersion'] = engine_version

        if final_snapshot_identifier and not isinstance(final_snapshot_identifier, basestring):
            raise TypeError('Expected property final_snapshot_identifier to be a basestring')
        __self__.final_snapshot_identifier = final_snapshot_identifier
        """
        The name of your final DB snapshot
        when this DB cluster is deleted. If omitted, no final snapshot will be
        made.
        """
        __props__['finalSnapshotIdentifier'] = final_snapshot_identifier

        if iam_database_authentication_enabled and not isinstance(iam_database_authentication_enabled, bool):
            raise TypeError('Expected property iam_database_authentication_enabled to be a bool')
        __self__.iam_database_authentication_enabled = iam_database_authentication_enabled
        """
        Specifies whether or mappings of AWS Identity and Access Management (IAM) accounts to database accounts is enabled. Please see [AWS Documentation][6] for availability and limitations.
        """
        __props__['iamDatabaseAuthenticationEnabled'] = iam_database_authentication_enabled

        if iam_roles and not isinstance(iam_roles, list):
            raise TypeError('Expected property iam_roles to be a list')
        __self__.iam_roles = iam_roles
        """
        A List of ARNs for the IAM roles to associate to the RDS Cluster.
        """
        __props__['iamRoles'] = iam_roles

        if kms_key_id and not isinstance(kms_key_id, basestring):
            raise TypeError('Expected property kms_key_id to be a basestring')
        __self__.kms_key_id = kms_key_id
        """
        The ARN for the KMS encryption key. When specifying `kms_key_id`, `storage_encrypted` needs to be set to true.
        """
        __props__['kmsKeyId'] = kms_key_id

        if master_password and not isinstance(master_password, basestring):
            raise TypeError('Expected property master_password to be a basestring')
        __self__.master_password = master_password
        """
        Password for the master DB user. Note that this may
        show up in logs, and it will be stored in the state file. Please refer to the [RDS Naming Constraints][5]
        """
        __props__['masterPassword'] = master_password

        if master_username and not isinstance(master_username, basestring):
            raise TypeError('Expected property master_username to be a basestring')
        __self__.master_username = master_username
        """
        Username for the master DB user. Please refer to the [RDS Naming Constraints][5]
        """
        __props__['masterUsername'] = master_username

        if port and not isinstance(port, int):
            raise TypeError('Expected property port to be a int')
        __self__.port = port
        """
        The port on which the DB accepts connections
        """
        __props__['port'] = port

        if preferred_backup_window and not isinstance(preferred_backup_window, basestring):
            raise TypeError('Expected property preferred_backup_window to be a basestring')
        __self__.preferred_backup_window = preferred_backup_window
        """
        The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter.Time in UTC
        Default: A 30-minute window selected at random from an 8-hour block of time per region. e.g. 04:00-09:00
        """
        __props__['preferredBackupWindow'] = preferred_backup_window

        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, basestring):
            raise TypeError('Expected property preferred_maintenance_window to be a basestring')
        __self__.preferred_maintenance_window = preferred_maintenance_window
        """
        The weekly time range during which system maintenance can occur, in (UTC) e.g. wed:04:00-wed:04:30
        """
        __props__['preferredMaintenanceWindow'] = preferred_maintenance_window

        if replication_source_identifier and not isinstance(replication_source_identifier, basestring):
            raise TypeError('Expected property replication_source_identifier to be a basestring')
        __self__.replication_source_identifier = replication_source_identifier
        """
        ARN of a source DB cluster or DB instance if this DB cluster is to be created as a Read Replica.
        """
        __props__['replicationSourceIdentifier'] = replication_source_identifier

        if s3_import and not isinstance(s3_import, dict):
            raise TypeError('Expected property s3_import to be a dict')
        __self__.s3_import = s3_import
        __props__['s3Import'] = s3_import

        if scaling_configuration and not isinstance(scaling_configuration, dict):
            raise TypeError('Expected property scaling_configuration to be a dict')
        __self__.scaling_configuration = scaling_configuration
        """
        Nested attribute with scaling properties. Only valid when `engine_mode` is set to `serverless`. More details below.
        """
        __props__['scalingConfiguration'] = scaling_configuration

        if skip_final_snapshot and not isinstance(skip_final_snapshot, bool):
            raise TypeError('Expected property skip_final_snapshot to be a bool')
        __self__.skip_final_snapshot = skip_final_snapshot
        """
        Determines whether a final DB snapshot is created before the DB cluster is deleted. If true is specified, no DB snapshot is created. If false is specified, a DB snapshot is created before the DB cluster is deleted, using the value from `final_snapshot_identifier`. Default is `false`.
        """
        __props__['skipFinalSnapshot'] = skip_final_snapshot

        if snapshot_identifier and not isinstance(snapshot_identifier, basestring):
            raise TypeError('Expected property snapshot_identifier to be a basestring')
        __self__.snapshot_identifier = snapshot_identifier
        """
        Specifies whether or not to create this cluster from a snapshot. You can use either the name or ARN when specifying a DB cluster snapshot, or the ARN when specifying a DB snapshot.
        """
        __props__['snapshotIdentifier'] = snapshot_identifier

        if source_region and not isinstance(source_region, basestring):
            raise TypeError('Expected property source_region to be a basestring')
        __self__.source_region = source_region
        """
        The source region for an encrypted replica DB cluster.
        """
        __props__['sourceRegion'] = source_region

        if storage_encrypted and not isinstance(storage_encrypted, bool):
            raise TypeError('Expected property storage_encrypted to be a bool')
        __self__.storage_encrypted = storage_encrypted
        """
        Specifies whether the DB cluster is encrypted. The default is `false` for `provisioned` `engine_mode` and `true` for `serverless` `engine_mode`.
        """
        __props__['storageEncrypted'] = storage_encrypted

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the DB cluster.
        """
        __props__['tags'] = tags

        if vpc_security_group_ids and not isinstance(vpc_security_group_ids, list):
            raise TypeError('Expected property vpc_security_group_ids to be a list')
        __self__.vpc_security_group_ids = vpc_security_group_ids
        """
        List of VPC security groups to associate
        with the Cluster
        """
        __props__['vpcSecurityGroupIds'] = vpc_security_group_ids

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        Amazon Resource Name (ARN) of cluster
        """
        __self__.cluster_resource_id = pulumi.runtime.UNKNOWN
        """
        The RDS Cluster Resource ID
        """
        __self__.endpoint = pulumi.runtime.UNKNOWN
        """
        The DNS address of the RDS instance
        """
        __self__.hosted_zone_id = pulumi.runtime.UNKNOWN
        """
        The Route53 Hosted Zone ID of the endpoint
        """
        __self__.reader_endpoint = pulumi.runtime.UNKNOWN
        """
        A read-only endpoint for the Aurora cluster, automatically
        load-balanced across replicas
        """

        super(Cluster, __self__).__init__(
            'aws:rds/cluster:Cluster',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'applyImmediately' in outs:
            self.apply_immediately = outs['applyImmediately']
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'availabilityZones' in outs:
            self.availability_zones = outs['availabilityZones']
        if 'backtrackWindow' in outs:
            self.backtrack_window = outs['backtrackWindow']
        if 'backupRetentionPeriod' in outs:
            self.backup_retention_period = outs['backupRetentionPeriod']
        if 'clusterIdentifier' in outs:
            self.cluster_identifier = outs['clusterIdentifier']
        if 'clusterIdentifierPrefix' in outs:
            self.cluster_identifier_prefix = outs['clusterIdentifierPrefix']
        if 'clusterMembers' in outs:
            self.cluster_members = outs['clusterMembers']
        if 'clusterResourceId' in outs:
            self.cluster_resource_id = outs['clusterResourceId']
        if 'databaseName' in outs:
            self.database_name = outs['databaseName']
        if 'dbClusterParameterGroupName' in outs:
            self.db_cluster_parameter_group_name = outs['dbClusterParameterGroupName']
        if 'dbSubnetGroupName' in outs:
            self.db_subnet_group_name = outs['dbSubnetGroupName']
        if 'deletionProtection' in outs:
            self.deletion_protection = outs['deletionProtection']
        if 'enabledCloudwatchLogsExports' in outs:
            self.enabled_cloudwatch_logs_exports = outs['enabledCloudwatchLogsExports']
        if 'endpoint' in outs:
            self.endpoint = outs['endpoint']
        if 'engine' in outs:
            self.engine = outs['engine']
        if 'engineMode' in outs:
            self.engine_mode = outs['engineMode']
        if 'engineVersion' in outs:
            self.engine_version = outs['engineVersion']
        if 'finalSnapshotIdentifier' in outs:
            self.final_snapshot_identifier = outs['finalSnapshotIdentifier']
        if 'hostedZoneId' in outs:
            self.hosted_zone_id = outs['hostedZoneId']
        if 'iamDatabaseAuthenticationEnabled' in outs:
            self.iam_database_authentication_enabled = outs['iamDatabaseAuthenticationEnabled']
        if 'iamRoles' in outs:
            self.iam_roles = outs['iamRoles']
        if 'kmsKeyId' in outs:
            self.kms_key_id = outs['kmsKeyId']
        if 'masterPassword' in outs:
            self.master_password = outs['masterPassword']
        if 'masterUsername' in outs:
            self.master_username = outs['masterUsername']
        if 'port' in outs:
            self.port = outs['port']
        if 'preferredBackupWindow' in outs:
            self.preferred_backup_window = outs['preferredBackupWindow']
        if 'preferredMaintenanceWindow' in outs:
            self.preferred_maintenance_window = outs['preferredMaintenanceWindow']
        if 'readerEndpoint' in outs:
            self.reader_endpoint = outs['readerEndpoint']
        if 'replicationSourceIdentifier' in outs:
            self.replication_source_identifier = outs['replicationSourceIdentifier']
        if 's3Import' in outs:
            self.s3_import = outs['s3Import']
        if 'scalingConfiguration' in outs:
            self.scaling_configuration = outs['scalingConfiguration']
        if 'skipFinalSnapshot' in outs:
            self.skip_final_snapshot = outs['skipFinalSnapshot']
        if 'snapshotIdentifier' in outs:
            self.snapshot_identifier = outs['snapshotIdentifier']
        if 'sourceRegion' in outs:
            self.source_region = outs['sourceRegion']
        if 'storageEncrypted' in outs:
            self.storage_encrypted = outs['storageEncrypted']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'vpcSecurityGroupIds' in outs:
            self.vpc_security_group_ids = outs['vpcSecurityGroupIds']
