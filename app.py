from flask import Flask
import socket          #This module is used to get IP 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'welcome to my world'

@app.route('/name')
def name():
    return 'First-web'    #Simply for testing purpose, you can add your own sentence here

@app.route('/ip')
def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
