Mandelbrot
==========

Sample program that calculates the mandelbrot set. This program was written
as the synthetic benchmark for a tech talk part of the 2011 PyDay event.

The script mandelbrot.py can calculate the mandelbrot set using two 
different implementations: one in pure python and one in C, using ctypes.
The objective was to show how to speed up Python programs using the power
of native code.

To run the code using the Python implementation, you will need pygame. To 
run the code using the native implementation, you will have to have a C
build environment available (preferrably on an UNIX environment). Run the
Makefile script to compile the shared library.

To execute the script, just run mandelbrot.py. By default, the script 
attempts to run the native version. Change the native_comp variable to False
to switch to the Python version.

