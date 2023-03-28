import socket

target_host = input("Enter the target host: ")
target_port = int(input("Enter the target port: "))

# create a new socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set a timeout of 1 second
client.settimeout(1)

try:
    # connect to the target host and port
    client.connect((target_host, target_port))
    
    # print a message indicating the port is open
    print(f"Port {target_port} is open on {target_host}")
    
except:
    # print a message indicating the port is closed
    print(f"Port {target_port} is closed on {target_host}")
    
finally:
    # close the socket
    client.close()
