// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

import {Region} from "..";

let __config = new pulumi.Config("aws");

/**
 * The access key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
 */
export let accessKey: string | undefined = __config.get("accessKey");
export let allowedAccountIds: string[] | undefined = __config.getObject<string[]>("allowedAccountIds");
export let assumeRole: outputs.config.AssumeRole | undefined = __config.getObject<outputs.config.AssumeRole>("assumeRole");
export let endpoints: outputs.config.Endpoints[] | undefined = __config.getObject<outputs.config.Endpoints[]>("endpoints");
export let forbiddenAccountIds: string[] | undefined = __config.getObject<string[]>("forbiddenAccountIds");
/**
 * Configuration block with settings to ignore resource tags across all resources.
 */
export let ignoreTags: outputs.config.IgnoreTags | undefined = __config.getObject<outputs.config.IgnoreTags>("ignoreTags");
/**
 * Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`
 */
export let insecure: boolean | undefined = __config.getObject<boolean>("insecure");
/**
 * The maximum number of times an AWS API request is being executed. If the API request still fails, an error is thrown.
 */
export let maxRetries: number | undefined = __config.getObject<number>("maxRetries");
/**
 * The profile for API operations. If not set, the default profile created with `aws configure` will be used.
 */
export let profile: string | undefined = __config.get("profile") || utilities.getEnv("AWS_PROFILE");
/**
 * The region where AWS operations will take place. Examples are us-east-1, us-west-2, etc.
 */
export let region: Region | undefined = __config.getObject<Region>("region") || <any>utilities.getEnv("AWS_REGION", "AWS_DEFAULT_REGION");
/**
 * Set this to true to force the request to use path-style addressing, i.e., http://s3.amazonaws.com/BUCKET/KEY. By
 * default, the S3 client will use virtual hosted bucket addressing when possible (http://BUCKET.s3.amazonaws.com/KEY).
 * Specific to the Amazon S3 service.
 */
export let s3ForcePathStyle: boolean | undefined = __config.getObject<boolean>("s3ForcePathStyle");
/**
 * The secret key for API operations. You can retrieve this from the 'Security & Credentials' section of the AWS console.
 */
export let secretKey: string | undefined = __config.get("secretKey");
/**
 * The path to the shared credentials file. If not set this defaults to ~/.aws/credentials.
 */
export let sharedCredentialsFile: string | undefined = __config.get("sharedCredentialsFile");
/**
 * Skip the credentials validation via STS API. Used for AWS API implementations that do not have STS
 * available/implemented.
 */
export let skipCredentialsValidation: boolean | undefined = __config.getObject<boolean>("skipCredentialsValidation");
/**
 * Skip getting the supported EC2 platforms. Used by users that don't have ec2:DescribeAccountAttributes permissions.
 */
export let skipGetEc2Platforms: boolean | undefined = __config.getObject<boolean>("skipGetEc2Platforms");
export let skipMetadataApiCheck: boolean | undefined = __config.getObject<boolean>("skipMetadataApiCheck");
/**
 * Skip static validation of region name. Used by users of alternative AWS-like APIs or users w/ access to regions that are
 * not public (yet).
 */
export let skipRegionValidation: boolean | undefined = __config.getObject<boolean>("skipRegionValidation");
/**
 * Skip requesting the account ID. Used for AWS API implementations that do not have IAM/STS API and/or metadata API.
 */
export let skipRequestingAccountId: boolean | undefined = __config.getObject<boolean>("skipRequestingAccountId");
/**
 * session token. A session token is only required if you are using temporary security credentials.
 */
export let token: string | undefined = __config.get("token");
