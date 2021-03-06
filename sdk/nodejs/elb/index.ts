// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./appCookieStickinessPolicy";
export * from "./attachment";
export * from "./getHostedZoneId";
export * from "./getLoadBalancer";
export * from "./getServiceAccount";
export * from "./listenerPolicy";
export * from "./loadBalancer";
export * from "./loadBalancerBackendServerPolicy";
export * from "./loadBalancerCookieStickinessPolicy";
export * from "./loadBalancerPolicy";
export * from "./sslNegotiationPolicy";

// Import resources to register:
import { AppCookieStickinessPolicy } from "./appCookieStickinessPolicy";
import { Attachment } from "./attachment";
import { ListenerPolicy } from "./listenerPolicy";
import { LoadBalancer } from "./loadBalancer";
import { LoadBalancerBackendServerPolicy } from "./loadBalancerBackendServerPolicy";
import { LoadBalancerCookieStickinessPolicy } from "./loadBalancerCookieStickinessPolicy";
import { LoadBalancerPolicy } from "./loadBalancerPolicy";
import { SslNegotiationPolicy } from "./sslNegotiationPolicy";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws:elb/appCookieStickinessPolicy:AppCookieStickinessPolicy":
                return new AppCookieStickinessPolicy(name, <any>undefined, { urn })
            case "aws:elb/attachment:Attachment":
                return new Attachment(name, <any>undefined, { urn })
            case "aws:elb/listenerPolicy:ListenerPolicy":
                return new ListenerPolicy(name, <any>undefined, { urn })
            case "aws:elb/loadBalancer:LoadBalancer":
                return new LoadBalancer(name, <any>undefined, { urn })
            case "aws:elb/loadBalancerBackendServerPolicy:LoadBalancerBackendServerPolicy":
                return new LoadBalancerBackendServerPolicy(name, <any>undefined, { urn })
            case "aws:elb/loadBalancerCookieStickinessPolicy:LoadBalancerCookieStickinessPolicy":
                return new LoadBalancerCookieStickinessPolicy(name, <any>undefined, { urn })
            case "aws:elb/loadBalancerPolicy:LoadBalancerPolicy":
                return new LoadBalancerPolicy(name, <any>undefined, { urn })
            case "aws:elb/sslNegotiationPolicy:SslNegotiationPolicy":
                return new SslNegotiationPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws", "elb/appCookieStickinessPolicy", _module)
pulumi.runtime.registerResourceModule("aws", "elb/attachment", _module)
pulumi.runtime.registerResourceModule("aws", "elb/listenerPolicy", _module)
pulumi.runtime.registerResourceModule("aws", "elb/loadBalancer", _module)
pulumi.runtime.registerResourceModule("aws", "elb/loadBalancerBackendServerPolicy", _module)
pulumi.runtime.registerResourceModule("aws", "elb/loadBalancerCookieStickinessPolicy", _module)
pulumi.runtime.registerResourceModule("aws", "elb/loadBalancerPolicy", _module)
pulumi.runtime.registerResourceModule("aws", "elb/sslNegotiationPolicy", _module)
