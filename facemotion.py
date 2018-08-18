import face_recognition


image = face_recognition.api.load_image_file("source_photo/01.JPG")
face_locations = face_recognition.api.face_locations(image, number_of_times_to_upsample=1,model="hog")

print(face_locations)
