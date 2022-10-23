import math
import tkinter
import numpy


def mapValue(x, old_a, old_b, new_a, new_b):
    return (x - old_a) * ((new_b - new_a) / (old_b - old_a)) + new_a


def func(x):
    return x ** 2 + math.sin(x)


def getValues(a, b):
    return {x: func(x) for x in numpy.arange(a, b, 0.1)}


def drawFunc(canvas: tkinter.Canvas, a, b, width, height):
    data = getValues(a, b)
    mxd = max(data.values())
    mnd = min(data.values())
    for i in range(len(data) - 2):
        x1 = list(data.keys())[i]
        y1 = data[x1]
        x2 = list(data.keys())[i+1]
        y2 = data[x2]

        mx1 = mapValue(x1, a, b, width*0.1, width*0.9)
        mx2 = mapValue(x2, a, b, width*0.1, width*0.9)
        my1 = mapValue(y1, mnd, mxd, height*0.9, height*0.1)
        my2 = mapValue(y2, mnd, mxd, height*0.9, height*0.1)

        canvas.create_line(mx1, my1, mx2, my2, fill="white")

    canvas.create_line(
        0,
        mapValue(0, mnd, mxd, height*0.9, height*0.1),
        width,
        mapValue(0, mnd, mxd, height*0.9, height*0.1),
        dash=(2, 2), fill="grey")

    canvas.create_line(
        mapValue(0, a, b, width*0.1, width*0.9),
        0,
        mapValue(0, a, b, width*0.1, width*0.9),
        height,
        dash=(2, 2), fill="grey")
