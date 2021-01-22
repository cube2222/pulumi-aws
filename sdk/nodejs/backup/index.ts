// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./getPlan";
export * from "./getSelection";
export * from "./getVault";
export * from "./globalSettings";
export * from "./plan";
export * from "./regionSettings";
export * from "./selection";
export * from "./vault";
export * from "./vaultNotifications";
export * from "./vaultPolicy";

// Import resources to register:
import { GlobalSettings } from "./globalSettings";
import { Plan } from "./plan";
import { RegionSettings } from "./regionSettings";
import { Selection } from "./selection";
import { Vault } from "./vault";
import { VaultNotifications } from "./vaultNotifications";
import { VaultPolicy } from "./vaultPolicy";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws:backup/globalSettings:GlobalSettings":
                return new GlobalSettings(name, <any>undefined, { urn })
            case "aws:backup/plan:Plan":
                return new Plan(name, <any>undefined, { urn })
            case "aws:backup/regionSettings:RegionSettings":
                return new RegionSettings(name, <any>undefined, { urn })
            case "aws:backup/selection:Selection":
                return new Selection(name, <any>undefined, { urn })
            case "aws:backup/vault:Vault":
                return new Vault(name, <any>undefined, { urn })
            case "aws:backup/vaultNotifications:VaultNotifications":
                return new VaultNotifications(name, <any>undefined, { urn })
            case "aws:backup/vaultPolicy:VaultPolicy":
                return new VaultPolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws", "backup/globalSettings", _module)
pulumi.runtime.registerResourceModule("aws", "backup/plan", _module)
pulumi.runtime.registerResourceModule("aws", "backup/regionSettings", _module)
pulumi.runtime.registerResourceModule("aws", "backup/selection", _module)
pulumi.runtime.registerResourceModule("aws", "backup/vault", _module)
pulumi.runtime.registerResourceModule("aws", "backup/vaultNotifications", _module)
pulumi.runtime.registerResourceModule("aws", "backup/vaultPolicy", _module)
