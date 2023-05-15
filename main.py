from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_index(self):
        return "<h1>Hello, World wide web!</h1>"

    def do_GET(self):
        content = self.__get_index()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        request_body = self.rfile.read(content_length)
        print(request_body.decode('utf-8'))

        self.send_response(201)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('Data has been posted', 'utf-8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server has been started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server has been stopped!")
