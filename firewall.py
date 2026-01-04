import psutil
import json
import time

def load_rules():
    with open("rules.json", "r") as f:
        return json.load(f)

def monitor_traffic(rules):
    print("Personal Firewall Running...")
    while True:
        conns = psutil.net_connections(kind="inet")
        for c in conns:
            if not c.raddr:
                continue

            ip = c.raddr.ip
            port = c.raddr.port

            if ip in rules["blocked_ips"]:
                print(f"Blocked IP detected: {ip}")

            if port in rules["blocked_ports"]:
                print(f"Blocked Port detected: {port}")

        time.sleep(3)

if __name__ == "__main__":
    rules = load_rules()
    monitor_traffic(rules)
