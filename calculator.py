import ipaddress

def calculate_network(ip):
    network = ipaddress.ip_network(ip, strict=False)

    return {
        "network": str(network.network_address),
        "broadcast": str(network.broadcast_address),
        "mask": str(network.netmask),
        "total": network.num_addresses,
        "first_host": str(list(network.hosts())[0]),
        "last_host": str(list(network.hosts())[-1])
    }