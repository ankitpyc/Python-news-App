import htmlPy
import os
from PyQt4 import QtCore, QtGui


def  init_configuration(app):
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))
	app.width = 500
	app.height = 300
	app.web_app.setMinimumHeight(400)
	app.developer_mode =True
	app.web_app.setMinimumWidth(660)
	app.template_path = os.path.abspath(".")
	app.static_path = BASE_DIR+"/static/"
	print app.static_path
	return app	