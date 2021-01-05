// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Emr
{
    /// <summary>
    /// ## Import
    /// 
    /// EMR Instance Fleet can be imported with the EMR Cluster identifier and Instance Fleet identifier separated by a forward slash (`/`), e.g. console
    /// 
    /// ```sh
    ///  $ pulumi import aws:emr/instanceFleet:InstanceFleet example j-123456ABCDEF/if-15EK4O09RZLNR
    /// ```
    /// </summary>
    [AwsResourceType("aws:emr/instanceFleet:InstanceFleet")]
    public partial class InstanceFleet : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// Configuration block for instance fleet
        /// </summary>
        [Output("instanceTypeConfigs")]
        public Output<ImmutableArray<Outputs.InstanceFleetInstanceTypeConfig>> InstanceTypeConfigs { get; private set; } = null!;

        /// <summary>
        /// Configuration block for launch specification
        /// </summary>
        [Output("launchSpecifications")]
        public Output<Outputs.InstanceFleetLaunchSpecifications?> LaunchSpecifications { get; private set; } = null!;

        /// <summary>
        /// Friendly name given to the instance fleet.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("provisionedOnDemandCapacity")]
        public Output<int> ProvisionedOnDemandCapacity { get; private set; } = null!;

        [Output("provisionedSpotCapacity")]
        public Output<int> ProvisionedSpotCapacity { get; private set; } = null!;

        /// <summary>
        /// The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.
        /// </summary>
        [Output("targetOnDemandCapacity")]
        public Output<int?> TargetOnDemandCapacity { get; private set; } = null!;

        /// <summary>
        /// The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.
        /// </summary>
        [Output("targetSpotCapacity")]
        public Output<int?> TargetSpotCapacity { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceFleet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceFleet(string name, InstanceFleetArgs args, CustomResourceOptions? options = null)
            : base("aws:emr/instanceFleet:InstanceFleet", name, args ?? new InstanceFleetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceFleet(string name, Input<string> id, InstanceFleetState? state = null, CustomResourceOptions? options = null)
            : base("aws:emr/instanceFleet:InstanceFleet", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing InstanceFleet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceFleet Get(string name, Input<string> id, InstanceFleetState? state = null, CustomResourceOptions? options = null)
        {
            return new InstanceFleet(name, id, state, options);
        }
    }

    public sealed class InstanceFleetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("instanceTypeConfigs")]
        private InputList<Inputs.InstanceFleetInstanceTypeConfigArgs>? _instanceTypeConfigs;

        /// <summary>
        /// Configuration block for instance fleet
        /// </summary>
        public InputList<Inputs.InstanceFleetInstanceTypeConfigArgs> InstanceTypeConfigs
        {
            get => _instanceTypeConfigs ?? (_instanceTypeConfigs = new InputList<Inputs.InstanceFleetInstanceTypeConfigArgs>());
            set => _instanceTypeConfigs = value;
        }

        /// <summary>
        /// Configuration block for launch specification
        /// </summary>
        [Input("launchSpecifications")]
        public Input<Inputs.InstanceFleetLaunchSpecificationsArgs>? LaunchSpecifications { get; set; }

        /// <summary>
        /// Friendly name given to the instance fleet.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.
        /// </summary>
        [Input("targetOnDemandCapacity")]
        public Input<int>? TargetOnDemandCapacity { get; set; }

        /// <summary>
        /// The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.
        /// </summary>
        [Input("targetSpotCapacity")]
        public Input<int>? TargetSpotCapacity { get; set; }

        public InstanceFleetArgs()
        {
        }
    }

    public sealed class InstanceFleetState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("instanceTypeConfigs")]
        private InputList<Inputs.InstanceFleetInstanceTypeConfigGetArgs>? _instanceTypeConfigs;

        /// <summary>
        /// Configuration block for instance fleet
        /// </summary>
        public InputList<Inputs.InstanceFleetInstanceTypeConfigGetArgs> InstanceTypeConfigs
        {
            get => _instanceTypeConfigs ?? (_instanceTypeConfigs = new InputList<Inputs.InstanceFleetInstanceTypeConfigGetArgs>());
            set => _instanceTypeConfigs = value;
        }

        /// <summary>
        /// Configuration block for launch specification
        /// </summary>
        [Input("launchSpecifications")]
        public Input<Inputs.InstanceFleetLaunchSpecificationsGetArgs>? LaunchSpecifications { get; set; }

        /// <summary>
        /// Friendly name given to the instance fleet.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("provisionedOnDemandCapacity")]
        public Input<int>? ProvisionedOnDemandCapacity { get; set; }

        [Input("provisionedSpotCapacity")]
        public Input<int>? ProvisionedSpotCapacity { get; set; }

        /// <summary>
        /// The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand instances to provision.
        /// </summary>
        [Input("targetOnDemandCapacity")]
        public Input<int>? TargetOnDemandCapacity { get; set; }

        /// <summary>
        /// The target capacity of Spot units for the instance fleet, which determines how many Spot instances to provision.
        /// </summary>
        [Input("targetSpotCapacity")]
        public Input<int>? TargetSpotCapacity { get; set; }

        public InstanceFleetState()
        {
        }
    }
}
