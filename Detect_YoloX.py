# Detect objects in a set of images
# using YoloX-X from https://modelplace.ai/models/49
# J.Beale Nov. 2021

import sys
import os
from PIL import Image
from onnx_yolox import InferenceModel  # import the AI Model
from modelplace_api import Device


def run_model(dirPath: str, outPath: str):
    thresh = 0.75   # probability threshold to accept as valid object
    model = InferenceModel()  # Initialize a model
    model.model_load(Device.cpu)  # Loading a model weights
    
    for file in os.listdir(dirPath):
      filename = os.fsdecode(file)
      if filename.endswith(".jpg") : 
        fname = os.path.join(dirPath, filename)    
        image = Image.open(fname).convert("RGB")  # Read an image
        rlist = model.process_sample(image)  # Processing an image
        for e in rlist:
          if (e.score > thresh):
            print("%s, %d,%d, %d,%d, %5.3f, %s" % 
              (filename,e.x1,e.y1,e.x2,e.y2,e.score,e.class_name))
            im = image.crop((e.x1,e.y1,e.x2,e.y2))  
            # im.show()
            fnew = filename.replace(".jpg","_"+e.class_name) + ".jpg"
            fout = os.path.join(outPath, fnew)
            im.save(fout, "JPEG")
    return rlist


if __name__ == "__main__":
    imageDir = sys.argv[1]  # directory of images to process
    outDir = sys.argv[2]    # output directory
    rlist = run_model(imageDir, outDir)
