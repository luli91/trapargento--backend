🐍 Trap Argento — Backend API
API RESTful construida con Flask y Python, conectada inicialmente a una base de datos MySQL relacional durante el desarrollo y migrada a SQLite para facilitar el deploy gratuito en Render. Gestiona canciones y proporciona endpoints CRUD para el frontend del proyecto.

⚙️ Tecnologías utilizadas
Python 3

Flask

Flask-CORS

SQLite (para producción)

MySQL (utilizado en desarrollo)

dotenv (para configuración inicial)

📚 Estructura de carpetas
TrapArgento-backend/
├── argentrap.db              # Base de datos SQLite usada en deploy
├── database.py               # Conexión (SQLite activa, MySQL comentado)
├── run.py                    # Punto de entrada Flask
├── requirements.txt
├── Procfile
└── app/
    ├── __init__.py
    ├── models.py
    └── views.py
🔌 Endpoints principales
Método	Ruta	Descripción
GET	/	Hello World
GET	/api/songs/	Listar canciones
POST	/api/songs/	Crear canción
GET	/api/songs/<id>	Obtener canción por ID
PUT	/api/songs/<id>	Actualizar canción
DELETE	/api/songs/<id>	Eliminar canción
⚙️ Configuración local
Cloná este repositorio y accedé al proyecto:

bash
git clone <repo>
cd TrapArgento-backend
Instalá las dependencias:

bash
pip install -r requirements.txt
Iniciá el servidor:

bash
python run.py
La API estará disponible en http://127.0.0.1:5000/

💾 Base de datos
Este backend fue desarrollado inicialmente con MySQL para aprovechar relaciones relacionales y claves foráneas. Para deploy gratuito en Render, se migró a una base SQLite sin perder la integridad del modelo. El archivo argentrap.db contiene datos reales de artistas, álbumes, canciones, seguidores y reseñas.

📝 El código original con soporte para MySQL sigue comentado en los archivos (database.py, models.py, etc.) para conservar esa funcionalidad.

🔁 Relación con el frontend
Este backend expone la API consumida por el proyecto TrapArgento Frontend, que permite visualizar y gestionar el catálogo musical completo a través de la interfaz React.