from flask import Flask
from flask import request, make_response
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!',

 
@app.route('/hello')  # Decorator to define the URL route
def helloworld():
    response = make_response()  # Create a new response object
    response.status_code = 200  # Set the HTTP status code to 200 (OK)
    response.headers['content-type'] = 'text/plain'  # Set the response content type to plain text
    return response  # Return the response object

# routes
@app.route('/greet/')    
def greetings():
    return 'greeting, World!'

# url variables
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


# url parameters
@app.route('/handle_url_params')
def handle_params():
    greeting = request.args.get('greetings')
    name = request.args.get('name')
    return f'{greeting}!, {name}'      


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    


