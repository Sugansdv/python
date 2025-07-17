# 14. IP Logger with Blacklist
# Goal: Log only clean IPs from visitors.
# Requirements:
# - Store visitor IPs in a set.
# - Store blacklist in another set.
# - Use isdisjoint() to validate before adding.
# - If blacklisted, discard() or skip.
# Concepts Covered: isdisjoint(), discard(), membership test.

visitor_ips = set()
blacklist = {"192.168.1.100", "10.0.0.9"}

incoming_ips = ["192.168.1.10", "10.0.0.9", "172.16.0.5", "192.168.1.100", "192.168.1.10"]

for ip in incoming_ips:
    if ip not in blacklist:
        visitor_ips.add(ip)

print("Logged visitor IPs:", visitor_ips)
