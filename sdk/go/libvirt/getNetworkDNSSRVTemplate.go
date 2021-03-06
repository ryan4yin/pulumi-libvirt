// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package libvirt

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func GetNetworkDNSSRVTemplate(ctx *pulumi.Context, args *GetNetworkDNSSRVTemplateArgs, opts ...pulumi.InvokeOption) (*GetNetworkDNSSRVTemplateResult, error) {
	var rv GetNetworkDNSSRVTemplateResult
	err := ctx.Invoke("libvirt:index/getNetworkDNSSRVTemplate:getNetworkDNSSRVTemplate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetworkDNSSRVTemplate.
type GetNetworkDNSSRVTemplateArgs struct {
	Domain   *string `pulumi:"domain"`
	Port     *string `pulumi:"port"`
	Priority *string `pulumi:"priority"`
	Protocol string  `pulumi:"protocol"`
	Service  string  `pulumi:"service"`
	Target   *string `pulumi:"target"`
	Weight   *string `pulumi:"weight"`
}

// A collection of values returned by getNetworkDNSSRVTemplate.
type GetNetworkDNSSRVTemplateResult struct {
	Domain *string `pulumi:"domain"`
	// The provider-assigned unique ID for this managed resource.
	Id       string                 `pulumi:"id"`
	Port     *string                `pulumi:"port"`
	Priority *string                `pulumi:"priority"`
	Protocol string                 `pulumi:"protocol"`
	Rendered map[string]interface{} `pulumi:"rendered"`
	Service  string                 `pulumi:"service"`
	Target   *string                `pulumi:"target"`
	Weight   *string                `pulumi:"weight"`
}
