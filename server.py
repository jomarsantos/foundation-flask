import app
import app.main
import yaml

# SERVER
if __name__ == '__main__':
    app.main.flask_app.run(
        host=app.config['server']['host'],
        debug=app.config['server']['debug'],
        port=app.config['server']['port']
    )
