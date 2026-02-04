# ⚡ SHADOW - Advanced Network Stress Testing Tool

![Version](https://img.shields.io/badge/version-3.0-red)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

SHADOW is a high-performance network testing tool developed for academic purposes. It is designed to simulate various types of network traffic to analyze server stability and resilience against high-load scenarios.

## 🚀 Features
* **Multi-Protocol Support:** Supports HTTP Request flooding, SYN Flood (Layer 4), and Pyslow (Slowloris) methods.
* **Smart User-Agent Switching:** Randomizes User-Agent strings to simulate diverse client environments.
* **Multi-Threading:** Optimized thread management for maximum concurrent connections.
* **Customizable Payload:** Ability to adjust timeout, sleep intervals, and thread counts via CLI.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/username/shadow-ddos.git](https://github.com/username/shadow-ddos.git)
   cd shadow-ddos
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

📖 Usage
Run the tool with the following arguments:
Bash
python shadow_ddos.py -d <target_url/ip> [options]

Examples:
HTTP Request Flood:
```bash
python shadow_ddos.py -d [www.example.com](https://www.example.com) -T 2000 -Request
SYN Flood (Requires Root/Sudo):

```bash
sudo python shadow_ddos.py -d 192.168.1.1 -T 5000 -Synflood
Slowloris Attack (Pyslow):

```bash
python shadow_ddos.py -d [www.example.com](https://www.example.com) -p 80 -T 500 -Pyslow

📊 Technical Overview
This tool operates at different layers of the OSI model:

SYN Flood: Targets the Transport Layer (Layer 4) by exploiting the TCP three-way handshake.

HTTP Request: Targets the Application Layer (Layer 7) by exhausting web server resources.
