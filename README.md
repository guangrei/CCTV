# CCTV
turn your old android phone into remote CCTV with qpython.

## RUN

- connect to wifi.
- install [qpycmd](https://github.com/guangrei/Qpy-CMD)
- run this project from qpython application.
- put your phone in the right place.
- from other device (phone/computer) with same network open http://your-ip:8000

now you can start/stop webcam (mjpegstream), record video and take pictures.

## Problem solving

- make sure your qpython app has  camera permission.
- make sure your qpython app excluded from battery saving list.
- known bug [cant startwebcam](https://stackoverflow.com/questions/14159483/setparameters-failed-when-initializing-android-webcam-with-python-and-sl4a) and [solution](https://github.com/olapaola/olapaola-android-scripting).

## Improve

the fronted is not yet designed, your contribute are welcome :)