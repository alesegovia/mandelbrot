/**
 * Calculate the mandelbrot set in C.
 * Copyright (C) 2009 Alejandro Segovia
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *		    
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *				    
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 **/
#include <complex.h>
#include <math.h>

typedef struct Color
{
	int r,g,b;
} Color;

float modulo(complex z)
{
	return sqrt(creal(z)*creal(z) + cimag(z)*cimag(z));
}

complex cmplx_square(complex z)
{
	float real = creal(z)*creal(z) - cimag(z)*cimag(z);
	float imag = 2.0 * creal(z) * cimag(z);
	return real + I*imag;
}

complex cmplx_add(complex a, complex b)
{
	return (creal(a) + creal(b)) + I * (cimag(a) + cimag(b));
}

int calc_set(int w, int h, int num_iters, Color* pset)
{
	int i, j;
	for (i = 0; i < w; i++)
	{
		for (j = 0; j < h; j++)
		{
			int ii = i - w/2.0f;
			int jj = j - h/2.0f;

			complex c = ii*4.0f/w + jj*4.0f/h*I;
			complex z = 0.0f + 0.0f*I;

			int count = 0;
			while (count < num_iters && modulo(z) <= 2.0f)
			{
				z = cmplx_add(cmplx_square(z), c);
				++count;
			}

			if (modulo(z) <= 2)
			{
				pset[j * w + i].r = 0;
				pset[j * w + i].g = 0;
				pset[j * w + i].b = (int)(255*modulo(z)/2.0f);
			}
			else
			{
				pset[j * w + i].r = 0;
				pset[j * w + i].g = (int)(255*count/num_iters);
				pset[j * w + i].b = 0;

			}
		}
	}
	return 0;
}

