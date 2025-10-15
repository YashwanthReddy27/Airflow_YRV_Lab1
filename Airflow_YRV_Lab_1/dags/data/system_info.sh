#!/bin/bash

echo "===== System Information ====="
echo "Dtate and Time: $(data)"
echo "Uptime: $(uptime -p)"
echo "Logged in users:"
who

echo ""
echo "===== Disk Usage Summary ====="
df -h | grep -v tmpfs | grep -v loop

echo ""
echo "===== Top 5 Memory Consuming Processes ====="
ps aux --sort=-%mem | head -n 6

echo ""
echo "===== Network Interfaces and IPs ====="
ip -brief addr show | grep -v lo

echo ""
echo "Script run completed!"