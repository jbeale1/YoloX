# YoloX
Experiments with object detection

I am experimenting with the YoloX-X detector provided by https://modelplace.ai/models/49

I find this model _mostly_ works well to locate objects like people, cars and trucks in real-world images of a driveway and road area. 
I was surprised to find one image (unmodified, direct from camera) of an empty road with a bit of snow falling, is detected as an "oven" object, with object boundaries enclosing nearly the entire frame, at 90.5% confidence. It would be interesting to know how that happens, but large networks are difficult to interpret.

DH5_211226_035952_960.jpg, 0,1, 1276,707, 0.905, oven
