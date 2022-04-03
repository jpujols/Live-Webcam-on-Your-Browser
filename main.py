import cv2
from flask import Flask, render_template, Response

#Cameras goes by index. 0 Laptop 1 Desktop
video = cv2.VideoCapture(1)

#Video Frames Generator
def get_frame():
    while True:
        #If the frame is capture, it will be stored on the success key
        success, frame = video.read()
        #sc holds the true or false value captured on the turple and encodes the frame in jpg format
        sc, encoded_image = cv2.imencode('.jpg', frame)
        #Then the frame is converted to bytes
        frame = encoded_image.tobyte()
        #Generator function
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#Flask Instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_url')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

#To view the camera froma another computer, make sure your PC is listening to port (your choice)
#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0', port=5001)