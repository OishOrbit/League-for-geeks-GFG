# Accept a domain name and resolve it to a valid IP address
# ● Scan the resolved IP for open ports
# ● Perform basic vulnerability checks on open ports
# ● Alert the user if any vulnerabilities are detected
# ● (Optional) Export scan results to a CSV log file
import socket
import csv 
import threading
target_domain=input("Enter the domain name : ")
target_domain.strip() 
target_ip=socket.gethostbyname(target_domain)
# target_ip="192.168.1.10" for example 
ports = range(1,65535)
open_ports=[]

port_vulnerabilities={21:"FTP-Brute force,Sniffing",
                      22:"SSH-Brute force",
                      23: "telnet-MITM,sniffing",
                      25: "SMPT-Spoofing,spam",
                      53: "DNS-cache poisoning",
                      80: "HTTP-XSS,SQLi",
                      443:"HTTPS-TLS downgrade",
                      110:"POP3-Credential theft",
                      143:"IMAP-account takeover",   
                      3306: "MySQL-DB access",
                      445:"SMB- ransomware",
                      3389:"RDP - Bruteforce"                  
                      }
lock = threading.Lock()
def scan(ports):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.settimeout(1)
    result=server.connect_ex((target_ip,ports))
    if result==0:
        with lock:
            print("Öpen port",ports)
            open_ports.append(ports)
            
        if ports in port_vulnerabilities:
         print("Alert: ",port_vulnerabilities[ports])
        
        # data=server.recv(1024)
        # data=data.decode().strip()
        # print(data) omitting as error= timeout, crash
    server.close()
 
threads=[]
for i in ports:
    t=threading.Thread(target=scan, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

with open("ports.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Open Ports","Vulnerabilities"])
    # for rows in ports:
    #     print(rows)
    for i in open_ports:
        vuln = port_vulnerabilities.get(i)
        writer.writerow([i, vuln])

print("Scan is complete and the results are in csv file \n")
            
        
    
