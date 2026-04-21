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
