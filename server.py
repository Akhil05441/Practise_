import http.server
import socketserver

PORT = 8080

class HealthCheckHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "healthy", "message": "API is running"}')

with socketserver.TCPServer(("", PORT), HealthCheckHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()