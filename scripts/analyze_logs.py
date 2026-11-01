from collections import Counter
import re

log_file = "logs/auth.log"

with open(log_file, "r") as file:
    logs = file.readlines()

print(f"Total log entries: {len(logs)}")

failed_logins = []

for line in logs:
    if "Failed password" in line:
        failed_logins.append(line)

print(f"Failed login attempts: {len(failed_logins)}")

failed_ips = []

for line in failed_logins:
    match = re.search(r"from (\d{1,3}(?:\.\d{1,3}){3})", line)

    if match:
        ip_address = match.group(1)
        failed_ips.append(ip_address)

print("\nFailed login attempts by IP: ")

for ip, count in Counter(failed_ips).items():
    print(f"{ip}: {count} attempts")

successful_logins = []

for line in logs:
    if "Accepted password" in line:
        successful_logins.append(line)

print(f"\nSuccessful login attempts: {len(successful_logins)}")

for line in successful_logins:
    print(line.strip())

suspicious_ips = []

for ip in Counter(failed_ips):
    for line in successful_logins:
        if f"from {ip} " in line:
            suspicious_ips.append(ip)
            break

print("\nSuspicious IP addresses:")

for ip in suspicious_ips:
    print(f"ALERT: {ip} had failed login attempts followed by a successful login.")
