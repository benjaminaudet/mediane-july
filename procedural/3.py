import sys


def compute_rect_surface(height, width):
    return height * width


if len(sys.argv) <= 1:
    print('need 2 integer arguments')
    exit(-1)

print(compute_rect_surface(int(sys.argv[1]), int(sys.argv[2])))
