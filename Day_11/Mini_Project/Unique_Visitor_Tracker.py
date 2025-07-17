# 1. Unique Visitor Tracker
# Goal: Track unique visitors to a website.
# Requirements:
# - Store each visitor’s IP in a set.
# - Use add() for each new IP.
# - Use len() to get total unique visits.
# - Use discard() to remove blacklisted IPs.
# - Save a backup of visitor set using copy().
# Concepts Covered: add(), discard(), copy(), membership test, len().

visitor_ips = set()

visitor_ips.add("192.168.1.1")
visitor_ips.add("10.0.0.2")
visitor_ips.add("172.16.0.3")
visitor_ips.add("192.168.1.1")

print("Total unique visitors:", len(visitor_ips))

check_ip = "10.0.0.2"
if check_ip in visitor_ips:
    print(f"{check_ip} has visited the site.")
else:
    print(f"{check_ip} has not visited the site.")

blacklisted_ips = ["192.168.1.1", "8.8.8.8"]
for ip in blacklisted_ips:
    visitor_ips.discard(ip)

backup_visitors = visitor_ips.copy()
print("Backup of visitor IPs:", backup_visitors)
