import argparse
from colorama import init, Fore
from modules.port_parser import parse_ports
from modules.target_collector import collect_targets
from modules.threads_valid import valid_threads
from modules.scan import scan_port
from concurrent.futures import ThreadPoolExecutor, as_completed


init()
argparser = argparse.ArgumentParser(prog="PSD SCANNER", add_help=True)
argparser.add_argument("-t", "--target", help="Target IP, or IP txt list", required=True)
argparser.add_argument("-p", "--ports", help="Ports you need to scan", default="1-1024")
argparser.add_argument("--threads", type=int, help="Set THREADS. Be carefully (DEF:10)", default=10)
argparser.add_argument("-o", "--output", help="File to output", default=None)

arguments = argparser.parse_args()

threads = valid_threads(arguments)
targets = collect_targets(arguments)
ports = parse_ports(arguments)

print(Fore.CYAN + "Scan started! \n"
      f"THREADS:{threads}\n"
      f"PORTS:{arguments.ports}")


results = []

with ThreadPoolExecutor(max_workers=threads) as executor:

    futures = [executor.submit(scan_port, target, port) for target in targets for port in ports]

    for future in as_completed(futures):
        results.append(future.result())

if arguments.output:
    with open(arguments.output, "w") as f:
        for line in results:
            if line is not None and line != " ":
                f.write(f"{line}\n")
