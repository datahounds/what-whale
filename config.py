import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    OUTPUT_DIR = os.path.join(basedir, 'static')
    SIZE = 224  # image width and height
