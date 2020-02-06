import face_recognition

gates_image = face_recognition.load_image_file('./img/known/bill-gates.jpg')
gates_face_encoding = face_recognition.face_encodings(gates_image)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/gates-2.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces([gates_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is the same person')
else:
    print('This is not the same person')
