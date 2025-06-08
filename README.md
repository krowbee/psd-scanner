# PSD Scanner — Fast Multi-Threaded Port Scanner (Python)

**PSD Scanner** is a lightweight yet powerful multithreaded port scanner built in Python. It supports scanning single IPs, IP ranges (CIDR), hostnames, and lists from files.
Results can include basic banner grabbing and be exported to a file.

This tool was created as a personal learning project to dive into network programming, threading, and building real-world security tools with clean, modular Python code.

---

## Features

- ✅ **Multithreaded scanning** with configurable thread count
- ✅ **Flexible target input**: IPs, hostnames, CIDR, or .txt lists
- ✅ **Custom port ranges** or specific port lists (`80,443,8000-8100`)
- ✅ **Basic banner grabbing** (e.g., SSH, HTTP services)
- ✅ **Output results to file**
- ✅ **Color-coded terminal output** (using `colorama`)
- ✅ **Modular structure** – clean and extensible

---

## Usage

```bash
python psd.py -t <target> [-p <ports>] [--threads <n>] [-o <output_file>]
