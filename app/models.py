from app.database import get_db

class Tracks:
    def __init__(self, id_songs=None,tittle=None, duracion=None, fecha_subida=None):
        self.id_songs = id_songs
        self.tittle = tittle
        self.duracion = duracion
        self.fecha_subida = fecha_subida
        
    @staticmethod
    def get_by_id(id_songs):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM songs WHERE id_songs = %s", (id_songs,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Tracks(id_songs=row[0], tittle=row[1], duracion=row[2], fecha_subida=row[3])
        return None

    @staticmethod
    def get_all():
        db = get_db()
        #ejecuta instrucciones sql y permite extraer los resultados de esas consultas
        cursor = db.cursor()
        cursor.execute("SELECT * FROM argentrap.songs")
        rows = cursor.fetchall()
        # creo una lista de objeto
        canciones = [Tracks(id_songs=row[0],tittle=row[1], duracion=str(row[2]), fecha_subida=row[3],) for row in rows]
        cursor.close()
        return canciones
    
    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id_songs:
            cursor.execute("""
                UPDATE songs SET tittle = %s, duracion = %s, fecha_subida = %s
                WHERE id_songs = %s
            """, (self.tittle, self.duracion, self.fecha_subida))
        else:
            cursor.execute("""
                INSERT INTO songs (tittle, duracion, fecha_subida) VALUES (%s, %s, %s)
            """, (self.tittle, self.duracion, self.fecha_subida))
            self.id_songs = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM songs WHERE id_songs = %s", (self.id_songs,))
        db.commit()
        cursor.close()

    # devolvemos un diccionario con los elementos que traje en artistas linea 20
    def serialize(self):
        return{
        'id_songs': self.id_songs,
        'tittle': self.tittle,  
        'duracion': str(self.duracion),  
        'fecha_subida': self.fecha_subida,  
        }