# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_script import Server

from app.settings import config

from app.application import create_app

app = create_app(config['development'])

manager = Manager(app)

manager.add_command("runserver", Server(host='0.0.0.0', port=5555))

if __name__ == '__main__':
    manager.run()
