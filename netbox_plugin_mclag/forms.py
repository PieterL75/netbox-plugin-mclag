from django import forms

from dcim.models import Interface, Device
from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm
from utilities.forms.fields import DynamicModelMultipleChoiceField, DynamicModelChoiceField, CommentField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import APISelectMultiple

from netbox_plugin_mclag.models import McDomain, McLag
from netbox_plugin_mclag.util import get_interface_label

class McDomainForm(NetBoxModelForm):
    class Meta:
        model = McDomain
        fields = ('name', 'domain_id', 'description', 'devices', 'tags')

class McDomainBulkEditForm(NetBoxModelBulkEditForm):
    domain_id = forms.CharField(
        required=False,
    )
    devices = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )

    model = McDomain
    nullable_fields = ('description', 'tags',)
    fields = ('domain_id', 'devices', 'description', 'tags')
    field_order = ('domain_id', 'devices', 'description', 'tags')
    fieldsets = (
        FieldSet('domain_id', 'devices', 'description', name='Multi-Chassis Domain Group'),
    )

class McInterfaceMultipleChoiceField(DynamicModelMultipleChoiceField):
    def label_from_instance(self, interface):
        return get_interface_label(interface)

class McLagForm(NetBoxModelForm):
    interfaces = McInterfaceMultipleChoiceField(
        queryset = Interface.objects.filter(type='lag'),
        selector = True,
        query_params = {
            'mc_domain': '$mc_domain',
            'brief': 'false'
        },
        widget=APISelectMultiple(
            api_url='/api/plugins/mclag/interfaces/'
        )
    )
    class Meta:
        model = McLag
        fields = ('name', 'mc_domain', 'type', 'lag_id', 'interfaces', 'description', 'tags')

class McLagBulkEditForm(NetBoxModelBulkEditForm):
    type = forms.ChoiceField(
        choices=[('', '---------'),] + McLag._meta.get_field('type').choices,
        required=False,
        initial=''
    )
    lag_id = forms.CharField(
        required=False,
    )
    mc_domain = DynamicModelChoiceField(
        queryset=McDomain.objects.all(),
        required=False,
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )

    model = McLag
    nullable_fields = ('description', 'tags',)
    fields = ('name', 'mc_domain', 'type', 'lag_id', 'interfaces', 'description', 'tags')
    field_order = ('mc_domain', 'type', 'lag_id', 'description', 'tags')
    fieldsets = (
        FieldSet('type', 'mc_domain', 'description', name='Multi-Chassis Link Aggregation Group'),
    )
