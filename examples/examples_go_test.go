// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.
// +build go all

package examples

import (
	"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v2/testing/integration"
)

func TestAccWebserverGo(t *testing.T) {
	t.Skip("Chicken and egg wile creating this new major version")
	skipIfShort(t)
	test := integration.ProgramTestOptions{
		Dir: path.Join(getCwd(t), "webserver-go"),
		Dependencies: []string{
			"github.com/pulumi/pulumi-aws/sdk/go/v2",
		},
		Config: map[string]string{"aws:region": getEnvRegion(t)},
	}

	integration.ProgramTest(t, &test)
}
