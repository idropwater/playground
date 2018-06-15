import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'YOU WILL NEWVER GUSS'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # Flask-SQLAlchemy 扩展需要，数据库文件的路径
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # SQLAlchemy-migrate 数据文件存储在这里