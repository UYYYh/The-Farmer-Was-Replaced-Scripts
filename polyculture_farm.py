from constants import DIM 
from movements import goto, flip
from mappers import map_area, map_range, map_area_all
from helpers import till_plant, try_harvest, adj

_field = []
	
def _initialise():
	for _ in range(DIM):
		row = []
		for _ in range(DIM):
			row.append(Entities.Grass)
		_field.append(row)
		
def _set_plant(plant_type, x, y):
	if plant_type == Entities.Tree:
		for nx, ny in adj(x, y):
			if _field[nx][ny] == Entities.Tree:
				return False
	_field[x][y] = plant_type
	return True

def _cycle():
	goto(0, 0)
	
	def poly_go():
		try_harvest()
		x, y = get_pos_x(), get_pos_y()
		till_plant(_field[x][y])
		companion, (x_com, y_com) = get_companion()
		_set_plant(companion, x_com, y_com)
	map_area_all(poly_go)
	
def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()
farm(1000)

	