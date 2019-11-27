from flask import Flask, render_template, request
import urllib2
import os
import socket

app = Flask(__name__, static_folder='static')
IP_ADDRESS = 'http://192.168.10.1/'

@app.route('/')
def hello_world():
	return render_template('index.html', ip_address=IP_ADDRESS)

@app.route('/capture_picture', methods=['POST'])
def capture_picture():
    file_name = request.headers.get('file_name')

    image_request = urllib2.Request(IP_ADDRESS + 'media/?action=snapshot')
    image_request.add_header('Authorization', b'Basic ' + ('admin' + b':' + '').encode('base64').replace('\n', ''))
    image = urllib2.urlopen(image_request).read()
    open(os.path.join('data', file_name), 'wb').write(image)

    return {'status': 'success', 'data': file_name}

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    else:
        print 'data dir already exists'

    app.run()