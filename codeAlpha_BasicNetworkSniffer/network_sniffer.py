from scapy.all import sniff, IP, TCP, UDP, Raw
import csv
from datetime import datetime

# CSV file to store packet data
csv_file = "packet_log.csv"

# Write headers to CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Protocol", "Source IP", "Destination IP", "Payload"])

# Callback function to process each packet
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = "OTHER"
        payload = ""

        if TCP in packet:
            proto = "TCP"
        elif UDP in packet:
            proto = "UDP"

        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load.decode(errors='ignore')
            except:
                payload = "N/A"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{timestamp}] {proto} | {src_ip} -> {dst_ip}")
        if payload:
            print(f"Payload: {payload}\n")

        # Write to CSV
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, proto, src_ip, dst_ip, payload])

# Run sniffer
print("Sniffing... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)