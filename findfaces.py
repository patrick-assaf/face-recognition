import face_recognition

image = face_recognition.load_image_file('./img/groups/group1.jpg')
face_locations = face_recognition.face_locations(image)

print(face_locations) # Array of coordinates of each face in the image

print(f'There are {len(face_locations)} people in this image')