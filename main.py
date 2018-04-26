import unicornhathd
import time
from math import cos, sin, radians

def calc_point(r, theta, shift):
    x = round(r * cos(radians(theta))) + shift 
    y = round(r * sin(radians(theta))) + shift

    return x, y

if __name__ == "__main__":
    unicornhathd.off()
    unicornhathd.brightness(0.6)

    r = 6
    start_angle = 0
    while True:
        if start_angle % 360 == 0:
            start_angle = 0
        
        theta = start_angle    
        for unuse in range(15):
            theta += 5
            x, y = calc_point(r, theta, 8)
            i, j = calc_point(r, theta, 7)
            unicornhathd.set_pixel(x, y, 200, 50, 0)
            unicornhathd.set_pixel(i, j, 200, 120, 0)

        start_angle += 30 
        unicornhathd.show()
        time.sleep(0.08)
        unicornhathd.off()
