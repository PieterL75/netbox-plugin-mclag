from dcim.models import Interface
from dcim.tables.devices import InterfaceTable
from netbox.views.generic import (
    ObjectListView,
    ObjectEditView,
    ObjectDeleteView,
    ObjectView,
    ObjectChildrenView,
    BulkEditView,
    BulkDeleteView,
)
from utilities.views import register_model_view

from netbox_plugin_mclag.models import McDomain, McLag
from netbox_plugin_mclag.forms import McDomainForm, McDomainBulkEditForm, McLagForm, McLagBulkEditForm
from netbox_plugin_mclag.tables import McDomainTable, McLagTable
from netbox_plugin_mclag.filtersets import McDomainFilterSet, McLagFilterSet

@register_model_view(McDomain)
class McDomainView(ObjectView):
    queryset = McDomain.objects.all()
    def get_extra_context(self, request, instance):
        mclag_table = McLagTable(instance.mc_lags.all())
        mclag_table.configure(request)

        return {
            'mclag_table': mclag_table,
        }
@register_model_view(McDomain, name='list')
class McDomainListView(ObjectListView):
    queryset = McDomain.objects.all()
    table = McDomainTable
    filterset = McDomainFilterSet

@register_model_view(McDomain, name='edit')
class McDomainEditView(ObjectEditView):
    queryset = McDomain.objects.all()
    form = McDomainForm

@register_model_view(McDomain, name='bulk_edit')
class McDomainBulkEditView(BulkEditView):
    queryset = McDomain.objects.all()
    table = McDomainTable
    form = McDomainBulkEditForm
    filterset = McDomainFilterSet

@register_model_view(McDomain, name='delete')
class McDomainDeleteView(ObjectDeleteView):
    queryset = McDomain.objects.all()

@register_model_view(McDomain, name='bulk_delete')
class McDomainBulkDeleteView(BulkDeleteView):
    queryset = McDomain.objects.all()
    table = McDomainTable
    filterset = McDomainFilterSet

@register_model_view(McLag)
class McLagView(ObjectView):
    queryset = McLag.objects.all()
    def get_extra_context(self, request, instance):
        lag_interfaces_table = InterfaceTable(instance.interfaces.all())
        lag_interfaces_table.configure(request)

        physical_interfaces_table = InterfaceTable(Interface.objects.filter(lag__mc_lags=instance))
        physical_interfaces_table.configure(request)
        return {
            'lag_interfaces_table': lag_interfaces_table,
            'physical_interfaces_table': physical_interfaces_table,
        }

@register_model_view(McLag, name='list')
class McLagListView(ObjectListView):
    queryset = McLag.objects.all()
    table = McLagTable
    filterset = McLagFilterSet

@register_model_view(McLag, name='edit')
class McLagEditView(ObjectEditView):
    queryset = McLag.objects.all()
    form = McLagForm

@register_model_view(McLag, name='bulk_edit')
class McLagBulkEditView(BulkEditView):
    queryset = McLag.objects.all()
    table = McLagTable
    form = McLagBulkEditForm
    filterset = McLagFilterSet

@register_model_view(McLag, name='delete')
class McLagDeleteView(ObjectDeleteView):
    queryset = McLag.objects.all()

@register_model_view(McLag, name='bulk_delete')
class McLagBulkDeleteView(BulkDeleteView):
    queryset = McLag.objects.all()
    table = McLagTable
    filterset = McLagFilterSet

