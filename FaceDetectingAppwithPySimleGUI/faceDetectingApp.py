""" Face Detecting and Tracking App with PySimpleGUI"""

from curses import window
import PySimpleGUI as sg
import cv2


layout = [
    [sg.Image(key= '-IMAGE-')],
    [sg.Text('Face on cam: 0', key ='-TEXT-',expand_x = True, justification= 'c')]
    ]
window = sg.Window('Face Detecting and Tracking', layout)

# Getting Video
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    
    _, frame = cam.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.3, minNeighbors = 7, minSize = (50,50)) # we can write gray instead of frame 
    
    # the first we draw rectangle 
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2) 

    # and now we update the image
    imgBytes = cv2.imencode('.png', frame)[1].tobytes()
    window['-IMAGE-'].update(data = imgBytes) 
    
    # and then we update the text
    window['-TEXT-'].update(f'Face on cam : {len(faces)}') # we figure out how many faces are being detected 

window.close()    


