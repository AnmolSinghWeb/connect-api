import json
import os
from flask_restful import Api
from flask import Flask, jsonify, request
from waitress import serve
from api.routes import init as ntfta_init
from api.root import init as root_init
import chromadb

# client = chroma_client = chromadb.HttpClient(host='localhost', port=8000)

application = appobj = Flask(__name__)
app = Api(appobj)

PORT = os.getenv('PORT', '80')
BIND_ADDRESS = os.getenv('BIND_ADDRESS', '0.0.0.0')
ENV = os.getenv('ENV', 'development')

root_init(app)
ntfta_init(app)

def start_server():
    serve(appobj, host='0.0.0.0', port=8080, threads=100)

def main(start=True):
    if start:
        print('Starting feathery-api')
        serve(application, host='0.0.0.0', port=8080, threads=100)
        # collection = client.create_collection(name="my_collection", embedding_function='emb_fn')
        # collection = client.get_collection(name="my_collection", embedding_function='emb_fn')
        # print(collection)
        print('here')

if os.environ.get('ENV') == 'development':
    print('Starting nt-api')
    print('ENV: development')
    print('dev')
    start_server()
elif os.environ.get('ENV') == 'production':
    print('Starting nt-api')
    print('ENV: production')
    if __name__ == '__main__':
        serve(application, host=BIND_ADDRESS, port=int(PORT), threads=100)
