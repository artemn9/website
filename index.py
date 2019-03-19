from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # get the mongodb connection:
        import pymongo
        client = pymongo.MongoClient("mongodb+srv://artemn9:rDkAH8Npm5XXHaPb@artemn9-mongo-fpjxf.mongodb.net/test?retryWrites=true")
        db = client.get_database('academic')
        cl = db.get_collection('papers')

        # published papers
        papers = []
        for doc in cl.find({"publish": True}):
            #title = doc['title']
            abstract = doc['abstract']
            cite = doc['cite']
            papers.append('<h4>{cite}</h4><p><I>{abstract}</I></p>'.format(cite=cite,
            abstract=abstract))

        # working papers
        wpapers = []
        for wdoc in cl.find({"publish": None}):
            title = doc['title']
            wpapers.append('<h4>{title}</h4>'.format(title=title))
        

        # get the template of the front-end
        with open('page.html', 'r') as f:
            z = f.read()
        self.wfile.write(str(z.format(publications=''.join(papers),
        wpapers=''.join(wpapers))).encode())

        return
