from adafruit_circuitplayground.express import cpx
def pattern1():
    cpx.pixels[0] = (29,23,49)
    cpx.pixels[1] = (11,33,3)
    cpx.pixels[2] = (33,4,40)
    cpx.pixels[3] = (20,40,46)
    cpx.pixels[4] = (46,10,2)
    cpx.pixels[5] = (41,20,15)
    cpx.pixels[6] = (23,8,31)
    cpx.pixels[7] = (37,19,1)
    cpx.pixels[8] = (46,19,15)
    cpx.pixels[9] = (20,0,43)
    return None

def pattern2():
    cpx.pixels[0] = (46,48,48)
    cpx.pixels[1] = (43,12,38)
    cpx.pixels[2] = (44,41,5)
    cpx.pixels[3] = (27,41,3)
    cpx.pixels[4] = (6,10,42)
    cpx.pixels[5] = (20,37,26)
    cpx.pixels[6] = (43,41,23)
    cpx.pixels[7] = (14,34,14)
    cpx.pixels[8] = (16,14,25)
    cpx.pixels[9] = (45,18,0)
    return None

def pattern_random():
    from random import random
    for pixel_num in range(10):
        cpx.pixels[pixel_num] = (random()*50,random()*50,random()*50)
