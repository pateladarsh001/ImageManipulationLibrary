## IMAGE MANIPULATION LIBRARY

## Introduction
This library allows manipulating PGM based images using NumPy only.

## Functionality
 Some the manipulation functions that are in the library are: (*More functions may be added in the future*)
 
 - Reflect the image left to right, and right to left
 - Invert black and white pixel values
 - Increase the relative brightness of the image without exceeding the maximum pixel value of the given image/data set

## Requirements
Please note that the following requirements are suggested to make sure that the the library is utilized optimally: (*More flexibility in terms of image types and image sizes and pixel values might be added later*)

 - The following assumptions have been made regarding the format of the PGM file:
 
	The header of a PGM file has the form:
	
	P2
	20 30
	255
	
	where P2 indicates a PGM file with ASCII encoding,
	and the next three numbers are the number of columns in the image,
	the number of rows in the image, and the maximum pixel value.
	
	Comments are indicated by # and could occur anywhere in the file.
	For simplicity, it is assumed that a # is preceded by whitespace.
	
	The remaining entries are pixel values.
 
 - The PGM file contains pixel values in **grayscale format**, where the maximum value is 255(white) and minimum value is 0(black).
 - The library file(s) must be kept in the same folder as the image(s) folder

## 

> Last updated on December 22nd, 2020.
