# python-multithreaded-webserver

Develop a simple web server in Python that is capable of processing multi-requests using threads. Specifically, the web server will:
- create a connection socket when contacted by a client (browser); 
- receive the HTTP request from this connection; 
- parse the request to determine the specific file being requested; 
- get the requested file from the server’s file system; 
- create an HTTP response message consisting of the requested file preceded by header lines; and 
- send the response over the TCP connection to the requesting browser. If a browser requests a file that is not present in your server, your server should return a “404 Not Found” error message. 
