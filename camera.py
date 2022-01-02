import cv2

class VideoCamera(object):
    def __init__(self):
        # Использование OpenCV для захвата с устройства 0. Если у вас возникли проблемы с захватом
        # с веб-камеры прокомментируйте строку ниже и используйте видеофайл
        # вместо этого.
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # Если вы решите использовать video.mp4, у вас должен быть этот файл в папке
        # как main.py .
        # self.video = cv2.видеозапись ('видео.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # Мы используем Motion JPEG, но OpenCV по умолчанию захватывает необработанные изображения,
        # поэтому мы должны закодировать его в JPEG, чтобы правильно отобразить
        # видеопоток
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
