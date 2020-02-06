import face_recognition
from PIL import Image, ImageDraw

obama_image = face_recognition.load_image_file('./img/known/barack-obama.jpg')
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

trump_image = face_recognition.load_image_file('./img/known/donald-trump.jpg')
trump_face_encoding = face_recognition.face_encodings(trump_image)[0]

# Create an array of encodings and names
known_face_encodings = [
    obama_face_encoding,
    trump_face_encoding
]

known_face_names = [
    "Barack Obama",
    "Donald Trump"
]

# Load test image to find faces in 
test_image = face_recognition.load_image_file('./img/groups/obama-and-trump.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

# Delete the ImageDraw instance from memory (recommended by documentation)
del draw

# Display image
pil_image.show()
pil_image.save('face_recognition.jpg')
