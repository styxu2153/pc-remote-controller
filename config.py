import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder-key-in-case-original-not-in-path'
    SELENIUM_DRIVER_PATH = os.environ.get('SELENIUM_DRIVER_PATH')
    SYSTEM_CONTROL_PIN = os.environ.get('SYSTEM_CONTROL_PIN') or '2153'
    