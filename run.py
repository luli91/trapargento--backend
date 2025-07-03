from flask import Flask
from flask_cors import CORS  
from database import init_app
from app.views import create_songs, delete_songs, get_all_songs, get_songs, index, update_songs

# Crear instancia de Flask
app = Flask(__name__)

# Inicializa conexión a DB y CORS
init_app(app)
CORS(app)

# Rutas
app.route('/', methods=['GET'])(index)
app.route('/api/songs/', methods=['GET'])(get_all_songs)
app.route('/api/songs/', methods=['POST'])(create_songs)
app.route('/api/songs/<int:id_songs>', methods=['GET'])(get_songs)
app.route('/api/songs/<int:id_songs>', methods=['PUT'])(update_songs)
app.route('/api/songs/<int:id_songs>', methods=['DELETE'])(delete_songs)

# Ejecutar local
if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask
# from flask_cors import CORS  
# from database import init_app
# from app.views import create_songs, delete_songs, get_all_songs, get_songs, index, update_songs


# # Crear una instancia de Flask
# app = Flask(__name__)

# init_app(app)

# CORS(app)
# # asosiacion de rutas con vistas

# app.route('/',methods=['GET'])(index)
# app.route('/api/songs/',methods=['GET'])(get_all_songs)
# app.route('/api/songs/',methods=['POST'])(create_songs)
# app.route('/api/songs/<int:id_songs>',methods=['GET'])(get_songs)
# app.route('/api/songs/<int:id_songs>',methods=['PUT'])(update_songs)
# app.route('/api/songs/<int:id_songs>',methods=['DELETE'])(delete_songs)


# #permite separar el codigo que se ejecuta cuando corre el servidor
# if __name__=='__main__':
#     app.run(debug=True)