# Face Recognition
Using Python's face recognition API to find, match, and identify faces across different images.

## Commands

### Set up a virtual environment
```
$ pip install pipenv
$ pipenv shell
```

### Install the face recognition library
```
$ pipenv install face_recognition
```

### (Optional) Helpful commands for debugging
```
$ face_recognition ./img/known ./img/unknown
$ face_recognition --show-distance true ./img/known ./img/unknown
$ face_recognition --tolerance 0.55 ./img/known ./img/unknown
$ face_recognition ./img/known ./img/unknown | cut -d ',' -f2
$ face_recognition --cpus 8 ./img/known ./img/unknown
```
