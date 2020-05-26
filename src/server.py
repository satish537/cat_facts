from flask import Flask, request
import logging
import json
from flask import jsonify

logger = logging.getLogger(__name__)
global data
app = Flask(__name__)
logging.basicConfig(filename='server.log', level=logging.DEBUG,filemode='w',
            format='%(name)s - %(levelname)s - %(message)s')
@app.route('/facts',methods=['POST'])
def post_data():
    try:
        data = json.loads(request.data)
        logging.debug('%s Post data Recieved',data)
        with open("facts.txt", 'w') as outfile:
            json.dump(data, outfile)

    except:
        logging.error('%s Error while recieving data',data)

@app.route('/facts',methods=['GET'])
def get_data():
    with open('facts.txt') as json_file:
        data = json.load(json_file)
    '''fp=open("facts.txt","r")
    data=fp.read()
    fp.close()'''
    logging.debug('%s Data sent to client ',data)
    return jsonify(data)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
