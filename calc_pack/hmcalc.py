#!/usr/bin/python

def tiles(width, height, tWidth, tHeight):
	area = width * height
	tile = tWidth * tHeight
	return area / tile

	
def paint(width, height, performance):
	area = width * height
	return area / performance
	
def panels(width, height, tWidth, tHeight):
	area = width * height;
	panel = tWidth * tHeight;
	return area / panel
