ps1.py - >
# Network Intrusion Detection System (Scapy-Based)

## Overview

This project is a lightweight **Intrusion Detection System (IDS)** that analyzes network traffic from a packet capture (`.pcap`) file to identify suspicious or potentially malicious activities. It leverages packet-level inspection to monitor communication patterns and flag anomalies based on predefined behavioral thresholds.

The system focuses on detecting common network-layer attacks such as scanning and flooding, making it useful for understanding traffic behavior and basic cybersecurity analysis.

---

## Objective

The primary goal of this project is to:

* Identify abnormal traffic patterns in network data
* Detect early indicators of common cyber attacks
* Provide a simple, rule-based approach to intrusion detection
* Help in learning packet analysis and network security fundamentals

---

## What It Does

The script reads captured network traffic and evaluates packets based on source IP activity. It tracks communication patterns and generates alerts when certain thresholds are exceeded.

### Detected Activities

**1. Port Scanning**

* Detects when a single source IP attempts connections to many different destination ports
* Indicates reconnaissance activity where an attacker searches for open ports

**2. Brute Force Attempts**

* Identifies repeated connection attempts to the same port from a single source
* Suggests password guessing or repeated login attempts

**3. SYN Flood Attack**

* Monitors TCP SYN packets (connection initiation requests)
* Flags excessive SYN packets from a source, indicating possible denial-of-service attempts

**4. ICMP Flood Attack**

* Tracks ICMP (ping) requests
* Detects unusually high volumes, which may indicate network flooding or probing

---

## Output

* Generates a CSV file (`ids_alerts.csv`) containing:

  * Source IP address
  * Type of detected attack
  * Additional details describing the behavior

* Also prints a summary of detected alerts to the console

---

## Why This Project Matters

* Demonstrates how **network traffic can be analyzed for security threats**
* Highlights the importance of **behavior-based detection**
* Provides a foundation for building more advanced IDS/IPS systems
* Useful for academic learning, lab experiments, and basic threat analysis

---

## Prerequisites

* Python 3.x
* Required libraries:

  * `scapy` (for packet parsing and analysis)
  * `csv` (for storing results)
  * `socket` (standard networking support)

---

## Limitations

* **Static Thresholds**: Detection is based on fixed values, which may not adapt well to different network environments
* **False Positives/Negatives**: Legitimate traffic may be flagged, or some attacks may go undetected
* **No Time-Based Analysis**: Does not consider rate (e.g., packets per second), only counts
* **Offline Processing**: Works only on pre-captured `.pcap` files, not real-time traffic
* **No Deep Packet Inspection**: Payload content is not analyzed
* **Duplicate Alerts**: Same source may trigger repeated alerts without consolidation

---

## Possible Enhancements

* Introduce dynamic or adaptive thresholds
* Implement time-window based detection (rate limiting)
* Add support for additional protocols (e.g., UDP attacks)
* Enable real-time packet monitoring
* Integrate alert deduplication and prioritization
* Build a visualization dashboard for insights

---

## Summary

This project provides a clear and practical implementation of a rule-based intrusion detection system using packet analysis. While simple, it effectively demonstrates how monitoring network behavior can help identify potential security threats.

ps2.py->
# Multithreaded Port Scanner with Basic Vulnerability Detection

## Overview

This project is a **multithreaded port scanning tool** that takes a domain name as input, resolves it to an IP address, and scans all possible TCP ports to identify open services. It also performs **basic vulnerability mapping** by associating commonly known security risks with specific open ports.

The system is designed to provide a quick overview of exposed services on a target machine and highlight potential security concerns.

---

## Objective

The main goals of this project are:

* Resolve a domain name into its corresponding IP address
* Identify open ports on the target system
* Map open ports to commonly associated vulnerabilities
* Generate structured output for analysis

---

## What It Does

### 1. Domain Resolution

* Accepts a domain name as input
* Uses DNS resolution to convert it into a valid IP address

### 2. Port Scanning

* Scans all TCP ports in the range **1 to 65535**
* Uses socket connections to check if a port is open
* Implements **multithreading** to speed up the scanning process

### 3. Open Port Detection

* Identifies ports that accept connections
* Stores and displays all open ports

### 4. Basic Vulnerability Detection

* Matches open ports with a predefined list of known vulnerabilities
* Examples include:

  * FTP → Brute force, sniffing
  * SSH → Brute force
  * HTTP → XSS, SQL Injection
  * SMB → Ransomware risks
  * RDP → Brute force attacks

### 5. Result Logging

* Exports results to a CSV file (`ports.csv`)
* Each entry includes:

  * Open port number
  * Associated vulnerability (if known)

---

## Why This Project Matters

* Demonstrates how exposed network services can become **attack entry points**
* Highlights the importance of **port security and service hardening**
* Provides a basic understanding of **network reconnaissance techniques**
* Useful for educational purposes and introductory cybersecurity practice

---

## Key Features

* Full port range scanning (1–65535)
* Multithreaded execution for improved performance
* Real-time console alerts for open ports and vulnerabilities
* CSV-based reporting for easy analysis
* Simple and extensible vulnerability mapping

---

## Prerequisites

* Python 3.x
* Required libraries:

  * `socket` (for network communication)
  * `threading` (for concurrent scanning)
  * `csv` (for exporting results)

---

## Limitations

* **No Service Verification**: Assumes vulnerabilities based only on port numbers, not actual service detection
* **High Resource Usage**: Creating a thread per port can consume significant system resources
* **Timeout Dependency**: Fixed timeout may lead to missed open ports or slower scans
* **No Banner Grabbing**: Does not retrieve service information for deeper analysis
* **False Positives**: Open port does not always imply vulnerability
* **No Rate Limiting**: May overwhelm the network or trigger security defenses
* **Legal/Ethical Concerns**: Scanning systems without permission may violate policies or laws

---

## Possible Enhancements

* Implement thread pooling instead of one thread per port
* Add banner grabbing for accurate service identification
* Introduce OS and service fingerprinting
* Include UDP port scanning
* Add configurable scan ranges and timeout settings
* Integrate real vulnerability databases (e.g., CVE mapping)
* Build a GUI or dashboard for visualization

---

## Summary

This project provides a practical implementation of a **basic port scanner combined with vulnerability awareness**. While it uses simplified assumptions, it effectively demonstrates how attackers and security analysts identify exposed services and assess potential risks in a network.
