
import os
import cv2

__source = os.environ.get('CAM_SOURCE', 0)
try:
    __source = int(__source)
except:
    raise Exception('No es posible determinar el origen del stream')

__cam = cv2.VideoCapture(__source)

def cam():
    return __cam

def frame_rate():
    '''
    Indica la cantidad de fotogramas por segundo a las que se  procesa el recurso
    '''
    return __cam.get(5)

def current_frame():
    return __cam.get(1)

def take_pick_from_stream():
    '''Si le es posible intenta leer una imagen tomada desde el stream de origen'''
    ret, frame = cam().read()
    if not ret:
        return None
    return frame