import os
import sys

from JJEchart import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

'''
sqlite 配置
'''
#dev_db = prefix+os.path.join(os.path.dirname(app.root_path),'data.db')
#SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)