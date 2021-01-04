# This file will delete the photos from the project folder
import os
def delete(path, img_type):
    for f in os.listdir(path):
        if f.endswith(img_type):
            os.remove(f)
