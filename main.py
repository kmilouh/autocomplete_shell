#!/usr/bin/python3
import zipfile
import os
import re
import string
import base64
from bottle import route, response, static_file, run, debug
from pathlib import Path
from json import dumps
from log_helper import LogHelper
from models import LanguageModelException, ModelBase



# Logs
loghelper = LogHelper()
logger = loghelper.getLogger("default")
logger.info("Start App")

# Default Models
# You can add the number of models that you implement.
model = [ModelBase(logger),
         ModelBase(logger, "X-ES-parl"),
         ModelBase(logger, "Y-EN-parl"),
         ModelBase(logger, "Z-ES-news")
         ]

# You must set here the info messages for all the models that you implement.
info = [{"name": model[0].message, "value": "Model Base(this is a Foo Model )"},
        {"name": model[1].message,
            "value":"Model in ES trained from X with dictionary Size 144760, size of corpus 300 MB"},
        {"name": model[2].message,
            "value":"Model in EN trained from Y with dictionary Size 78839, size of corpus 310.1 MB"},
        {"name": model[3].message,
            "value":"Model in ES trained from Z with dictionary Size 74666, size of corpus 28.3 MB"},
        ]


def runServer(httpPort=9000):

    debug(True)
    global logger
    # Load Spanish Model
    # You can load the trained models here.

    @route('/')
    def send_static_index():
        logger.info("Request index.html")
        return static_file("index.html", root='./static/')

    @route('/models')
    def send_models():
        return dumps(info, ensure_ascii=False).encode('utf8')

    @route('/complete/<modelbase>/<length>/<words>')
    def send_autocomplete(modelbase, length, words):
        response.content_type = 'application/json'
        modelbase = int(modelbase)
       
        if modelbase < 0 or modelbase > len(model):
            message_error = "ModelBase Number {0} not exist".format(modelbase)
            logger.error(message_error)
            ret = {"Error": message_error}
            return dumps(ret, ensure_ascii=False).encode('utf8')
        try:
            wordList = words.split("$")
            ret = model[modelbase].predict(wordList, int(length))
            return dumps({"words": ret}, ensure_ascii=False).encode('utf8')
        except Exception as ex:
            logger.exception("Exception: {0}".format(str(ex)))
            ret = {"Error": str(ex)}
            return dumps(ret, ensure_ascii=False).encode('utf8')

    @route('/<filename:path>')
    def send_static(filename):
        logger.info("Request {0}".format(filename))
        return static_file(filename, root='./static/')

    run(host='localhost', port=httpPort)

runServer()



