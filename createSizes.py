import cv2
import os
import csv

folder='/content/OIDv4_ToolKit/OID/Dataset/validation/ft'
with open('sizes.csv','wb') as file:
  for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    if img is not None:
      h, w, c = img.shape
      file.write(filename.split(".")[0]+","+str(w)+","+str(h))
file.close    
