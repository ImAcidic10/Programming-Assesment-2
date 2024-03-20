import socket
import sys

#Inputting what IP address and ports to scan

ip=input("INPUT IP ADDRESS:")

try:
    StartingPort= int(input("FIRST PORT NUMBER: "))
except ValueError:
    print("Invalid input. Please enter a valide integer")

try:
    EndPort= int(input("LAST PORT NUMBER: "))
except ValueError:
    print("Invalid input. Please enter a valide integer")

#Code for the scan



end=input("Press any key to exit")