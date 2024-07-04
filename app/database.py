import os
import mysql.connector
from flask import g
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306))
}
#funmcion para obtener la conexion a la base de datos
def get_db():
    #si "db" no está en el contexto global de flask 'g'
    if 'db' not in g:
        #crear una nueva conexion a la base de datos 
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
        # retorna la conexion a la base de datos
    return g.db

# funcion para cerrar la conexion a la base de datos
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# funcion para inicializar la aplicacion
def init_app(app):
    app.teardown_appcontext(close_db)