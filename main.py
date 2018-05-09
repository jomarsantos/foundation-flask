import yaml
from app import app

# CONFIG
with open("./config.yaml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# SERVER
if __name__ == '__main__':
    app.run(
        host=config['server']['host'],
        debug=config['server']['debug'],
        port=config['server']['port']
    )
