import math


__all__ = (
    'circle',
    'rectangle',
    'triangle'
)


def circle(r):
    return math.pi*(r**2)


def rectangle(a, b):
    return a*b


def triangle(d, h):
    return 0.5*d*h
