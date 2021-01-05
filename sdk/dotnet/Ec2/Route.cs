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
    /// Provides a resource to create a routing table entry (a route) in a VPC routing table.
    /// 
    /// &gt; **NOTE on Route Tables and Routes:** This provider currently
    /// provides both a standalone Route resource and a Route Table resource with routes
    /// defined in-line. At this time you cannot use a Route Table with in-line routes
    /// in conjunction with any Route resources. Doing so will cause
    /// a conflict of rule settings and will overwrite rules.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var route = new Aws.Ec2.Route("route", new Aws.Ec2.RouteArgs
    ///         {
    ///             RouteTableId = "rtb-4fbb3ac4",
    ///             DestinationCidrBlock = "10.0.1.0/22",
    ///             VpcPeeringConnectionId = "pcx-45ff3dc1",
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 aws_route_table.Testing,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Example IPv6 Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs
    ///         {
    ///             CidrBlock = "10.1.0.0/16",
    ///             AssignGeneratedIpv6CidrBlock = true,
    ///         });
    ///         var egress = new Aws.Ec2.EgressOnlyInternetGateway("egress", new Aws.Ec2.EgressOnlyInternetGatewayArgs
    ///         {
    ///             VpcId = vpc.Id,
    ///         });
    ///         var route = new Aws.Ec2.Route("route", new Aws.Ec2.RouteArgs
    ///         {
    ///             RouteTableId = "rtb-4fbb3ac4",
    ///             DestinationIpv6CidrBlock = "::/0",
    ///             EgressOnlyGatewayId = egress.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Individual routes can be imported using `ROUTETABLEID_DESTINATION`. For example, import a route in route table `rtb-656C65616E6F72` with an IPv4 destination CIDR of `10.42.0.0/16` like thisconsole
    /// 
    /// ```sh
    ///  $ pulumi import aws:ec2/route:Route my_route rtb-656C65616E6F72_10.42.0.0/16
    /// ```
    /// 
    ///  Import a route in route table `rtb-656C65616E6F72` with an IPv6 destination CIDR of `2620:0:2d0:200::8/125` similarlyconsole
    /// 
    /// ```sh
    ///  $ pulumi import aws:ec2/route:Route my_route rtb-656C65616E6F72_2620:0:2d0:200::8/125
    /// ```
    /// </summary>
    [AwsResourceType("aws:ec2/route:Route")]
    public partial class Route : Pulumi.CustomResource
    {
        /// <summary>
        /// The destination CIDR block.
        /// </summary>
        [Output("destinationCidrBlock")]
        public Output<string?> DestinationCidrBlock { get; private set; } = null!;

        /// <summary>
        /// The destination IPv6 CIDR block.
        /// </summary>
        [Output("destinationIpv6CidrBlock")]
        public Output<string?> DestinationIpv6CidrBlock { get; private set; } = null!;

        [Output("destinationPrefixListId")]
        public Output<string> DestinationPrefixListId { get; private set; } = null!;

        /// <summary>
        /// Identifier of a VPC Egress Only Internet Gateway.
        /// </summary>
        [Output("egressOnlyGatewayId")]
        public Output<string> EgressOnlyGatewayId { get; private set; } = null!;

        /// <summary>
        /// Identifier of a VPC internet gateway or a virtual private gateway.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// Identifier of an EC2 instance.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        [Output("instanceOwnerId")]
        public Output<string> InstanceOwnerId { get; private set; } = null!;

        /// <summary>
        /// Identifier of a Outpost local gateway.
        /// </summary>
        [Output("localGatewayId")]
        public Output<string> LocalGatewayId { get; private set; } = null!;

        /// <summary>
        /// Identifier of a VPC NAT gateway.
        /// </summary>
        [Output("natGatewayId")]
        public Output<string> NatGatewayId { get; private set; } = null!;

        /// <summary>
        /// Identifier of an EC2 network interface.
        /// </summary>
        [Output("networkInterfaceId")]
        public Output<string> NetworkInterfaceId { get; private set; } = null!;

        [Output("origin")]
        public Output<string> Origin { get; private set; } = null!;

        /// <summary>
        /// The ID of the routing table.
        /// </summary>
        [Output("routeTableId")]
        public Output<string> RouteTableId { get; private set; } = null!;

        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Identifier of an EC2 Transit Gateway.
        /// </summary>
        [Output("transitGatewayId")]
        public Output<string?> TransitGatewayId { get; private set; } = null!;

        /// <summary>
        /// Identifier of a VPC Endpoint.
        /// </summary>
        [Output("vpcEndpointId")]
        public Output<string?> VpcEndpointId { get; private set; } = null!;

        /// <summary>
        /// Identifier of a VPC peering connection.
        /// </summary>
        [Output("vpcPeeringConnectionId")]
        public Output<string?> VpcPeeringConnectionId { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/route:Route", name, args ?? new RouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, RouteState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/route:Route", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, RouteState? state = null, CustomResourceOptions? options = null)
        {
            return new Route(name, id, state, options);
        }
    }

    public sealed class RouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The destination CIDR block.
        /// </summary>
        [Input("destinationCidrBlock")]
        public Input<string>? DestinationCidrBlock { get; set; }

        /// <summary>
        /// The destination IPv6 CIDR block.
        /// </summary>
        [Input("destinationIpv6CidrBlock")]
        public Input<string>? DestinationIpv6CidrBlock { get; set; }

        /// <summary>
        /// Identifier of a VPC Egress Only Internet Gateway.
        /// </summary>
        [Input("egressOnlyGatewayId")]
        public Input<string>? EgressOnlyGatewayId { get; set; }

        /// <summary>
        /// Identifier of a VPC internet gateway or a virtual private gateway.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// Identifier of an EC2 instance.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// Identifier of a Outpost local gateway.
        /// </summary>
        [Input("localGatewayId")]
        public Input<string>? LocalGatewayId { get; set; }

        /// <summary>
        /// Identifier of a VPC NAT gateway.
        /// </summary>
        [Input("natGatewayId")]
        public Input<string>? NatGatewayId { get; set; }

        /// <summary>
        /// Identifier of an EC2 network interface.
        /// </summary>
        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        /// <summary>
        /// The ID of the routing table.
        /// </summary>
        [Input("routeTableId", required: true)]
        public Input<string> RouteTableId { get; set; } = null!;

        /// <summary>
        /// Identifier of an EC2 Transit Gateway.
        /// </summary>
        [Input("transitGatewayId")]
        public Input<string>? TransitGatewayId { get; set; }

        /// <summary>
        /// Identifier of a VPC Endpoint.
        /// </summary>
        [Input("vpcEndpointId")]
        public Input<string>? VpcEndpointId { get; set; }

        /// <summary>
        /// Identifier of a VPC peering connection.
        /// </summary>
        [Input("vpcPeeringConnectionId")]
        public Input<string>? VpcPeeringConnectionId { get; set; }

        public RouteArgs()
        {
        }
    }

    public sealed class RouteState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The destination CIDR block.
        /// </summary>
        [Input("destinationCidrBlock")]
        public Input<string>? DestinationCidrBlock { get; set; }

        /// <summary>
        /// The destination IPv6 CIDR block.
        /// </summary>
        [Input("destinationIpv6CidrBlock")]
        public Input<string>? DestinationIpv6CidrBlock { get; set; }

        [Input("destinationPrefixListId")]
        public Input<string>? DestinationPrefixListId { get; set; }

        /// <summary>
        /// Identifier of a VPC Egress Only Internet Gateway.
        /// </summary>
        [Input("egressOnlyGatewayId")]
        public Input<string>? EgressOnlyGatewayId { get; set; }

        /// <summary>
        /// Identifier of a VPC internet gateway or a virtual private gateway.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        /// <summary>
        /// Identifier of an EC2 instance.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        [Input("instanceOwnerId")]
        public Input<string>? InstanceOwnerId { get; set; }

        /// <summary>
        /// Identifier of a Outpost local gateway.
        /// </summary>
        [Input("localGatewayId")]
        public Input<string>? LocalGatewayId { get; set; }

        /// <summary>
        /// Identifier of a VPC NAT gateway.
        /// </summary>
        [Input("natGatewayId")]
        public Input<string>? NatGatewayId { get; set; }

        /// <summary>
        /// Identifier of an EC2 network interface.
        /// </summary>
        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        [Input("origin")]
        public Input<string>? Origin { get; set; }

        /// <summary>
        /// The ID of the routing table.
        /// </summary>
        [Input("routeTableId")]
        public Input<string>? RouteTableId { get; set; }

        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// Identifier of an EC2 Transit Gateway.
        /// </summary>
        [Input("transitGatewayId")]
        public Input<string>? TransitGatewayId { get; set; }

        /// <summary>
        /// Identifier of a VPC Endpoint.
        /// </summary>
        [Input("vpcEndpointId")]
        public Input<string>? VpcEndpointId { get; set; }

        /// <summary>
        /// Identifier of a VPC peering connection.
        /// </summary>
        [Input("vpcPeeringConnectionId")]
        public Input<string>? VpcPeeringConnectionId { get; set; }

        public RouteState()
        {
        }
    }
}
