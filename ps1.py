import scapy.all as scapy
import csv
import socket

pcap_file = "traffic.pcap"

ip_ports ={}
ip_port_count ={}
syn_count ={}
icmp_count =[]
alerts =[]

packets = scapy.rdpcap(pcap_file)
for i in packets:
    if i.haslayer(scapy.IP):
        src = i[scapy.IP].src
        if i.haslayer(scapy.TCP):
            dport = i[scapy.TCP].dport
            if src not in ip_ports:
                ip_ports[src] = []
            if dport not in ip_ports[src]:
                ip_ports[src].append(dport)
            if len(ip_ports[src]) >= 20:
                alerts.append([src, "port scan", "multiple ports"])
            key = (src, dport)
            if key in ip_port_count:
                ip_port_count[key] += 1
            else:
                ip_port_count[key] = 1

            if ip_port_count[key] >= 10:
                alerts.append([src,"brute force","port " + str(dport)])

            if i[scapy.TCP].flags == 2:  
                if src in syn_count:
                    syn_count[src] += 1
                else:
                    syn_count[src] = 1

                if syn_count[src] == 30:
                    alerts.append([src,"syn flood","excess syn packets"])

        if i.haslayer(scapy.ICMP):
            icmp_count.append(src)
            j = icmp_count.count(src)   
            if j >= 30:
                alerts.append([src,"icmp flood","excess icmp packets"])

with open("ids_alerts.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["source ip","attack type","details"])
    for i in alerts:
        writer.writerow(i)

print("Scan complete")
print("Alerts found:",len(alerts))
for i in alerts:
    print(i)
