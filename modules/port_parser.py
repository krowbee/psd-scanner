
def parse_ports(arguments) -> list[int]:
    ports = set()
    
    parts = arguments.ports.split(",")
                                
    for part in parts:
        if "-" in part:
            try:
                start, end = map(int, part.split("-"))
                if start > end or not (0 <= start <= 65535) or not (0 <= end <= 65535):
                    raise ValueError
                ports.update(range(start, end+1))
                return ports
            except ValueError:
                print(f"[!] Invalid port range: {part}")
        else:
            try:
                port = int(part)
                if not (0 <= port <= 65535):
                    raise ValueError
                else:
                    ports.add(port)
            except ValueError:
                print(f"[!] Invalid port: {part}")
    return sorted(list(ports))
