// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Workspaces
{
    /// <summary>
    /// Provides an IP access control group in AWS Workspaces Service
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/workspaces_ip_group.html.markdown.
    /// </summary>
    public partial class IpGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// The description.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the IP group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// One or more pairs specifying the IP group rule (in CIDR format) from which web requests originate.
        /// </summary>
        [Output("rules")]
        public Output<ImmutableArray<Outputs.IpGroupRules>> Rules { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a IpGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IpGroup(string name, IpGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:workspaces/ipGroup:IpGroup", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private IpGroup(string name, Input<string> id, IpGroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:workspaces/ipGroup:IpGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing IpGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IpGroup Get(string name, Input<string> id, IpGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new IpGroup(name, id, state, options);
        }
    }

    public sealed class IpGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the IP group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("rules")]
        private InputList<Inputs.IpGroupRulesArgs>? _rules;

        /// <summary>
        /// One or more pairs specifying the IP group rule (in CIDR format) from which web requests originate.
        /// </summary>
        public InputList<Inputs.IpGroupRulesArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.IpGroupRulesArgs>());
            set => _rules = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public IpGroupArgs()
        {
        }
    }

    public sealed class IpGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the IP group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("rules")]
        private InputList<Inputs.IpGroupRulesGetArgs>? _rules;

        /// <summary>
        /// One or more pairs specifying the IP group rule (in CIDR format) from which web requests originate.
        /// </summary>
        public InputList<Inputs.IpGroupRulesGetArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.IpGroupRulesGetArgs>());
            set => _rules = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public IpGroupState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class IpGroupRulesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        /// </summary>
        [Input("source", required: true)]
        public Input<string> Source { get; set; } = null!;

        public IpGroupRulesArgs()
        {
        }
    }

    public sealed class IpGroupRulesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        /// </summary>
        [Input("source", required: true)]
        public Input<string> Source { get; set; } = null!;

        public IpGroupRulesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class IpGroupRules
    {
        /// <summary>
        /// The description.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        /// </summary>
        public readonly string Source;

        [OutputConstructor]
        private IpGroupRules(
            string? description,
            string source)
        {
            Description = description;
            Source = source;
        }
    }
    }
}
