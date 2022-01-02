import face_recognition
import cv2 as cv
import numpy as np
import glob
import pickle

with open("ref_name.pkl", mode="rb") as file:
    name_dict = pickle.load(file)

with open("ref_embed.pkl", mode="rb") as file:
    embed_dict = pickle.load(file)

known_face_encodings = []
known_face_names = [] 
for ref_id , embed_list in embed_dict.items():
    for my_embed in embed_list:
        known_face_encodings +=[my_embed]
        known_face_names += [ref_id]

video_capture = cv.VideoCapture(0)
face_locations = []
face_encodings = []
face_names = []
process = True

while True:
    ret, frame = video_capture.read()
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)

    process = False
    
    for (top_s, right, bottom, left), name in zip(face_locations, face_names):
        top_s *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv.rectangle(frame, (left, top_s), (right, bottom), (0, 0, 255), 2)
        cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        font = cv.FONT_HERSHEY_DUPLEX
        cv.putText(frame, name_dict[name], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    font = cv.FONT_HERSHEY_DUPLEX
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv.destroyAllWindows()