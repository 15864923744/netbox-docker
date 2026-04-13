# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# PLUGINS = ["netbox_bgp"]

# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }

PLUGINS = [
    "netbox_diode_plugin",
]

PLUGINS_CONFIG = {
    "netbox_diode_plugin": {
        # Diode gRPC target for communication with Diode server
        "diode_target_override": "grpc://diode-diode-auth-1:8080/diode",

        # Username associated with changes applied via plugin
        "diode_username": "diode-ingest",

        # netbox-to-diode client_secret created during diode bootstrap.
        "netbox_to_diode_client_secret": "iR23FR393k4JPUpUyM5p5i05YccuOlECX8tWtiNtk0="
    },
}
