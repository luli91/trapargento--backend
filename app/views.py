from flask import jsonify, request
from app.models import Tracks

def index():
    return jsonify({'message': 'Hola mundo API FLASK'})

def get_all_songs():
    tracks = Tracks.get_all()
    list_songs = [song.serialize() for song in tracks]
    return jsonify(list_songs)

def create_songs():
    data = request.json
    new_song = Tracks(
        id_songs=None,
        tittle=data['tittle'],
        duracion=str(data['duracion']),
        fecha_subida=data['fecha_subida']  # ya viene como string
    )
    new_song.save()
    return jsonify({'message': 'track creado con éxito'}), 201

def get_songs(id_songs):
    track = Tracks.get_by_id(id_songs)
    if not track:
        return jsonify({'message': 'track not found'}), 404
    return jsonify(track.serialize())

def update_songs(id_songs):
    track = Tracks.get_by_id(id_songs)
    if not track:
        return jsonify({'message': 'track not found'}), 404
    data = request.json
    track.tittle = data['tittle']
    track.duracion = str(data['duracion'])
    track.fecha_subida = data['fecha_subida']
    track.save()
    return jsonify({'message': 'track updated successfully'})

def delete_songs(id_songs):
    track = Tracks.get_by_id(id_songs)
    if not track:
        return jsonify({'message': 'track not found'}), 404
    track.delete()
    return jsonify({'message': 'track deleted successfully'})


# from datetime import datetime
# from flask import jsonify, request
# from app.models import Tracks



# def index():
#     response = {'message': 'Hola mundo API FLASK'}
#     return jsonify(response)

# # obtiene todos los tracks
# def get_all_songs():
#     tracks = Tracks.get_all()
#     list_songs = [song.serialize() for song in tracks]
#     return jsonify(list_songs)

# # crea un track
# def create_songs():
#     data = request.json
#     fecha_subida_str = data['fecha_subida']
#     fecha_subida = datetime.strptime(fecha_subida_str, '%a, %d %b %Y %H:%M:%S %Z')
#     new_song = Tracks(id_songs=None, tittle=data['tittle'], duracion=str(data['duracion']), fecha_subida=fecha_subida)
#     new_song.save()
#     return jsonify({'message': 'track creado con éxito'}), 201

# # obtiene un solo track
# def get_songs(id_songs):
#     track = Tracks.get_by_id(id_songs)
#     if not track:
#         return jsonify({'message': 'track not found'}), 404
#     return jsonify(track.serialize())


# def update_songs(id_songs):
#     track = Tracks.get_by_id(id_songs)
#     if not track:
#         return jsonify({'message': 'track not found'}), 404
#     data = request.json
#     track.tittle = data['tittle']
#     track.duracion = str(data['duracion'])
#     track.fecha_subida= data['fecha_subida']
#     track.save()
#     return jsonify({'message': 'track updated successfully'})

# def delete_songs(id_songs):
#     track = Tracks.get_by_id(id_songs)
#     if not track:
#         return jsonify({'message': 'track not found'}), 404
#     track.delete()
#     return jsonify({'message': 'track deleted successfully'})
