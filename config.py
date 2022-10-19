# All the configuration items are in this file
# JSON_AS_ASCII = False

# Database Configuration
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'now_flask'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True


