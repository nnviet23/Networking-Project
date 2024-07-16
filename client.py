import socket
import signal
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    
    
def main():
    HOST = '127.0.0.1'
    PORT = 12345
    ADDR = (HOST, PORT)
    FORMAT = 'utf8'

    

    print("CLIENT SIDE")
    
    try:
        client.connect(ADDR)
        print("Client address: ", client.getsockname())
        print("Files available for download:")

        filename_str = client.recv(1024).decode(FORMAT)
        filenames = filename_str.split("\n")
        print(filenames)
        
        print("Press Ctrl-C to finish your connection")
        print("What files does client want to download: ")
        
        
        msg = None
        while msg != "":
            msg = input("Client talk: ")
            client.sendall(msg.encode(FORMAT))
            
    except Exception as e:
        print(f"Error: {e}")

    signal.signal(signal.SIGINT, signal_handler)
    client.close()
if __name__ == "__main__":
    main()