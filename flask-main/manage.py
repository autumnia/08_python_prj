# -*- coding: utf-8 -*-
import os
import sys
from config import Config
from apps.controllers.router import app as application
from apps.common.commands.manager import manager

# print( "Config.ROOT_DIR: " + Config.ROOT_DIR )
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    activate_this = '{0}/venv/bin/activate_this.py'.format(Config.ROOT_DIR)
    with open(activate_this) as f:
        exec(f.read(), dict(__file__=activate_this))
except FileNotFoundError:
    activate_this = '{0}/venv/Scripts/activate_this.py'.format(Config.ROOT_DIR)
    with open(activate_this) as f:
        exec(f.read(), dict(__file__=activate_this))

if __name__ == '__main__':
    manager.run()

