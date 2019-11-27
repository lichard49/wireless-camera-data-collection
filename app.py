from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/capture_picture', methods=['POST'])
def capture_picture():
    file_name = request.headers.get('file_name')
    print('request take picture and save to: ' + file_name)
    return {'status': 'success', 'data': file_name}

if __name__ == '__main__':
	app.run()