from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        import pymongo
        client = pymongo.MongoClient("mongodb+srv://artemn9:rDkAH8Npm5XXHaPb@artemn9-mongo-fpjxf.mongodb.net/test?retryWrites=true")
        db = client.get_database('academic')
        cl = db.get_collection('papers')
        for doc in cl.find():
            self.wfile.write(str(doc).encode())
        return
