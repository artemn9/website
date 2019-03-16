from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(str("Hello, getting ready. // ").encode())
        import pymongo
        self.wfile.write(str("Pymongo inserted. // ").encode())
        client = pymongo.MongoClient("mongodb+srv://artemn9:rDkAH8Npm5XXHaPb@artemn9-mongo-fpjxf.mongodb.net/test?retryWrites=true")
        db = client.get_database('academic')
        cl = db.get_collection('papers')
        self.wfile.write(str("Starting cycle. // ").encode())
        for doc in cl.find():
            self.wfile.write(str("one ... ").encode())
            self.wfile.write(str(doc).encode())
        return
