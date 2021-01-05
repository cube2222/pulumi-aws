// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    /// <summary>
    /// Provides a managed prefix list resource.
    /// 
    /// &gt; **NOTE on `max_entries`:** When you reference a Prefix List in a resource,
    /// the maximum number of entries for the prefix lists counts as the same number of rules
    /// or entries for the resource. For example, if you create a prefix list with a maximum
    /// of 20 entries and you reference that prefix list in a security group rule, this counts
    /// as 20 rules for the security group.
    /// 
    /// ## Example Usage
    /// 
    /// Basic usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.Ec2.ManagedPrefixList("example", new Aws.Ec2.ManagedPrefixListArgs
    ///         {
    ///             AddressFamily = "IPv4",
    ///             MaxEntries = 5,
    ///             Entries = 
    ///             {
    ///                 new Aws.Ec2.Inputs.ManagedPrefixListEntryArgs
    ///                 {
    ///                     Cidr = aws_vpc.Example.Cidr_block,
    ///                     Description = "Primary",
    ///                 },
    ///                 new Aws.Ec2.Inputs.ManagedPrefixListEntryArgs
    ///                 {
    ///                     Cidr = aws_vpc_ipv4_cidr_block_association.Example.Cidr_block,
    ///                     Description = "Secondary",
    ///                 },
    ///             },
    ///             Tags = 
    ///             {
    ///                 { "Env", "live" },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Prefix Lists can be imported using the `id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import aws:ec2/managedPrefixList:ManagedPrefixList default pl-0570a1d2d725c16be
    /// ```
    /// </summary>
    [AwsResourceType("aws:ec2/managedPrefixList:ManagedPrefixList")]
    public partial class ManagedPrefixList : Pulumi.CustomResource
    {
        /// <summary>
        /// The address family (`IPv4` or `IPv6`) of
        /// this prefix list.
        /// </summary>
        [Output("addressFamily")]
        public Output<string> AddressFamily { get; private set; } = null!;

        /// <summary>
        /// The ARN of the prefix list.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Can be specified multiple times for each prefix list entry.
        /// Each entry block supports fields documented below. Different entries may have
        /// overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        /// </summary>
        [Output("entries")]
        public Output<ImmutableArray<Outputs.ManagedPrefixListEntry>> Entries { get; private set; } = null!;

        /// <summary>
        /// The maximum number of entries that
        /// this prefix list can contain.
        /// </summary>
        [Output("maxEntries")]
        public Output<int> MaxEntries { get; private set; } = null!;

        /// <summary>
        /// The name of this resource. The name must not start with `com.amazonaws`.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the AWS account that owns this prefix list.
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The latest version of this prefix list.
        /// </summary>
        [Output("version")]
        public Output<int> Version { get; private set; } = null!;


        /// <summary>
        /// Create a ManagedPrefixList resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ManagedPrefixList(string name, ManagedPrefixListArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/managedPrefixList:ManagedPrefixList", name, args ?? new ManagedPrefixListArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ManagedPrefixList(string name, Input<string> id, ManagedPrefixListState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/managedPrefixList:ManagedPrefixList", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ManagedPrefixList resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ManagedPrefixList Get(string name, Input<string> id, ManagedPrefixListState? state = null, CustomResourceOptions? options = null)
        {
            return new ManagedPrefixList(name, id, state, options);
        }
    }

    public sealed class ManagedPrefixListArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The address family (`IPv4` or `IPv6`) of
        /// this prefix list.
        /// </summary>
        [Input("addressFamily", required: true)]
        public Input<string> AddressFamily { get; set; } = null!;

        [Input("entries")]
        private InputList<Inputs.ManagedPrefixListEntryArgs>? _entries;

        /// <summary>
        /// Can be specified multiple times for each prefix list entry.
        /// Each entry block supports fields documented below. Different entries may have
        /// overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        /// </summary>
        public InputList<Inputs.ManagedPrefixListEntryArgs> Entries
        {
            get => _entries ?? (_entries = new InputList<Inputs.ManagedPrefixListEntryArgs>());
            set => _entries = value;
        }

        /// <summary>
        /// The maximum number of entries that
        /// this prefix list can contain.
        /// </summary>
        [Input("maxEntries", required: true)]
        public Input<int> MaxEntries { get; set; } = null!;

        /// <summary>
        /// The name of this resource. The name must not start with `com.amazonaws`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to this resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public ManagedPrefixListArgs()
        {
        }
    }

    public sealed class ManagedPrefixListState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The address family (`IPv4` or `IPv6`) of
        /// this prefix list.
        /// </summary>
        [Input("addressFamily")]
        public Input<string>? AddressFamily { get; set; }

        /// <summary>
        /// The ARN of the prefix list.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("entries")]
        private InputList<Inputs.ManagedPrefixListEntryGetArgs>? _entries;

        /// <summary>
        /// Can be specified multiple times for each prefix list entry.
        /// Each entry block supports fields documented below. Different entries may have
        /// overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        /// </summary>
        public InputList<Inputs.ManagedPrefixListEntryGetArgs> Entries
        {
            get => _entries ?? (_entries = new InputList<Inputs.ManagedPrefixListEntryGetArgs>());
            set => _entries = value;
        }

        /// <summary>
        /// The maximum number of entries that
        /// this prefix list can contain.
        /// </summary>
        [Input("maxEntries")]
        public Input<int>? MaxEntries { get; set; }

        /// <summary>
        /// The name of this resource. The name must not start with `com.amazonaws`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the AWS account that owns this prefix list.
        /// </summary>
        [Input("ownerId")]
        public Input<string>? OwnerId { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to this resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The latest version of this prefix list.
        /// </summary>
        [Input("version")]
        public Input<int>? Version { get; set; }

        public ManagedPrefixListState()
        {
        }
    }
}
