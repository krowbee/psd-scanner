import socket
from colorama import Fore


def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    banner = sock.recv(1024).decode(errors="ignore").strip()
                    print(Fore.GREEN + f"[{port}] is open! {banner}")
                    return f"[{port}] is open! {banner}"
                except socket.timeout:
                    print(Fore.GREEN + f"[{port}] is open!")
                    return f"[{port}] is open!"
    except socket.gaierror:
        pass
    except socket.timeout:
        pass
    except Exception:
        pass
