import face_recognition as fr
import numpy as np


def get_enordings(path:str):
    face = fr.load_image_file(path)
    encoding = fr.face_encodings(face)
    return np.array(encoding)

def match_faces(face1: str, face2: str) -> list[bool]:
    return fr.compare_faces(get_enordings(face1), get_enordings(face2))


print(match_faces('images/me.jpeg', 'images/me.jpeg'))
assert match_faces('images/me.jpeg', 'images/me.jpeg'), "The two faces did not match."


print(match_faces('images/me.jpeg', 'images/me0.jpeg'))
assert match_faces('images/me.jpeg', 'images/me0.jpeg'), "The two faces did not match."

print(match_faces('images/me.jpeg', 'images/me1.jpeg'))
assert match_faces('images/me.jpeg', 'images/me1.jpeg'), "The two faces did not match."

print(match_faces('images/me.jpeg', 'images/me3.jpeg'))
assert match_faces('images/me.jpeg', 'images/me3.jpeg'), "The two faces did not match."


print(match_faces('images/me.jpeg', 'images/unnamed.jpg'))

assert not match_faces('images/me.jpeg', 'images/unnamed.jpg'), "The two faces did match."


