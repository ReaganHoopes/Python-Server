import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from time import strftime


class CS2610Assn1(BaseHTTPRequestHandler):

    def standardResponse(self, path, code, altLocation = "none"):
        if altLocation == "none":
            f = open(path, 'rb')
            dat = f.read()
            f.close()
            content_length = len(dat)
        else:
            f = open(altLocation, 'rb')
            dat = f.read()
            f.close()
            content_length = len(dat)

        self.send_response(code)
        self.send_header("Connection", "Close")
        self.send_header("Cache-Control", "max-age=0")

        if altLocation == "none":
            self.send_header("Content-Length", str(content_length))
            self.send_header("Content-Type", mimetypes.guess_type(self.path)[0])

        else:
            self.send_header("Location", "/" + altLocation)

        self.end_headers()
        self.wfile.write(dat)


    def errorResponse(self, path, code):
        self.send_response(code)
        self.send_header("Connection", "Close")
        self.send_header("Cache-Control", "max-age=0")
        self.send_header("Content-Type", mimetypes.guess_type(self.path)[0])
        self.end_headers()
        self.wfile.write(b"\n")

        if code == 418:
            self.wfile.write(b"<title>Error 418</title>\n")
            self.wfile.write(b"<h1>I am not a Teapot</h1>\n")
            self.wfile.write(b"<p>Go Back: <a href='/index.html'>Home</a></p>\n")
        elif code == 403:
            self.wfile.write(b"<title>Error 403</title>\n")
            self.wfile.write(b"<h1>Forbidden: Watch your back</h1>\n")
            self.wfile.write(b"<p>Go Back: <a href='/index.html'>Home</a></p>\n")
        elif code == 404:
            self.wfile.write(b"<title>Error 404</title>\n")
            self.wfile.write(b"<h1>You Are Mistaken</h1>\n")
            self.wfile.write(b"<p>You wanted to visit:</p>\n")
            self.wfile.write(bytes(f"{path}\n", "utf-8"))
            self.wfile.write(b"<p>Sorry! Not today...or any day!</p>\n")
            self.wfile.write(b"<p>Go Back: <a href='/index.html'>Home</a></p>\n")


    def do_GET(self):
        if self.path == '/':
            self.standardResponse("index.html", 301, altLocation="index.html")
        elif self.path == '/plan.html':
            self.standardResponse('plan.html', 200)
        elif self.path == '/plan':
            self.standardResponse("plan.html", 301, altLocation="plan.html")
        elif self.path == '/index.html':
            self.standardResponse("index.html", 200)
        elif self.path == '/index':
            self.standardResponse("index.html", 301, altLocation="index.html")
        elif self.path == '/about.html':
            self.standardResponse("about.html", 200)
        elif self.path == '/about':
            self.standardResponse("about.html", 301, altLocation="about.html")
        elif self.path.startswith("/bio"):
            self.standardResponse("about.html", 301, altLocation="about.html")
        elif self.path == '/tips' or self.path == '/help':
            self.standardResponse("techtips+css.html", 301, altLocation="techtips+css.html")
        elif self.path == '/techtips+css.html':
            self.standardResponse("techtips+css.html", 200)
        elif self.path == '/techtips+css':
            self.standardResponse("techtips+css.html", 301, altLocation="techtips+css.html")
        elif self.path == '/techtips-css.html':
            self.standardResponse("techtips-css.html", 200)
        elif self.path == '/techtips-css':
            self.standardResponse("techtips-css.html", 301, altLocation="techtips-css.html")
        elif self.path == '/debugging':
            self.send_response(200)
            self.wfile.write(b"HTTP/1.0 200 OK\n")
            self.wfile.write(bytes(f"Server: {server_address}\n","utf-8"))
            self.wfile.write(bytes(f"Date: {strftime('%c')}\n", "utf-8"))
            self.wfile.write(b"\n")
            self.wfile.write(b"<title>Server Debugging Page</title>\n")
            self.wfile.write(b"<h1>Server Debugging Page</h1>\n")
            self.wfile.write(bytes(f"<p>You are visiting debugging from the IP address {self.address_string()}, port number {self.client_address[1]}. </p>\n","utf-8"))
            self.wfile.write(bytes(f"<p>Currently, it is {strftime('%c')}</p>\n", "utf-8"))
            self.wfile.write(bytes(
                f"<ul> <li>Command: {self.command}</li> <li>Path: {self.path}</li> <li>Request Version: {self.request_version}</li> <li>Version String: {self.version_string()}</li> </ul>\n",
                "utf-8"))
            self.wfile.write(b"<h2>Request Headers</h2>")
            for header in self.headers:
                self.wfile.write(bytes(f"<p>{header} => {self.headers[header]}</p>\n", "utf-8"))
            self.wfile.write(b"<p>Go Back: <a href='/'>Home</a></p>\n")

        #images
        elif self.path.startswith("/kp_"):
            self.standardResponse(self.path[1:], 200)
        #favicon
        elif self.path == '/favicon.ico':
            self.standardResponse('favicon.ico', 200)
        #style sheet
        elif self.path == '/style.css':
            self.standardResponse('style.css',200)
        elif self.path == '/teapot':
            self.errorResponse(self.path, 418)
        elif self.path == '/forbidden':
            self.errorResponse(self.path, 403)
        else:
            self.errorResponse(self.path, 404)


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    try:
        HTTPServer(server_address, CS2610Assn1).serve_forever()
    except KeyboardInterrupt:
        print(" Exiting")
        exit(0)