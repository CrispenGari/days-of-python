### Face Recognition

In this one we are going to use the [face_recognition library](https://github.com/ageitgey/face_recognition) module in doing the following:

1. Match faces
2. Detect Faces
3. Recognizing common faces can be found https://github.com/CrispenGari/opencv-python/blob/main/facerecognition/Face%20Recognition.ipynb

First things first we need to install the `face_recognition`. But before you do that you need to follow the following steps:

1. Check your python version (I'm using `3.11`)
2. Go to [Dlib_Windows_Python3.x](https://github.com/z-mahmud22/Dlib_Windows_Python3.x) and download the `.whl` file for your python version. In my case i will put it in the `dlib` folder
3. Now you can install `dlib` by running the following command

```shell
pip install "dlib/dlib-19.24.1-cp311-cp311-win_amd64.whl"
```

Now you can install `face_recognition` library by running the following command:

```shell
pip3 install face_recognition
```

4. We are also going to install `opencv` by running the following command:

```shell
pip install opencv-python
```

#### 1. Matching faces

In the following code sample we are going to check if the two faces matches using the face library.

```py
import face_recognition as fr
import numpy as np


def get_enordings(path:str):
    face = fr.load_image_file(path)
    encoding = fr.face_encodings(face)
    return np.array(encoding)

def match_faces(face1: str, face2: str) -> list[bool]:
    return fr.compare_faces(get_enordings(face1), get_enordings(face2))

matches = match_faces('images/me.jpeg', 'images/me0.jpeg')

print("The two faces: ", "mached." if matches else "did not match.")

# testing

assert all(match_faces('images/me.jpeg', 'images/me0.jpeg')), "The two faces did not match."
assert all(match_faces('images/me.jpeg', 'images/me1.jpeg')), "The two faces did not match."
assert all(match_faces('images/me.jpeg', 'images/me3.jpeg')), "The two faces did not match."
assert not all(match_faces('images/me.jpeg', 'images/unnamed.jpg')), "The two faces did match."

```

#### 2. Detecting faces

This is how you can detect faces using the face recognition library.

```py
import face_recognition as fr
import matplotlib.pyplot as plt
import cv2

me = fr.load_image_file('images/me.jpeg')
faces = fr.face_locations(me)

for  (top, right, bottom, left)in faces:
    frame = cv2.rectangle(me, (left, top), (right, bottom), (0, 0, 255), 3)

plt.imshow(frame)
plt.show()

```
