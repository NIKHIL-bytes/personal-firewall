# Personal Firewall

## About

This project is a basic personal firewall built as a learning exercise in cybersecurity and networking.  
It monitors active network connections and applies simple allow/deny rules based on IP addresses and ports.

The goal is to understand how firewalls conceptually work rather than replace system-level firewalls.

## Objective

- Monitor active network connections
- Detect blocked IPs and ports
- Practice network traffic inspection using Python

## Tools Used

- Python
- psutil
- JSON-based rule configuration

## Rules

- Rules are defined in `rules.json`
- Only basic IP and port blocking is supported
- No packets are dropped at kernel level

## Usage

- Install dependencies:
 - pip install -r requirements.txt
- Run the firewall:
 - python firewall.py
