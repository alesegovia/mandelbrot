# Calculate the mandelbrot set using python and/or native C.
# Alejandro Segovia - asegovi@gmail.com - 2011/08/19
CC=gcc
CFLAGS=-O3 -Wall
all:
	$(CC) $(CFLAGS) -c libmandelbrot.c -o libmandelbrot.o
	$(CC) $(CFLAGS) -dynamiclib libmandelbrot.o -o libmandelbrot.so
