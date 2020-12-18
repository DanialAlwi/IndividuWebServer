import socketserver
import http.server
import ssl

from http.server import HTTPServer, BaseHTTPRequestHandler 

class pelayan(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			self.path = 'index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "File Tak Jumpa!!"
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))


pelayan = socketserver.TCPServer(('192.168.1.27', 443), http.server.SimpleHTTPRequestHandler)

pelayan.socket = ssl.wrap_socket(pelayan.socket, certfile= "/home/nial/newP/pelayan.pem", keyfile= "/home/nial/newP/kunci.pem", server_side=True)
pelayan.serve_forever()
