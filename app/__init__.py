from flask import Flask

app = Flask(__name__)
from app import views

def run(server='waitress'):
	if 'waitress' == server:
		from waitress import serve
		import logging
		logger = logging.getLogger('waitress')
		logger.setLevel(logging.INFO)
		#app.run(host='0.0.0.0')
		#We now use this syntax to server our app. 
		serve(app, host='0.0.0.0', port=5050)
	else:
		app.run(host='0.0.0.0', port=5050, debug=True)
