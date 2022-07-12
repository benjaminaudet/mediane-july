import sys

if len(sys.argv) <= 1:
    print('need one argument to be passed')
    exit(-1)

if sys.argv[1] % 15 == 0:
    print('{} is a multiple of 15!'.format(sys.argv[1]))
    exit(0)
print('{} is not multiple of 15!'.format(sys.argv[1]))
