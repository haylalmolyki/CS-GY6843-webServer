# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))
    
    #Fill in start
    serverSocket.listen(1)  # Listen for incoming connections
    #Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end

        try:
            message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
            filename = message.split()[1]

            # opens the client requested file.
            #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], 'rb')  #fill in start #fill in end)

            # This variable can store the headers you want to send for any valid or invalid request.
            # What header should be sent for a response that is ok?
            # Fill in start
            outputdata = b"HTTP/1.1 200 OK\r\n"
            # Content-Type is an example on how to send a header as bytes. There are more!
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"  # Content type header
            outputdata += b"Connection: keep-alive\r\n"
            outputdata += b"Cache-Control: no-cache\r\n"
            outputdata += b"Date: \r\n"
            outputdata += b"Server: MyWebServer\r\n"
            outputdata += b"Set-Cookie: sessionid=abc123; Path=/; Secure; HttpOnly\r\n"
            outputdata += b"Location: \r\n"
            outputdata += b"Expires: \r\n"
            outputdata += b"ETag: \"5f3a-4ff441ea4a680\"\r\n"
            outputdata += b"Last-Modified: Sun, 06 Feb 2024 12:00:00 GMT\r\n"
            outputdata += b"X-Frame-Options: DENY\r\n"
            outputdata += b"Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline';\r\n"
            outputdata += b"Strict-Transport-Security: max-age=31536000; includeSubDomains; preload\r\n"
            outputdata += b"Referrer-Policy: strict-origin-when-cross-origin\r\n"
            outputdata += b"X-Content-Type-Options: nosniff\r\n"
            outputdata += b"X-XSS-Protection: 1; mode=block\r\n"
            outputdata += b"Allow: GET, POST, HEAD, OPTIONS\r\n"
            outputdata += b"Access-Control-Allow-Origin: *\r\n"
            # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n"
            # Fill in end
            content = b""

            for i in f:
                content  += i

            outputdata += b"Content-Length: " + str(len(content)).encode() + b"\r\n"
            outputdata += b"\r\n"
            # Send the content of the requested file to the client (don't forget the headers you created)!
            # Fill in start
            connectionSocket.send(outputdata + content)
            # Fill in end
            
            # Close the file
            f.close()
            
            connectionSocket.close()  # Closing the connection socket


        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            # Remember the format you used in the try: block!
            # Fill in start
            outputdata = b"HTTP/1.1 404 Not Found\r\n"
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"  # Content type header
            outputdata += b"Connection: keep-alive\r\n"
            outputdata += b"Cache-Control: no-cache\r\n"
            outputdata += b"Date: \r\n"
            outputdata += b"Server: MyWebServer\r\n"
            outputdata += b"Set-Cookie: sessionid=abc123; Path=/; Secure; HttpOnly\r\n"
            outputdata += b"Location: \r\n"
            outputdata += b"Expires: \r\n"
            outputdata += b"ETag: \"5f3a-4ff441ea4a680\"\r\n"
            outputdata += b"Last-Modified: Sun, 06 Feb 2024 12:00:00 GMT\r\n"
            outputdata += b"X-Frame-Options: DENY\r\n"
            outputdata += b"Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline';\r\n"
            outputdata += b"Strict-Transport-Security: max-age=31536000; includeSubDomains; preload\r\n"
            outputdata += b"Referrer-Policy: strict-origin-when-cross-origin\r\n"
            outputdata += b"X-Content-Type-Options: nosniff\r\n"
            outputdata += b"X-XSS-Protection: 1; mode=block\r\n"
            outputdata += b"Allow: GET, POST, HEAD, OPTIONS\r\n"
            outputdata += b"Access-Control-Allow-Origin: *\r\n"
            outputdata += b"\r\n"  # Blank line indicates the end of headers
            content = b"<html><head></head><body><h1>404 Not Found</h1></body></html>"

            connectionSocket.send(outputdata + content)
            # Fill in end

            # Close client socket
            # Fill in start
            connectionSocket.close()
            # Fill in end

    # Commenting out the below, as it's technically not required, and some students have moved it erroneously in the While loop.
    # DO NOT DO THAT OR YOU'RE GONNA HAVE A BAD TIME.
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer(13331)
