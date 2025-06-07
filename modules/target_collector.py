import ipaddress
import os
import socket

def ip_address_validation(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False


def dns_resolver(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False


def collect_targets(arguments) -> list[str]:
    targets = []

    if "/" in arguments.target:
        try:
            network = ipaddress.IPv4Network(arguments.target, strict=False)
            targets = [str(ip) for ip in network.hosts()]
        except ValueError:
            print(f"[!] Not correct CIDR: {arguments.target}")
            return []

    elif os.path.isfile(arguments.target):
        with open(arguments.target, "r") as ip_file:
            for line in ip_file:
                target = line.strip()
                if target:
                    if ip_address_validation(target) or dns_resolver(target):
                        targets.append(target)

    else:
        if ip_address_validation(arguments.target) or dns_resolver(arguments.target):
            targets.append(arguments.target)

    return targets
