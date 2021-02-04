// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const Runtime = {
    DotnetCore2d1: "dotnetcore2.1",
    DotnetCore3d1: "dotnetcore3.1",
    Go1dx: "go1.x",
    Java8: "java8",
    Java8AL2: "java8.al2",
    Java11: "java11",
    Ruby2d5: "ruby2.5",
    Ruby2d7: "ruby2.7",
    NodeJS10dX: "nodejs10.x",
    NodeJS12dX: "nodejs12.x",
    NodeJS14dX: "nodejs14.x",
    Python2d7: "python2.7",
    Python3d6: "python3.6",
    Python3d7: "python3.7",
    Python3d8: "python3.8",
    Custom: "provided",
    CustomAL2: "provided.al2",
} as const;

/**
 * See https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
 */
export type Runtime = (typeof Runtime)[keyof typeof Runtime];
