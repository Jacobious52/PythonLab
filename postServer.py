from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class POSTHTTPHandler(BaseHTTPRequestHandler):
    def _set_headers(self, type='html'):
        self.send_response(200)
        self.send_header('Content-type', 'text/%s')
        self.end_headers()
 
    def do_GET(self):
        self._set_headers('txt')
        with open('wall.txt', 'r') as wall:
            self.wfile.write(wall.read().encode())
 
    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        self._set_headers('txt')
        length = self.headers['content-length']
        data = self.rfile.read(int(length))
        with open('wall.txt', 'a') as wall:
            wall.write('\n' + data.decode())
        self.wfile.write("Accepted")
        
def run_server():
    server_address = ('', 8000)
    http_server = HTTPServer(server_address, POSTHTTPHandler)
    print 'Starting HTTP server at %s on port %s' % server_address
    http_server.serve_forever()
 
if __name__ == "__main__":
        run_server()