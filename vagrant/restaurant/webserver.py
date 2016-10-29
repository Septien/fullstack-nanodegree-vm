from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):


def main():
    try:
        port = 8080
        #Host as empty string
        server = HTTPServer (('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    #Handle ctrl+c interruption. Stops server
    except KeyboardInterrupt:
        print "^C entered, stopping the server"
        server.socket.close()



if __name__ == '__main__':
    main()
