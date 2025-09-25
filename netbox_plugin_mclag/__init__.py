from netbox.plugins import PluginConfig


class NetBoxMcLagConfig(PluginConfig):
    name = "netbox_plugin_mclag"
    verbose_name = "Multi-Chassis LAG"
    description = "Manage Multi-Chassis Link Aggregation Groups in Netbox (MC-LAG / MLAG / vPC / etc)"
    author = "Pieter Lambrecht"
    author_email = "pieter.lambrecht@gmail.com"
    version = "0.3.0"
    base_url = "mclag"

# based original code of pv2b: https://github.com/pv2b/netbox-plugin-mclag

config = NetBoxMcLagConfig
