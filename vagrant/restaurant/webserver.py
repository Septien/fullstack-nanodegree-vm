from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#Necesary moduls for CRUD
from database_setup import Restaurant, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_session():
    '''
    Create session for queries.
    '''
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadate.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

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
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
                        <input name="message" type="text"><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>&#161Hola!</h1>"
                output += '''<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
                        <input name="message" type="text"><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        """
        Handle POST request. Uses Common Gateway Interface.
        Overrides do_POST method of base class.
        """
        try:
            #Recieve the post request
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            #Decide what to send
            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            #Post request and header tag. Request the user to input something
            output += '''<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
                        <input name="message" type="text"><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output
        except:
            pass

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
