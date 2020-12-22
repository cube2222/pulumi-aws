// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.LakeFormation
{
    public static class GetDataLakeSettings
    {
        /// <summary>
        /// Get Lake Formation principals designated as data lake administrators and lists of principal permission entries for default create database and default create table permissions.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.LakeFormation.GetDataLakeSettings.InvokeAsync(new Aws.LakeFormation.GetDataLakeSettingsArgs
        ///         {
        ///             CatalogId = "14916253649",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetDataLakeSettingsResult> InvokeAsync(GetDataLakeSettingsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDataLakeSettingsResult>("aws:lakeformation/getDataLakeSettings:getDataLakeSettings", args ?? new GetDataLakeSettingsArgs(), options.WithVersion());
    }


    public sealed class GetDataLakeSettingsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Identifier for the Data Catalog. By default, the account ID.
        /// </summary>
        [Input("catalogId")]
        public string? CatalogId { get; set; }

        public GetDataLakeSettingsArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetDataLakeSettingsResult
    {
        /// <summary>
        /// List of ARNs of AWS Lake Formation principals (IAM users or roles).
        /// </summary>
        public readonly ImmutableArray<string> Admins;
        public readonly string? CatalogId;
        /// <summary>
        /// Up to three configuration blocks of principal permissions for default create database permissions. Detailed below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDataLakeSettingsCreateDatabaseDefaultPermissionResult> CreateDatabaseDefaultPermissions;
        /// <summary>
        /// Up to three configuration blocks of principal permissions for default create table permissions. Detailed below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDataLakeSettingsCreateTableDefaultPermissionResult> CreateTableDefaultPermissions;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// List of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs).
        /// </summary>
        public readonly ImmutableArray<string> TrustedResourceOwners;

        [OutputConstructor]
        private GetDataLakeSettingsResult(
            ImmutableArray<string> admins,

            string? catalogId,

            ImmutableArray<Outputs.GetDataLakeSettingsCreateDatabaseDefaultPermissionResult> createDatabaseDefaultPermissions,

            ImmutableArray<Outputs.GetDataLakeSettingsCreateTableDefaultPermissionResult> createTableDefaultPermissions,

            string id,

            ImmutableArray<string> trustedResourceOwners)
        {
            Admins = admins;
            CatalogId = catalogId;
            CreateDatabaseDefaultPermissions = createDatabaseDefaultPermissions;
            CreateTableDefaultPermissions = createTableDefaultPermissions;
            Id = id;
            TrustedResourceOwners = trustedResourceOwners;
        }
    }
}