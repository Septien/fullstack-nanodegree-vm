from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET request. Use pattern matching for knowing wich
        resource are being tryed to access.
        Overrides do_GET method of base class.
        """
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola! <a href='/hello'>Back to Hello</a></body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)


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
