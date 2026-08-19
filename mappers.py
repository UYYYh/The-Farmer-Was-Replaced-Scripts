from movements import goto, flip
from constants import DIM

# Repeats func in the area specified by the two tuples.
def map_area(lower_left_corner, upper_right_corner, func = till):
	x_lo, y_lo = lower_left_corner
	x_hi, y_hi = upper_right_corner
	
	goto(x_lo, y_lo)
	x_dir = East
	width, height = x_hi - x_lo, y_hi - y_lo
	for i in range(height + 1):
		for j in range(width):
			func()
			move(x_dir)
		x_dir = flip(x_dir)
		func()
		move(North)

# Similar with map_area, but takes a function and applies it over the range defined by the two corners.
def map_range(lower_left_corner, upper_right_corner, func):
	x_lo, y_lo = lower_left_corner
	x_hi, y_hi = upper_right_corner
	
	for y in range(y_lo, y_hi + 1):
		if y % 2 == 0:
			x_low, x_high, x_step = x_lo, x_hi + 1, 1
		else:
			x_low, x_high, x_step = x_hi, x_lo - 1, -1
		for x in range(x_low, x_high, x_step):
			func(x, y)

def map_area_all(func = till):
	return map_area((0, 0), (DIM - 1, DIM - 1), func)

def map_range_all(func, checkered = False):
	return map_range((0, 0), (DIM - 1, DIM - 1), func, checkered)

def map_cols(x_lo, x_hi, func):
	for x in range(x_lo, x_hi + 1):
		goto(x, 0)
		func()

def map_rows(y_lo, y_hi, func):
	for y in range(y_lo, y_hi + 1):
		goto(0, y)
		func()

def map_range_1d(lo, hi, func):
	for i in range(lo, hi + 1):
		func(i)

def map_range_1d_all(func):
	return map_range_1d(0, DIM - 1, func)