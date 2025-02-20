import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

harsh_image = face_recognition.load_image_file("C:\Users\Harsh\OneDrive\Desktop\face recognition\database")
harsh_encoding = face_recognition.face_encoding(harsh_image)[0]