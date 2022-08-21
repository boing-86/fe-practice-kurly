import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI : DB접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'project_1.db'))

# SQLALCHEMY_TRACK_MODIFICATIONS : SQLAlchemy 이벤트 처리 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"