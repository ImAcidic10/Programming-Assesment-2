import socket #The library used

print("Make sure to have the correct authorisation before executing this program.") #A text-based warning to make sure that those who are executing this program must have the correct authorisation.

#Inputting what IP address and ports to scan
def main():
    socket.setdefaulttimeout(0.01) #Socket time out

    scanHost(ip, StartingPort, EndPort)
ip=input("INPUT IP ADDRESS:") #This is where the user inputs the IP address to scan

try:
    StartingPort= int(input("FIRST PORT NUMBER: ")) #This is where the user inputs the first port they want to scan from.
except ValueError:
    print("Invalid input. Please enter a valide integer") #This is the error that will be outputted if an integer isn't inputted.

try:
    EndPort= int(input("LAST PORT NUMBER: ")) #This is last port which the program will stop scanning at
except ValueError:
    print("Invalid input. Please enter a valide integer") #This is the error that will be outputted if an integer isn't inputted.

#Code for the scan

def scanHost(ip, StartingPort, EndPort): #definition for 'scanHost'
    print('Starting TCP port scan on host %s' % ip) #Text showing that it has started a TCP scan
    tcp_scan(ip, StartingPort, EndPort) #TCP scan code
    print('TCP scan on host %s complete' % ip) #Text saying it is a certain number percentage complete


def scanRange(network, startPort, endPort): #Definintion of 'scanRange'
    print('Starting TCP port scan on network %s.0' % network) #Title text saying what network ip is being scanned
    for host in range(1, 255): #A loop construct based on the IP
        ip = network + '.' + str(host) #The IP and the host range put together with the use of a string
        tcp_scan(ip, StartingPort, EndPort) #Telling the program to scan a specified IP and set of ports

    print('TCP scan on network %s.0 complete' % network) #Output updating the percentage complete

def tcp_scan(ip, StartingPort, EndPort): #repeat of telling the program to scan a specified IP and set of ports
    for port in range(StartingPort, EndPort + 1):
        try: #try except code
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket library code that is needed
            if not tcp.connect_ex((ip, port)): #attempting to connect to specified IP and port to decide whether it is open or closed.
                print('%s:%d/Open' % (ip, port)) #Text output letting the user know is the specified IP's port is open
                tcp.close() #Closing the connection to the IP and port
        except Exception: #Exception meaning if the port is closed, just pass and ignore it. 
            pass #Just a placeholder to ingore/ do nothing
            
main()
end=input("Press any key to close") #A Just an output saying to press any key to exit the program