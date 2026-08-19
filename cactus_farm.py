from mappers import map_area_all, map_range_1d_all
from movements import goto
from constants import DIM
def _initialise():
	map_area_all(till)


def _plant_cactus():
	plant(Entities.Cactus)

def _insertion_sort_row(row):
	for l in range(DIM):
		goto(l, row)
		height = measure()
		while get_pos_x() > 0 and measure(West) > height:
			swap(West)
			move(West)

def _insertion_sort_col(col):
	for l in range(DIM):
		goto(col, l)
		height = measure()
		while get_pos_y() > 0 and measure(South) > height:
			swap(South)
			move(South)

def _reset():
	map_area_all(_plant_cactus)

def _cycle():
	_reset()
	goto(0, 0)
	map_range_1d_all(_insertion_sort_row)
	map_range_1d_all(_insertion_sort_col)
	harvest()

def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()
farm(100)
	