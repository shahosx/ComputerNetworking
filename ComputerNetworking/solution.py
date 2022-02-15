# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    # Fill in start

    # Fill in end

    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr =  # Fill in start      #Fill in end
        try:

            try:
                message =  # Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata =  # Fill in start     #Fill in end

                # Send one HTTP header line into socket.
                # Fill in start

                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
        # Send response message for file not found (404)
        # Fill in start

        # Fill in end

        # Close client socket
        # Fill in start

        # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)

"""  

from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))
    print("The server is ready to receive")
    # Fill in start
    serverSocket.listen(2)
    print('Listening on port %s ...'% port)
    # Fill in end

    while True:
        #Connection
        # Establish the connection
        #serverSocket.connect(port, addr)
        #print('Ready to serve...')
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        # will accept any client info
        #print(f"connection from {addr} has been established")
        # Fill in start

        # #Fill in end

        try:

            try:
                #co
                message = connectionSocket.recv(1024).decode()# Fill in start    #Fill in end
                #print( "Decoded the message: "+message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()

                # Fill in start     #Fill in end
                # Send one HTTP header line into socket.
                #connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
                connectionSocket.send(outputdata.encode())
                # Fill in start


                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                print("you got into an error")
            #connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
            #connectionSocket.send("<html><head></head><body><h1> 404 Not Found</h1></body></html>\r\n")

        except (ConnectionError, BrokenPipeError):
            pass
            print("you got into an error")


        #print("failed to connect to %s on port %s" %(outputdata))
        # Send response message for file not found (404)

        # Fill in start

        # Fill in end

        # Close client socket
        connectionSocket.close
        # Fill in start

        # Fill in end

        #except (ConnectionResetError, BrokenPipeError):
         #   pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)


    #Questions:
    #It's just once code to run the entire program?
    # do we need to run the html file first
    # why do we put things into two try


"""