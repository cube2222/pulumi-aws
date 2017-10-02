// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "pulumi";

/**
 * Use this data source to get information about an EBS Snapshot for use when provisioning EBS Volumes
 */
export function getSnapshot(args?: GetSnapshotArgs): Promise<GetSnapshotResult> {
    args = args || {};
    return pulumi.runtime.invoke("aws:ebs/getSnapshot:getSnapshot", {
        "filter": args.filter,
        "mostRecent": args.mostRecent,
        "owners": args.owners,
        "restorableByUserIds": args.restorableByUserIds,
        "snapshotIds": args.snapshotIds,
    });
}

/**
 * A collection of arguments for invoking getSnapshot.
 */
export interface GetSnapshotArgs {
    /**
     * One or more name/value pairs to filter off of. There are
     * several valid keys, for a full reference, check out
     * [describe-snapshots in the AWS CLI reference][1].
     */
    filter?: pulumi.ComputedValue<{ name: pulumi.ComputedValue<string>, values: pulumi.ComputedValue<pulumi.ComputedValue<string>>[] }>[];
    /**
     * If more than one result is returned, use the most recent snapshot.
     */
    mostRecent?: pulumi.ComputedValue<boolean>;
    /**
     * Returns the snapshots owned by the specified owner id. Multiple owners can be specified.
     */
    owners?: pulumi.ComputedValue<pulumi.ComputedValue<string>>[];
    /**
     * One or more AWS accounts IDs that can create volumes from the snapshot.
     */
    restorableByUserIds?: pulumi.ComputedValue<pulumi.ComputedValue<string>>[];
    /**
     * Returns information on a specific snapshot_id.
     */
    snapshotIds?: pulumi.ComputedValue<pulumi.ComputedValue<string>>[];
}

/**
 * A collection of values returned by getSnapshot.
 */
export interface GetSnapshotResult {
    /**
     * The data encryption key identifier for the snapshot.
     */
    dataEncryptionKeyId: string;
    /**
     * A description for the snapshot
     */
    description: string;
    /**
     * Whether the snapshot is encrypted.
     */
    encrypted: boolean;
    /**
     * The ARN for the KMS encryption key.
     */
    kmsKeyId: string;
    /**
     * Value from an Amazon-maintained list (`amazon`, `aws-marketplace`, `microsoft`) of snapshot owners.
     */
    ownerAlias: string;
    /**
     * The AWS account ID of the EBS snapshot owner.
     */
    ownerId: string;
    /**
     * The snapshot ID (e.g. snap-59fcb34e).
     */
    snapshotId: string;
    /**
     * The snapshot state.
     */
    state: string;
    /**
     * A mapping of tags for the resource.
     */
    tags: { key: string, value: string }[];
    /**
     * The volume ID (e.g. vol-59fcb34e).
     */
    volumeId: string;
    /**
     * The size of the drive in GiBs.
     */
    volumeSize: number;
}
