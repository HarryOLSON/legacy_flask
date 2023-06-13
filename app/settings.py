# -*- coding: utf-8 -*-

import os


class Config(object):

    DEBUG = False
    TESTING = False

    # mail settings
    # extract env var
    MAIL_SERVER = 'abc.343.com'
    MAIL_PORT = 25

    # mail authentication
    MAIL_USERNAME = 'user'
    MAIL_PASSWORD = '123'


class DevelopmentConfig(Config):

    ENV = 'development'
    DEBUG = True

    # session
    CSRF_ENABLED = True
    SECRET_KEY = "asgSfsf3Xd8ffy]fw8vfd0zbvssqwertsd4sdwe"

    # datebase
    SQLALCHEMY_DATABASE_URI = "mysql://root:abc123@localhost/new-blog"
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):

    ENV = 'testing'
    TESTING = True


class StagingConfig(Config):

    ENV = 'staging'
    TESTING = True

class ProductionConfig(Config):

    ENV = 'production'
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
