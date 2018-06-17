#!/usr/bin/python

"""@package hmcalc
Documentation for this module.
"""

def tiles(width, height, tWidth, tHeight):
	"""Calculates how many tiles does one need
	for given area
	@param width: area's width
	@param height: area's height
	@param tWidth: tile's width
	@param tHeight: tiles's height"""
	area = width * height
	tile = tWidth * tHeight
	return area / tile

	
def paint(width, height, performance):
	"""Calculates how many paint does one need
	for given area
	@param width: area's width
	@param height: area's height
	@param performance: paint performance/m^2"""
	area = width * height
	return area / performance
	
def panels(width, height, tWidth, tHeight):
	"""Calculates how many panels does one need
	for given area
	@param width: area's width
	@param height: area's height
	@param tWidth: panel's width
	@param tHeight: panel's height"""
	area = width * height;
	panel = tWidth * tHeight;
	return area / panel

def super_new_function():
	print("it works")