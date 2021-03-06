// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package imagebuilder

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "aws:imagebuilder/component:Component":
		r, err = NewComponent(ctx, name, nil, pulumi.URN_(urn))
	case "aws:imagebuilder/distributionConfiguration:DistributionConfiguration":
		r, err = NewDistributionConfiguration(ctx, name, nil, pulumi.URN_(urn))
	case "aws:imagebuilder/image:Image":
		r, err = NewImage(ctx, name, nil, pulumi.URN_(urn))
	case "aws:imagebuilder/imagePipeline:ImagePipeline":
		r, err = NewImagePipeline(ctx, name, nil, pulumi.URN_(urn))
	case "aws:imagebuilder/imageRecipe:ImageRecipe":
		r, err = NewImageRecipe(ctx, name, nil, pulumi.URN_(urn))
	case "aws:imagebuilder/infrastructureConfiguration:InfrastructureConfiguration":
		r, err = NewInfrastructureConfiguration(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := aws.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"aws",
		"imagebuilder/component",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"imagebuilder/distributionConfiguration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"imagebuilder/image",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"imagebuilder/imagePipeline",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"imagebuilder/imageRecipe",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"aws",
		"imagebuilder/infrastructureConfiguration",
		&module{version},
	)
}
