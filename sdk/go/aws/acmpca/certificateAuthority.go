// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package acmpca

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage AWS Certificate Manager Private Certificate Authorities (ACM PCA Certificate Authorities).
//
// > **NOTE:** Creating this resource will leave the certificate authority in a `PENDING_CERTIFICATE` status, which means it cannot yet issue certificates. To complete this setup, you must fully sign the certificate authority CSR available in the `certificateSigningRequest` attribute and import the signed certificate using the AWS SDK, CLI or Console. This provider can support another resource to manage that workflow automatically in the future.
//
// ## Example Usage
// ### Basic
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/acmpca"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := acmpca.NewCertificateAuthority(ctx, "example", &acmpca.CertificateAuthorityArgs{
// 			CertificateAuthorityConfiguration: &acmpca.CertificateAuthorityCertificateAuthorityConfigurationArgs{
// 				KeyAlgorithm:     pulumi.String("RSA_4096"),
// 				SigningAlgorithm: pulumi.String("SHA512WITHRSA"),
// 				Subject: &acmpca.CertificateAuthorityCertificateAuthorityConfigurationSubjectArgs{
// 					CommonName: pulumi.String("example.com"),
// 				},
// 			},
// 			PermanentDeletionTimeInDays: pulumi.Int(7),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Enable Certificate Revocation List
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/acmpca"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleBucket, err := s3.NewBucket(ctx, "exampleBucket", nil)
// 		if err != nil {
// 			return err
// 		}
// 		exampleBucketPolicy, err := s3.NewBucketPolicy(ctx, "exampleBucketPolicy", &s3.BucketPolicyArgs{
// 			Bucket: exampleBucket.ID(),
// 			Policy: acmpcaBucketAccess.ApplyT(func(acmpcaBucketAccess iam.GetPolicyDocumentResult) (string, error) {
// 				return acmpcaBucketAccess.Json, nil
// 			}).(pulumi.StringOutput),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = acmpca.NewCertificateAuthority(ctx, "exampleCertificateAuthority", &acmpca.CertificateAuthorityArgs{
// 			CertificateAuthorityConfiguration: &acmpca.CertificateAuthorityCertificateAuthorityConfigurationArgs{
// 				KeyAlgorithm:     pulumi.String("RSA_4096"),
// 				SigningAlgorithm: pulumi.String("SHA512WITHRSA"),
// 				Subject: &acmpca.CertificateAuthorityCertificateAuthorityConfigurationSubjectArgs{
// 					CommonName: pulumi.String("example.com"),
// 				},
// 			},
// 			RevocationConfiguration: &acmpca.CertificateAuthorityRevocationConfigurationArgs{
// 				CrlConfiguration: &acmpca.CertificateAuthorityRevocationConfigurationCrlConfigurationArgs{
// 					CustomCname:      pulumi.String("crl.example.com"),
// 					Enabled:          pulumi.Bool(true),
// 					ExpirationInDays: pulumi.Int(7),
// 					S3BucketName:     exampleBucket.ID(),
// 				},
// 			},
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			exampleBucketPolicy,
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// `aws_acmpca_certificate_authority` can be imported by using the certificate authority Amazon Resource Name (ARN), e.g.
//
// ```sh
//  $ pulumi import aws:acmpca/certificateAuthority:CertificateAuthority example arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012
// ```
type CertificateAuthority struct {
	pulumi.CustomResourceState

	// Amazon Resource Name (ARN) of the certificate authority.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.
	Certificate pulumi.StringOutput `pulumi:"certificate"`
	// Nested argument containing algorithms and certificate subject information. Defined below.
	CertificateAuthorityConfiguration CertificateAuthorityCertificateAuthorityConfigurationOutput `pulumi:"certificateAuthorityConfiguration"`
	// Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.
	CertificateChain pulumi.StringOutput `pulumi:"certificateChain"`
	// The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
	CertificateSigningRequest pulumi.StringOutput `pulumi:"certificateSigningRequest"`
	// Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.
	NotAfter pulumi.StringOutput `pulumi:"notAfter"`
	// Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.
	NotBefore pulumi.StringOutput `pulumi:"notBefore"`
	// The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.
	PermanentDeletionTimeInDays pulumi.IntPtrOutput `pulumi:"permanentDeletionTimeInDays"`
	// Nested argument containing revocation configuration. Defined below.
	RevocationConfiguration CertificateAuthorityRevocationConfigurationPtrOutput `pulumi:"revocationConfiguration"`
	// Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.
	Serial pulumi.StringOutput `pulumi:"serial"`
	// Status of the certificate authority.
	Status pulumi.StringOutput `pulumi:"status"`
	// Specifies a key-value map of user-defined tags that are attached to the certificate authority.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The type of the certificate authority. Defaults to `SUBORDINATE`. Valid values: `ROOT` and `SUBORDINATE`.
	Type pulumi.StringPtrOutput `pulumi:"type"`
}

// NewCertificateAuthority registers a new resource with the given unique name, arguments, and options.
func NewCertificateAuthority(ctx *pulumi.Context,
	name string, args *CertificateAuthorityArgs, opts ...pulumi.ResourceOption) (*CertificateAuthority, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CertificateAuthorityConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'CertificateAuthorityConfiguration'")
	}
	var resource CertificateAuthority
	err := ctx.RegisterResource("aws:acmpca/certificateAuthority:CertificateAuthority", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCertificateAuthority gets an existing CertificateAuthority resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCertificateAuthority(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CertificateAuthorityState, opts ...pulumi.ResourceOption) (*CertificateAuthority, error) {
	var resource CertificateAuthority
	err := ctx.ReadResource("aws:acmpca/certificateAuthority:CertificateAuthority", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CertificateAuthority resources.
type certificateAuthorityState struct {
	// Amazon Resource Name (ARN) of the certificate authority.
	Arn *string `pulumi:"arn"`
	// Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.
	Certificate *string `pulumi:"certificate"`
	// Nested argument containing algorithms and certificate subject information. Defined below.
	CertificateAuthorityConfiguration *CertificateAuthorityCertificateAuthorityConfiguration `pulumi:"certificateAuthorityConfiguration"`
	// Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.
	CertificateChain *string `pulumi:"certificateChain"`
	// The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
	CertificateSigningRequest *string `pulumi:"certificateSigningRequest"`
	// Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.
	Enabled *bool `pulumi:"enabled"`
	// Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.
	NotAfter *string `pulumi:"notAfter"`
	// Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.
	NotBefore *string `pulumi:"notBefore"`
	// The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.
	PermanentDeletionTimeInDays *int `pulumi:"permanentDeletionTimeInDays"`
	// Nested argument containing revocation configuration. Defined below.
	RevocationConfiguration *CertificateAuthorityRevocationConfiguration `pulumi:"revocationConfiguration"`
	// Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.
	Serial *string `pulumi:"serial"`
	// Status of the certificate authority.
	Status *string `pulumi:"status"`
	// Specifies a key-value map of user-defined tags that are attached to the certificate authority.
	Tags map[string]string `pulumi:"tags"`
	// The type of the certificate authority. Defaults to `SUBORDINATE`. Valid values: `ROOT` and `SUBORDINATE`.
	Type *string `pulumi:"type"`
}

type CertificateAuthorityState struct {
	// Amazon Resource Name (ARN) of the certificate authority.
	Arn pulumi.StringPtrInput
	// Base64-encoded certificate authority (CA) certificate. Only available after the certificate authority certificate has been imported.
	Certificate pulumi.StringPtrInput
	// Nested argument containing algorithms and certificate subject information. Defined below.
	CertificateAuthorityConfiguration CertificateAuthorityCertificateAuthorityConfigurationPtrInput
	// Base64-encoded certificate chain that includes any intermediate certificates and chains up to root on-premises certificate that you used to sign your private CA certificate. The chain does not include your private CA certificate. Only available after the certificate authority certificate has been imported.
	CertificateChain pulumi.StringPtrInput
	// The base64 PEM-encoded certificate signing request (CSR) for your private CA certificate.
	CertificateSigningRequest pulumi.StringPtrInput
	// Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.
	Enabled pulumi.BoolPtrInput
	// Date and time after which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.
	NotAfter pulumi.StringPtrInput
	// Date and time before which the certificate authority is not valid. Only available after the certificate authority certificate has been imported.
	NotBefore pulumi.StringPtrInput
	// The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.
	PermanentDeletionTimeInDays pulumi.IntPtrInput
	// Nested argument containing revocation configuration. Defined below.
	RevocationConfiguration CertificateAuthorityRevocationConfigurationPtrInput
	// Serial number of the certificate authority. Only available after the certificate authority certificate has been imported.
	Serial pulumi.StringPtrInput
	// Status of the certificate authority.
	Status pulumi.StringPtrInput
	// Specifies a key-value map of user-defined tags that are attached to the certificate authority.
	Tags pulumi.StringMapInput
	// The type of the certificate authority. Defaults to `SUBORDINATE`. Valid values: `ROOT` and `SUBORDINATE`.
	Type pulumi.StringPtrInput
}

func (CertificateAuthorityState) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateAuthorityState)(nil)).Elem()
}

type certificateAuthorityArgs struct {
	// Nested argument containing algorithms and certificate subject information. Defined below.
	CertificateAuthorityConfiguration CertificateAuthorityCertificateAuthorityConfiguration `pulumi:"certificateAuthorityConfiguration"`
	// Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.
	Enabled *bool `pulumi:"enabled"`
	// The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.
	PermanentDeletionTimeInDays *int `pulumi:"permanentDeletionTimeInDays"`
	// Nested argument containing revocation configuration. Defined below.
	RevocationConfiguration *CertificateAuthorityRevocationConfiguration `pulumi:"revocationConfiguration"`
	// Specifies a key-value map of user-defined tags that are attached to the certificate authority.
	Tags map[string]string `pulumi:"tags"`
	// The type of the certificate authority. Defaults to `SUBORDINATE`. Valid values: `ROOT` and `SUBORDINATE`.
	Type *string `pulumi:"type"`
}

// The set of arguments for constructing a CertificateAuthority resource.
type CertificateAuthorityArgs struct {
	// Nested argument containing algorithms and certificate subject information. Defined below.
	CertificateAuthorityConfiguration CertificateAuthorityCertificateAuthorityConfigurationInput
	// Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. Defaults to `false`.
	Enabled pulumi.BoolPtrInput
	// The number of days to make a CA restorable after it has been deleted, must be between 7 to 30 days, with default to 30 days.
	PermanentDeletionTimeInDays pulumi.IntPtrInput
	// Nested argument containing revocation configuration. Defined below.
	RevocationConfiguration CertificateAuthorityRevocationConfigurationPtrInput
	// Specifies a key-value map of user-defined tags that are attached to the certificate authority.
	Tags pulumi.StringMapInput
	// The type of the certificate authority. Defaults to `SUBORDINATE`. Valid values: `ROOT` and `SUBORDINATE`.
	Type pulumi.StringPtrInput
}

func (CertificateAuthorityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateAuthorityArgs)(nil)).Elem()
}

type CertificateAuthorityInput interface {
	pulumi.Input

	ToCertificateAuthorityOutput() CertificateAuthorityOutput
	ToCertificateAuthorityOutputWithContext(ctx context.Context) CertificateAuthorityOutput
}

func (CertificateAuthority) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateAuthority)(nil)).Elem()
}

func (i CertificateAuthority) ToCertificateAuthorityOutput() CertificateAuthorityOutput {
	return i.ToCertificateAuthorityOutputWithContext(context.Background())
}

func (i CertificateAuthority) ToCertificateAuthorityOutputWithContext(ctx context.Context) CertificateAuthorityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateAuthorityOutput)
}

type CertificateAuthorityOutput struct {
	*pulumi.OutputState
}

func (CertificateAuthorityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CertificateAuthorityOutput)(nil)).Elem()
}

func (o CertificateAuthorityOutput) ToCertificateAuthorityOutput() CertificateAuthorityOutput {
	return o
}

func (o CertificateAuthorityOutput) ToCertificateAuthorityOutputWithContext(ctx context.Context) CertificateAuthorityOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CertificateAuthorityOutput{})
}
