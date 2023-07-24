import redis
import numpy as np
import os
import cv2

# Establecer conexión con el servidor Redis
redis_host = os.environ.get('REDIS_HOST', 'localhost')  # Cambia esto si Redis está en otro host
redis_port = os.environ.get('REDIS_PORT', 6379)         # Puerto predeterminado de Redis
redis_db = 0                                            # Base de datos de Redis a utilizar (no aplica)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
image_expire = 300

_RGB = 1
def send_to_cache(clave : str, image):
   
    # Codificar a texto la imagen
    retval, buffer = cv2.imencode('.png', image)
    image_bytes = np.array(buffer).tostring()

    # Guardar los bytes de la imagen en Redis
    stored = redis_client.set(clave, image_bytes, ex=image_expire)
    if stored:
        print("Imagen guardada en Redis con la clave:", clave)
    return stored


def get_from_cache(clave : str):
    
    # recuperar la info
    image_bytes = redis_client.get(clave)
    if image_bytes:
        return True, cv2.imdecode(np.frombuffer(image_bytes, np.uint8), _RGB)
    return False, None

def get_bytes( clave : str):
     # recuperar la info
    image_bytes = redis_client.get(clave)
    if image_bytes:
        return True, image_bytes
    return False, None

def decode_img_from_bytes( bytes):
    return cv2.imdecode(np.frombuffer(bytes, np.uint8), _RGB)
    


