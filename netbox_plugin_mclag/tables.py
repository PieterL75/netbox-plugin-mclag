from django.utils.translation import gettext_lazy as _
import django_tables2 as tables

from dcim.tables import DeviceInterfaceTable
from netbox.tables import NetBoxTable, columns
from utilities.tables import register_table_column

from netbox_plugin_mclag.models import McDomain, McLag

class McDomainTable(NetBoxTable):
    name = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = McDomain
        fields = ('pk', 'id', 'name', 'domain_id', 'description', 'actions')
        default_columns = ('name', 'domain_id')

class McLagTable(NetBoxTable):
    name = tables.Column(linkify=True)
    mc_domain = tables.Column(linkify=True)
    type = columns.ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = McLag
        fields = ('pk', 'id', 'name', 'lag_id', 'type', 'description', 'mc_domain', 'actions')
        default_columns = ('name', 'mc_domain', 'type', 'lag_id')
        orderable = True
        order_by = ('mc_domain', 'name')

MCLAG_LINK = """
{% if record.mc_lags %}{% if record.mc_lags.all %}{% for mc_lag in record.mc_lags.all %}
    <a href="{{ mc_lag.mc_domain.get_absolute_url }}">{{ mc_lag.mc_domain.name }}</a>:<a href="{{ mc_lag.get_absolute_url }}">{{ mc_lag.name }}</a>{% if not loop.last %}<br/>{% endif %}
{% endfor %}{% endif %}{% endif %}
"""

mclag_column = tables.TemplateColumn(
    verbose_name=_('MC LAG'),
    template_code=MCLAG_LINK,
    attrs={'td': {'class': 'text-nowrap'}}
)

register_table_column(mclag_column, 'mclag_column', DeviceInterfaceTable)