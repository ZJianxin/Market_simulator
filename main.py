import sys
import numpy

def main():
    initial_order_file = sys.argv[0]
    updates_file = sys.argv[1]
    initial_order_matrix = numpy.load(initial_order_file)
    updates_matrix = numpy.load(updates_file)
    for m in numpy.mean(data, axis=1):
        print(m)

if __name__ == '__main__':
   main()