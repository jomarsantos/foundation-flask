from flask import Flask, request
import yaml

app = Flask(__name__)

import routeA
@app.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return routeA.get()
    else:
        return routeA.post()

import routeB
@app.route('/api/user/<username>')
def user(username):
    return routeB.get(username)

with open("./config.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if __name__ == '__main__':
    app.run(
        host=config['server']['host'],
        debug=config['server']['debug'],
        port=config['server']['port']
    )
