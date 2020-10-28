// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.Aws.Ssm
{
    [EnumType]
    public readonly struct ParameterType : IEquatable<ParameterType>
    {
        private readonly string _value;

        private ParameterType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ParameterType String { get; } = new ParameterType("String");
        public static ParameterType StringList { get; } = new ParameterType("StringList");
        public static ParameterType SecureString { get; } = new ParameterType("SecureString");

        public static bool operator ==(ParameterType left, ParameterType right) => left.Equals(right);
        public static bool operator !=(ParameterType left, ParameterType right) => !left.Equals(right);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ParameterType other && Equals(other);
        public bool Equals(ParameterType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}