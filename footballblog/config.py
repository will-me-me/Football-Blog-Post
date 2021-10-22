import os


class Config:
    SECRET_KEY = 'e15459ff997d35ae64844279c0d0fa6e'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS = 'True'
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
