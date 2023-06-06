import http.server #Parameter : localisation. handler
import socketserver

class APIHANDLER(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) :
        print(" Test API") 
        self.send_response(200)
        self.send_header('Content-Type','text/json')
        self.end_headers()
        self.wfile.write("test response".encode('UTF-8'))
        
MyAPIHANDLER = APIHANDLER

#server
try:
    with socketserver.TCPServer(("", 8081), MyAPIHANDLER) as httpd :
        print ("server working")
        httpd.allow_reuse_address = True
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping server")
    httpd.server_close()

