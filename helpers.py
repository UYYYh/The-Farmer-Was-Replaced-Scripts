from logic import xor
from constants import DIM

_delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def adj(x, y):
	res = []
	for dx, dy in _delta:
		nx, ny = x + dx, y + dy 
		if 0 <= nx < DIM and 0 <= ny < DIM:
			res.append((nx, ny))
	return res
		

def try_till(plant_type):
	if xor(plant_type == Entities.Grass, get_ground_type() == Grounds.Grassland):
		till()

def till_plant(plant_type):
	try_till(plant_type)
	if plant_type != Entities.Grass:
		plant(plant_type)

def try_harvest():
	if can_harvest():
		harvest()
		return True
	return False
	
def fertilise_harvest():
	while not can_harvest():
		use_item(Items.Fertilizer)
	harvest()
	
def here():
	return (get_pos_x(), get_pos_y())

def arrs(arrays = DIM):
	res = []
	for _ in range(arrays):
		res.append([])
	return res

def arrs_of(arrays = DIM, arr_length = DIM, value = None):
	res = []
	for _ in range(arrays):
		row = []
		for _ in range(arr_length):
			row.append(value)
		res.append(row)
	return res


# The suffix _1 means that it takes an unary function as its argument.
def async_spawn_drone_1(func, arg):
	drone_ref = spawn_drone(func, arg)
	while not drone_ref:
		drone_ref = spawn_drone(func, arg)
	return drone_ref