#!/usr/bin/env python2.6
#
# Calculate the mandelbrot set using python and/or native C.
# Copyright (C) 2009 Alejandro Segovia
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#		    
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#				    
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import pygame
import sys
import math

from ctypes import *

class Color(Structure):
	_fields_ = ("r", c_int), ("g", c_int), ("b", c_int)

	def __getitem__(self, i):
		if i == 0:
			return int(self.r)
		elif i == 1:
			return int(self.g)
		elif i == 2:
			return int(self.b)

class Canvas:
	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.surface = pygame.display.set_mode((w,h), pygame.DOUBLEBUF)
	
	def clear(self):
		self.surface.fill([0,0,0])
	
	def update(self):
		pygame.display.flip()
	
	def putpixel(self, x, y, color):
		x1 = x + self.w/2
		y1 = -y + self.h/2
		self.surface.set_at((x1,y1), color)

class Complex:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
	
	def square(self):
		real = self.real*self.real - self.imag*self.imag
		imag = 2.0 * self.real * self.imag
		return Complex(real, imag)
	
	def __add__(self, other):
		return Complex(self.real + other.real, self.imag + other.imag)
	
	def modulo(self):
		return math.sqrt(self.real * self.real + self.imag * self.imag)
	
	def __str__(self):
		return "%f + %fi" % (self.real, self.imag)
	
	def __repr__(self):
		return str(self)

def calc_set(w, h, num_iters):
	l = [(0.0, 0.0, 0.0)] * (w * h)

	for i in range(0, w):
		for j in range(h):
			ii = i - w/2.0
			jj = j - h/2.0

			c = Complex(ii * 4.0 / w, jj * 4.0 / h)

			z = Complex(0.0, 0.0)
			count = 0
			while count < num_iters and z.modulo() <= 2:
				z = z.square() + c
				count += 1
			
			if z.modulo() <= 2:
				l[j * w + i] = (int(255*z.modulo()/2.0)*0, 0, int(255*z.modulo()/2.0))

			else:
				l[j * w + i] = (0, int(255*count/num_iters), 0)

	return l

def main():
	w, h = 512, 512
	pygame.init()
	canvas = Canvas(w, h)
	canvas.clear()
	canvas.update()

	z = Complex(0.0, 0.0)
	
	num_iters = 20
	native_comp = True

	t0 = pygame.time.get_ticks()

	if not native_comp:
		colors = calc_set(w, h, num_iters)
	else:
		colors = (Color * (w * h))()
		lib = CDLL("libmandelbrot.so")
		lib.calc_set(w, h, num_iters, colors)

	tf = pygame.time.get_ticks()
	time_str = "Time: %f secs" % ((tf - t0)/1000.0)
	print time_str
	pygame.display.set_caption(time_str)
	pygame.display.set_caption("Mandelbrot Set")

	for i in xrange(w):
		for j in range(h):
			ii = i - w/2
			jj = j - h/2
			color = colors[j * w + i]
			canvas.putpixel(ii, jj, (color[0], color[1], color[2]))

	print "Done"
	canvas.update()

	while True:
		evt = pygame.event.wait()
		if evt.type == pygame.QUIT:
			sys.exit(0)
		if evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
			sys.exit(0)

if __name__ == "__main__":
	main()

