from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import threading
import time

def Home(request):
    return render(request, 'signovatio/base.html')

# def process_image(request):
#     # Get the path to the media file (assuming the image is stored in the media folder)
#     media_path = os.path.join(settings.MEDIA_ROOT, 'your_image.jpg')

#     # Read the image using OpenCV
#     img = cv2.imread(media_path)

#     # Convert the image to grayscale
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Save the processed image (you can skip this step if you just want to display it)
#     # processed_image_path = os.path.join(settings.MEDIA_ROOT, 'processed_image.jpg')
#     # cv2.imwrite(processed_image_path, gray_img)

#     # Display the original and processed images in the browser
#     return render(request, 'signovatio/process_image.html', {'original_image': media_path, 'processed_image': gray_img})



# class VideoCamera:
#     def init(self):
#         self.video = cv2.VideoCapture(0)
#         _, self.frame = self.video.read()
#         self.is_running = True
#         self.thread = threading.Thread(target=self.update, args=())
#         self.thread.daemon = True
#         self.thread.start()

#     def __del__(self):
#         self.video.release()

#     def getframe(self):
#         _, jpeg = cv2.imencode('.jpg', self.frame)
#         return jpeg.tobytes()

#     def update(self):
#         while self.isrunning:
#             _, self.frame = self.video.read()
#             time.sleep(0.1)  # Adjust the sleep time if needed

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# def webcam_feed(request):
#     return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')