import cv2
import face_recognition

# 识别
def identification(data):
    stu_has = []
    video_capture = cv2.VideoCapture(0)
    face_encoding = []
    face_name = []
    for k,v in data.items():
        face_name.append(k)
        # print(face_recognition.face_encodings(face_recognition.load_image_file(v))[0])
        face_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(v)))
    print(data)
    print(face_encoding,face_locations)
    # face_names = []
    process_this_frame = True
    while(True):
        ret, frame = video_capture.read()
        # print(ret,frame)
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame = small_frame[:,:,::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names = []
            for face_en in face_encodings:
                matches = face_recognition.compare_faces(face_encoding,face_en)
                name = 'Unknown'
                print(matches)
                if True in matches:
                    first_match_index = matches.index(True)
                    name = face_name[first_match_index]
                    print(name)
                face_names.append(name)
                stu_has.append(name)
        process_this_frame = not process_this_frame
        for (top,right,bottom,left),name in zip(face_locations,face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
            cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    # print(face_names,stu_has,data)
    return stu_has



if __name__ =='__main__':
    name = identification({'11122':'c:/users/slx/pictures/123.jpg'})