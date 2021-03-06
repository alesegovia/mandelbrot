Mandelbrot
==========

Sample program that calculates the mandelbrot set and shows how to use the Python ctypes interface. This program was written as the synthetic benchmark for a tech talk part of the 2011 PyDay event.

The script mandelbrot.py can calculate the mandelbrot set using two different implementations: one in pure python and one in C, using ctypes. The objective was to show how to speed up Python programs using the power
of native code.

More details about this project, as well as the results for the synthetic benchmark that compares the pure Python vs the C-backend implementation, can be found in [my Blog](http://www.alejandrosegovia.net/2013/05/20/the-mandelbrot-project/).

To run the code using the Python implementation, you will need pygame. To run the code using the native implementation, you will have to have a C build system available (preferrably on an UNIX environment). Run the Makefile script to compile the shared library.

To execute the script, just run mandelbrot.py. By default, the script  attempts to run the native version. Change the native_comp variable to False to switch to the Python version.

If successful, you should get and image like this, along with the compute time printed in the standard output.

![ScreenShot](https://raw.github.com/alesegovia/mandelbrot/master/out.png)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

