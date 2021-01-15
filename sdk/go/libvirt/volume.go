// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package libvirt

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type Volume struct {
	pulumi.CustomResourceState

	BaseVolumeId   pulumi.StringPtrOutput `pulumi:"baseVolumeId"`
	BaseVolumeName pulumi.StringPtrOutput `pulumi:"baseVolumeName"`
	BaseVolumePool pulumi.StringPtrOutput `pulumi:"baseVolumePool"`
	Format         pulumi.StringOutput    `pulumi:"format"`
	Name           pulumi.StringOutput    `pulumi:"name"`
	Pool           pulumi.StringPtrOutput `pulumi:"pool"`
	Size           pulumi.IntOutput       `pulumi:"size"`
	Source         pulumi.StringPtrOutput `pulumi:"source"`
	Xml            VolumeXmlPtrOutput     `pulumi:"xml"`
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOption) (*Volume, error) {
	if args == nil {
		args = &VolumeArgs{}
	}
	var resource Volume
	err := ctx.RegisterResource("libvirt:index/volume:Volume", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolume gets an existing Volume resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolume(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeState, opts ...pulumi.ResourceOption) (*Volume, error) {
	var resource Volume
	err := ctx.ReadResource("libvirt:index/volume:Volume", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Volume resources.
type volumeState struct {
	BaseVolumeId   *string    `pulumi:"baseVolumeId"`
	BaseVolumeName *string    `pulumi:"baseVolumeName"`
	BaseVolumePool *string    `pulumi:"baseVolumePool"`
	Format         *string    `pulumi:"format"`
	Name           *string    `pulumi:"name"`
	Pool           *string    `pulumi:"pool"`
	Size           *int       `pulumi:"size"`
	Source         *string    `pulumi:"source"`
	Xml            *VolumeXml `pulumi:"xml"`
}

type VolumeState struct {
	BaseVolumeId   pulumi.StringPtrInput
	BaseVolumeName pulumi.StringPtrInput
	BaseVolumePool pulumi.StringPtrInput
	Format         pulumi.StringPtrInput
	Name           pulumi.StringPtrInput
	Pool           pulumi.StringPtrInput
	Size           pulumi.IntPtrInput
	Source         pulumi.StringPtrInput
	Xml            VolumeXmlPtrInput
}

func (VolumeState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeState)(nil)).Elem()
}

type volumeArgs struct {
	BaseVolumeId   *string    `pulumi:"baseVolumeId"`
	BaseVolumeName *string    `pulumi:"baseVolumeName"`
	BaseVolumePool *string    `pulumi:"baseVolumePool"`
	Format         *string    `pulumi:"format"`
	Name           *string    `pulumi:"name"`
	Pool           *string    `pulumi:"pool"`
	Size           *int       `pulumi:"size"`
	Source         *string    `pulumi:"source"`
	Xml            *VolumeXml `pulumi:"xml"`
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	BaseVolumeId   pulumi.StringPtrInput
	BaseVolumeName pulumi.StringPtrInput
	BaseVolumePool pulumi.StringPtrInput
	Format         pulumi.StringPtrInput
	Name           pulumi.StringPtrInput
	Pool           pulumi.StringPtrInput
	Size           pulumi.IntPtrInput
	Source         pulumi.StringPtrInput
	Xml            VolumeXmlPtrInput
}

func (VolumeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeArgs)(nil)).Elem()
}