from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def main():
    try:
        port = 8080
        #Host as empty string
        server = HTTPServer (('', port), webserverHandler)

    #Handle ctrl+c interruption
    except KeyboardInterrupt:



if __name__ == '__main__':
    main()
