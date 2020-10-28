// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.Aws.AutoScaling
{
    /// <summary>
    /// See https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html
    /// </summary>
    [EnumType]
    public readonly struct Metric : IEquatable<Metric>
    {
        private readonly string _value;

        private Metric(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static Metric GroupMinSize { get; } = new Metric("GroupMinSize");
        public static Metric GroupMaxSize { get; } = new Metric("GroupMaxSize");
        public static Metric GroupDesiredCapacity { get; } = new Metric("GroupDesiredCapacity");
        public static Metric GroupInServiceInstances { get; } = new Metric("GroupInServiceInstances");
        public static Metric GroupPendingInstances { get; } = new Metric("GroupPendingInstances");
        public static Metric GroupStandbyInstances { get; } = new Metric("GroupStandbyInstances");
        public static Metric GroupTerminatingInstances { get; } = new Metric("GroupTerminatingInstances");
        public static Metric GroupTotalInstances { get; } = new Metric("GroupTotalInstances");

        public static bool operator ==(Metric left, Metric right) => left.Equals(right);
        public static bool operator !=(Metric left, Metric right) => !left.Equals(right);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is Metric other && Equals(other);
        public bool Equals(Metric other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// See https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnableMetricsCollection.html
    /// </summary>
    [EnumType]
    public readonly struct MetricsGranularity : IEquatable<MetricsGranularity>
    {
        private readonly string _value;

        private MetricsGranularity(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static MetricsGranularity OneMinute { get; } = new MetricsGranularity("1Minute");

        public static bool operator ==(MetricsGranularity left, MetricsGranularity right) => left.Equals(right);
        public static bool operator !=(MetricsGranularity left, MetricsGranularity right) => !left.Equals(right);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is MetricsGranularity other && Equals(other);
        public bool Equals(MetricsGranularity other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// See https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_NotificationConfiguration.html
    /// </summary>
    [EnumType]
    public readonly struct NotificationType : IEquatable<NotificationType>
    {
        private readonly string _value;

        private NotificationType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static NotificationType InstanceLaunch { get; } = new NotificationType("autoscaling:EC2_INSTANCE_LAUNCH");
        public static NotificationType InstanceTerminate { get; } = new NotificationType("autoscaling:EC2_INSTANCE_TERMINATE");
        public static NotificationType InstanceLaunchError { get; } = new NotificationType("autoscaling:EC2_INSTANCE_LAUNCH_ERROR");
        public static NotificationType InstanceTerminateError { get; } = new NotificationType("autoscaling:EC2_INSTANCE_TERMINATE_ERROR");
        public static NotificationType TestNotification { get; } = new NotificationType("autoscaling:TEST_NOTIFICATION");

        public static bool operator ==(NotificationType left, NotificationType right) => left.Equals(right);
        public static bool operator !=(NotificationType left, NotificationType right) => !left.Equals(right);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is NotificationType other && Equals(other);
        public bool Equals(NotificationType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
