from movements import goto, flip
from constants import DIM

def pmap_rows(lo, hi, func):
	goto(0, lo)
	drones = []
	result = []
	for y in range(lo, hi + 1):
		drone_ref = spawn_drone(func)
		while drone_ref == None:
			drone_ref = spawn_drone(func)
		drones.append(drone_ref)
		move(North)
	for drone in drones:
		result.append(wait_for(drone))
	return result
	
	
def pmap_cols(lo, hi, func):
	goto(lo, 0)
	drones = []
	result = []
	while get_pos_x() <= hi:
		drone_ref = spawn_drone(func)
		if drone_ref == None:
			continue
		drones.append(drone_ref)
		move(East)
	for drone in drones:
		result.append(wait_for(drone))
	return result
			
def pmap_area_all(func):
	def row():
		res = []
		for _ in range(DIM):
			res.append(func())
			move(East)
		return res
	return pmap_rows(0, DIM - 1, row)
	
def pmap(func, arr):
	res    = []
	drones = []
	for elem in arr:
		drone_no = spawn_drone(func, elem)
		while drone_no == None:
			drone_no = spawn_drone(func, elem)
		drones.append(drone_no)
	for drone in drones:
		res.append(wait_for(drone))
	return res

def pmap_rows_nr(lo, hi, func):
	goto(0, lo)
	while get_pos_y() <= hi:
		if spawn_drone(func):
			move(North)
	
def pmap_cols_nr(lo, hi, func):
	goto(lo, 0)
	while get_pos_x() <= hi:
		if spawn_drone(func):
			move(East)
			
def pmap_area_all_nr(func):
	pmap_cols_nr(0, DIM - 1, func)
