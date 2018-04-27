import unicornhathd
import time
from math import cos, sin, radians

def calc_point(r, theta, shift):
    x = round(r * cos(radians(theta))) + shift 
    y = round(r * sin(radians(theta))) + shift

    return x, y


if __name__ == "__main__":
    unicornhathd.off()
    unicornhathd.brightness(0.5)

    r = 6
    start_angle = 0
    while True:
        if start_angle % 360 == 0:
            start_angle = 0
        
        theta = start_angle    
        for index in range(10):
            theta -= 10 
            x, y = calc_point(r, theta, 8)
            i, j = calc_point(r, theta, 7)

            if index == 9:
                unicornhathd.set_pixel(x, y, 0, 0, 0)
                unicornhathd.set_pixel(i, j, 0, 0, 0)
            else:
                unicornhathd.set_pixel(x, y, 200, 50, 0)
                unicornhathd.set_pixel(i, j, 200, 120, 0)
                    

        start_angle += 10
        unicornhathd.show()
        time.sleep(0.07)
