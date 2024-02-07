import fractal
import bmp
import reprlib

"""Generate Pixel Data"""
pixels = fractal.mandelbrot(448, 256)
print(reprlib.repr(pixels))

"""Writing BMP file"""
bmp.write_grayscale("mandel.bmp", pixels)

"""Reading BMP file"""
print(bmp.dimensions("mandel.bmp"))
