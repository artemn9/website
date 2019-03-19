from http.server import BaseHTTPRequestHandler


def pretty_paper(data):
    """function converts data on published papers into html"""
    assert 'cite' in data and 'description' in data
    template = '<h3>{cite}</h3><p>{description}</p>'
    return template.format(**data)


def working_paper(data):
    """function converts data on working papers into html"""
    assert 'title' in data and 'link' in data
    if 'comment' not in data:
        data['comment'] = ''
    template = '<h3><A href="{link}" target="blank">{title}</A>'
    template += '<br />{comment}</h3><p>{description}</p>'
    return template.format(**data)


def papers(func, what):
    """function creates text with all papers in html"""
    return ''.join([func(x) for x in what])


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # get the mongodb connection:
        import pymongo
        where = 'artemn9:rDkAH8Npm5XXHaPb@artemn9-mongo-fpjxf.mongodb.net/test'
        connection = 'mongodb+srv://{where}'.format(where=where)
        client = pymongo.MongoClient(connection)
        db = client.get_database('academic')
        cl = db.get_collection('papers')

        # published papers
        published = papers(pretty_paper, cl.find({"publish": True}))

        # working papers
        working = papers(working_paper, cl.find({"publish": None}))

        # get the template of the front-end
        with open('page.html', 'r') as f:
            html_page = f.read()
        with open('page.css', 'r') as f:
            styles = f.read()
        content = {'published': published, 'working': working, 'css': styles}
        html_page = html_page.format(**content)
        self.wfile.write(html_page.encode())

        return
