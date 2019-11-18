#!/usr/bin/env python3.8

from star import Star
from star_graphic import graph_window, GraphStarInfo, GraphStar
import conf
import time

ITERATIONS = 4 * conf.get_intvalue('SPEED', 'STAGE_ITERATIONS')

if __name__ == "__main__":
    lum = float(input('Enter luminosity: '))
    rad = float(input('Enter radius: '))
    temp = float(input('Enter temperature: '))
    mass = float(input('Enter mass: '))
    star = Star(lum, rad, temp, mass)
    graph_star = GraphStar(star)
    graph_star.draw(graph_window)
    graph_info = GraphStarInfo(star)
    graph_info.draw(graph_window)

    for i in range(ITERATIONS):
        star.grow_up()
        graph_star.update(graph_window)
        graph_info.update(graph_window)
        time.sleep(0.1)
    input()