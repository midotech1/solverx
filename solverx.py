import os
import nmap
import time
import socket
import pyfiglet
time.sleep(0.5)
os.system("clear")
def Banner():
    time.sleep(0.5)
    os.system("figlet SolverX")
    print("                               (V1.0)")
    print("                               Github: midotech1")
    print("                               Instagram: @hackerman_xz_1")
    time.sleep(0.5)
    print("")
def redx():
    host = input("Enter Hostname (www.example.com): ")
    # Get the IP address of the website using gethostbyname()
    ip_address = socket.gethostbyname(host)
    if host == host:
        time.sleep(1)
        print("-------------------------------------------------------")
        print("/SolverX v1.0/")
        print("-------------------------------------------------------")
        time.sleep(0.5)
        os.system("date")
        print(f"The IP address of {host} is: {ip_address}")
        df_port = "80"
        print(f"Default port is :{df_port}")
        print("-------------------------------------------------------")
    elif host <= host:
        print(f"Unable to get IP address for {host}. Please check the domain name.")
        exit()
Banner()
redx()

def scan_open_ports():
    sn_host = input("Enter The Scaned Host: ")
    # Create a PortScanner object
    nm = nmap.PortScanner()
    # Scan the target for open ports
    print(f"Scanning target: {sn_host}")
    nm.scan(hosts=sn_host, arguments='-p 1-1024')
    # Scanning ports 1-1024
    # Retrieve and display open ports
    print("-------------------------------------------------------")
    for host in nm.all_hosts():
        print(f"Host: {sn_host}")
        if 'hostnames' in nm[host]:
            print(f"Hostnames: {nm[host]['hostnames']}")
            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                lport = nm[host][proto].keys()
                for port in lport:
                    print("-------------------------------------------------------")
                    print(f"Port: {port}, State: {nm[host][proto][port]['state']}")
                    time.sleep(1)
                    print("-------------------------------------------------------")
scan_open_ports()


