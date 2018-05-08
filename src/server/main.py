from flask import Flask
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Worlds!"

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
