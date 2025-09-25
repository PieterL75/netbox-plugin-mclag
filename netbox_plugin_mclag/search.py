from netbox.search import SearchIndex, register_search
from netbox_plugin_mclag.models import McDomain, McLag

@register_search
class McDomainIndex(SearchIndex):
    model = McDomain
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('domain_id', 'description')

@register_search
class McLagIndex(SearchIndex):
    model = McLag
    fields = (
        ('name', 100),
        ('description', 500),
    )
    display_attrs = ('lag_id', 'mc_domain', 'description')