# 17. Device Connection Monitor
# Goal: Track connected devices to a server.
# Requirements:
# - Use set() to track current connections.
# - Use pop() when a device disconnects.
# - Use union() to merge multiple server logs.
# Concepts Covered: pop(), union(), membership.

server1_devices = {"deviceA", "deviceB", "deviceC"}
server2_devices = {"deviceD", "deviceE", "deviceB"}

current_connections = server1_devices.union(server2_devices)
disconnected_device = current_connections.pop()

print("Active connections after disconnection:", current_connections)
print("Disconnected device:", disconnected_device)
