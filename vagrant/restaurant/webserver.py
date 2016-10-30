from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

#Necesary moduls for CRUD
from database_setup import Restaurant, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Create session and connect to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET request. Use pattern matching for knowing wich
        resource are being tryed to access.
        Overrides do_GET method of base class.
        """
        try:
            #Handler for delete restaurants
            if self.path.endswith('/delete'):
                restaurantIDPath = self.path.split("/")[2]
                restaurantQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if restaurantQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>%s</h1>" % restaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete' >" % restaurantIDPath
                    output += "<input name='editRestaurant' type='text' placeholder='%s' >" % restaurantQuery.name
                    output += "<input type='submit' value='Edit' >"
                    output += "</form></body></html>"
                    self.wfile.write(output)
                return

            #Handler for edit restaurants
            #Iterate over all of them
            restaurants = session.query(Restaurant).all()
            for restaurant in restaurants:
                #It is the restaurant?
                path = "/restaurants/%s/edit" % restaurant.id
                if self.path.endswith(path):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>%s</h1>" % restaurant.name
                    output += "<form method='POST' enctype='multipart/form-data' action='%s' >" % path
                    output += "<input name='editRestaurant' type='text' placeholder='%s' >" % restaurant.name
                    output += "<input type='submit' value='Edit' >"
                    output += "</form></body></html>"
                    self.wfile.write(output)
                    return


            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new' >"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name' >"
                output += "<input type='submit' value='Create' >"
                output += "</form></body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                query = session.query(Restaurant).all()
                output = ""
                output += "<html><body>"
                for q in query:
                    output += q.name
                    output += "</br><a href='/restaurants/%s/edit'>Edit</a>" % q.id
                    output += "</br><a href='/restaurants/%s/delete'>Delete</a></br></br>" % q.id
                output += "<h2><a href='/restaurants/new'>Make a New Restaurant Here</h2>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                print "\n"
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        """
        Handle POST request. Uses Common Gateway Interface.
        Overrides do_POST method of base class.
        """
        try:
            #Handler POST method for edit restaurants
            restaurants = session.query(Restaurant).all()
            for restaurant in restaurants:
                #It is the restaurant?
                path = "/restaurants/%s/edit" % restaurant.id
                if self.path.endswith(path):
                    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        messagecontent = fields.get('editRestaurant')
                        #Modify restaurant
                        restaurant.name = messagecontent[0]
                        session.add(restaurant)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()
                        break

            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    #Create new restaurant class
                    newRestaurant = Restaurant(name = messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            # #Recieve the post request
            # self.send_response(301)
            # self.send_header('Content-type', 'text/html')
            # self.end_headers()

            # ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            # if ctype == 'multipart/form-data':
            #     fields = cgi.parse_multipart(self.rfile, pdict)
            #     messagecontent = fields.get('message')

            # #Decide what to send
            # output = ""
            # output += "<html><body>"
            # output += " <h2> Okay, how about this: </h2>"
            # output += "<h1> %s </h1>" % messagecontent[0]
            # #Post request and header tag. Request the user to input something
            # output += '''<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2>
            #             <input name="message" type="text"><input type="submit" value="Submit"> </form>'''
            # output += "</body></html>"
            # self.wfile.write(output)
            # print output
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
