import random
from flask import Flask, request, Response, json
app = Flask(__name__, static_url_path='')

# set DEBUG so you can see errors in your console
app.config['DEBUG'] = True

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/query', methods=['POST'])
def query():
    body = request.get_json()
    query = body.get('query')
    data = json.dumps(autocomplete(query))
    return Response(data, status=200, mimetype='application/json')

# Just a sample data set. Feel free to use something else!
mixmax_features = [
    'code snippet',
    'availability',
    'table',
    'Email tracking',
    'Giphy',
    'PDF Slideshow',
    'Article',
    'SMS Me',
    'Secret Message',
    'Encryption',
    'Poll',
    'Public Poll',
    'Send Later',
    'Send Later with tracking',
    'Markdown',
    'Link Preview',
    'Yes/No',
    'Question and Answer',
    'Forms in Email',
    'Forms in pages',
    'Cloud hosted attachments',
    'Email templates',
    'Gists',
    'Google Maps integration'
];

def autocomplete(query):
    # This picks a random element from the mixmaxFeatures array regardless of input
    # TODO Replace this with your autocomplete function
    return [random.choice(mixmax_features)]

if __name__ == '__main__':
    app.run()
