// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Pinpoint
{
    /// <summary>
    /// Provides a Pinpoint APNs Sandbox Channel resource.
    /// 
    /// &gt; **Note:** All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.IO;
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var app = new Aws.Pinpoint.App("app", new Aws.Pinpoint.AppArgs
    ///         {
    ///         });
    ///         var apnsSandbox = new Aws.Pinpoint.ApnsSandboxChannel("apnsSandbox", new Aws.Pinpoint.ApnsSandboxChannelArgs
    ///         {
    ///             ApplicationId = app.ApplicationId,
    ///             Certificate = File.ReadAllText("./certificate.pem"),
    ///             PrivateKey = File.ReadAllText("./private_key.key"),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Pinpoint APNs Sandbox Channel can be imported using the `application-id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import aws:pinpoint/apnsSandboxChannel:ApnsSandboxChannel apns_sandbox application-id
    /// ```
    /// </summary>
    [AwsResourceType("aws:pinpoint/apnsSandboxChannel:ApnsSandboxChannel")]
    public partial class ApnsSandboxChannel : Pulumi.CustomResource
    {
        /// <summary>
        /// The application ID.
        /// </summary>
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        /// <summary>
        /// The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.
        /// </summary>
        [Output("bundleId")]
        public Output<string?> BundleId { get; private set; } = null!;

        /// <summary>
        /// The pem encoded TLS Certificate from Apple.
        /// </summary>
        [Output("certificate")]
        public Output<string?> Certificate { get; private set; } = null!;

        /// <summary>
        /// The default authentication method used for APNs Sandbox.
        /// __NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
        /// You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
        /// If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.
        /// </summary>
        [Output("defaultAuthenticationMethod")]
        public Output<string?> DefaultAuthenticationMethod { get; private set; } = null!;

        /// <summary>
        /// Whether the channel is enabled or disabled. Defaults to `true`.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The Certificate Private Key file (ie. `.key` file).
        /// </summary>
        [Output("privateKey")]
        public Output<string?> PrivateKey { get; private set; } = null!;

        /// <summary>
        /// The ID assigned to your Apple developer account team. This value is provided on the Membership page.
        /// </summary>
        [Output("teamId")]
        public Output<string?> TeamId { get; private set; } = null!;

        /// <summary>
        /// The `.p8` file that you download from your Apple developer account when you create an authentication key.
        /// </summary>
        [Output("tokenKey")]
        public Output<string?> TokenKey { get; private set; } = null!;

        /// <summary>
        /// The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.
        /// </summary>
        [Output("tokenKeyId")]
        public Output<string?> TokenKeyId { get; private set; } = null!;


        /// <summary>
        /// Create a ApnsSandboxChannel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApnsSandboxChannel(string name, ApnsSandboxChannelArgs args, CustomResourceOptions? options = null)
            : base("aws:pinpoint/apnsSandboxChannel:ApnsSandboxChannel", name, args ?? new ApnsSandboxChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApnsSandboxChannel(string name, Input<string> id, ApnsSandboxChannelState? state = null, CustomResourceOptions? options = null)
            : base("aws:pinpoint/apnsSandboxChannel:ApnsSandboxChannel", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApnsSandboxChannel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApnsSandboxChannel Get(string name, Input<string> id, ApnsSandboxChannelState? state = null, CustomResourceOptions? options = null)
        {
            return new ApnsSandboxChannel(name, id, state, options);
        }
    }

    public sealed class ApnsSandboxChannelArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The application ID.
        /// </summary>
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        /// <summary>
        /// The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.
        /// </summary>
        [Input("bundleId")]
        public Input<string>? BundleId { get; set; }

        /// <summary>
        /// The pem encoded TLS Certificate from Apple.
        /// </summary>
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        /// <summary>
        /// The default authentication method used for APNs Sandbox.
        /// __NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
        /// You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
        /// If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.
        /// </summary>
        [Input("defaultAuthenticationMethod")]
        public Input<string>? DefaultAuthenticationMethod { get; set; }

        /// <summary>
        /// Whether the channel is enabled or disabled. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The Certificate Private Key file (ie. `.key` file).
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// The ID assigned to your Apple developer account team. This value is provided on the Membership page.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// The `.p8` file that you download from your Apple developer account when you create an authentication key.
        /// </summary>
        [Input("tokenKey")]
        public Input<string>? TokenKey { get; set; }

        /// <summary>
        /// The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.
        /// </summary>
        [Input("tokenKeyId")]
        public Input<string>? TokenKeyId { get; set; }

        public ApnsSandboxChannelArgs()
        {
        }
    }

    public sealed class ApnsSandboxChannelState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The application ID.
        /// </summary>
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// The ID assigned to your iOS app. To find this value, choose Certificates, IDs &amp; Profiles, choose App IDs in the Identifiers section, and choose your app.
        /// </summary>
        [Input("bundleId")]
        public Input<string>? BundleId { get; set; }

        /// <summary>
        /// The pem encoded TLS Certificate from Apple.
        /// </summary>
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        /// <summary>
        /// The default authentication method used for APNs Sandbox.
        /// __NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
        /// You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
        /// If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.
        /// </summary>
        [Input("defaultAuthenticationMethod")]
        public Input<string>? DefaultAuthenticationMethod { get; set; }

        /// <summary>
        /// Whether the channel is enabled or disabled. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The Certificate Private Key file (ie. `.key` file).
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// The ID assigned to your Apple developer account team. This value is provided on the Membership page.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// The `.p8` file that you download from your Apple developer account when you create an authentication key.
        /// </summary>
        [Input("tokenKey")]
        public Input<string>? TokenKey { get; set; }

        /// <summary>
        /// The ID assigned to your signing key. To find this value, choose Certificates, IDs &amp; Profiles, and choose your key in the Keys section.
        /// </summary>
        [Input("tokenKeyId")]
        public Input<string>? TokenKeyId { get; set; }

        public ApnsSandboxChannelState()
        {
        }
    }
}
