import sys
import cv2 as cv
import face_recognition
import pickle

name=input("enter name: ")
ref_id=input("enter id: ")

try:
    with open("ref_name.pkl", mode="rb") as file:
        name_dict = pickle.load(file)
except:
    name_dict = {}

name_dict[ref_id] = name

with open("ref_name.pkl", mode="wb") as file:
    pickle.dump(name_dict, file)

try:
    with open("ref_embed.pkl", mode="rb") as file:
        embed_dict = pickle.load(file)

except:
    embed_dict = {}

image = cv.imread("../data/student_image/2440005164.jpg")

small_image = cv.resize(image, (0, 0), fx=0.5, fy=0.5)
rgb_small_image = small_image[:, :, ::-1]

face_loc = face_recognition.face_locations(image)
if face_loc != []:
    face_encode = face_recognition.face_encodings(image)
    
    if ref_id in embed_dict:
        embed_dict[ref_id] += [face_encode]
    else:
        embed_dict[ref_id] = [face_encode]

key = cv.waitKey(0)

with open("ref_embed.pkl", mode="wb") as file:
    pickle.dump(embed_dict, file)

while True:
    cv.imshow("Open CV Image Reading", image)

    if key == ord("q"):
        cv.destroyAllWindows()
        break

# key = cv2. waitKey(1)
# webcam = cv2.VideoCapture(0)
# while True:

#     check, frame = webcam.read()
#     cv2.imshow("Capturing", frame)
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     rgb_small_frame = small_frame[:, :, ::-1]

#     key = cv2.waitKey(1)
#     if key == ord('s') : 
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         if face_locations != []:
#             face_encoding = face_recognition.face_encodings(frame)[0]
#             if ref_id in embed_dict:
#                 embed_dict[ref_id]+=[face_encoding]
#             else:
#                 embed_dict[ref_id]=[face_encoding]
#             webcam.release()
#             cv2.waitKey(1)
#             cv2.destroyAllWindows()     
#             break
#     elif key == ord('q'):
#         print("Turning off camera.")
#         webcam.release()
#         print("Camera off.")
#         print("Program ended.")
#         cv2.destroyAllWindows()
#         break


