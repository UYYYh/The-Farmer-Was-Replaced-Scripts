from constants import DIM 
from movements import goto
from mappers import map_area_all, map_range_all
from helpers import fertilise_harvest

# list of all the coordinates (x, y) that still needs to be planted
_need_planting = []
_not_yet_grown = 0

def _initialise():
	map_area_all(till)

def _reset():
	global _need_planting
	global _grown
	_need_planting = []
	_not_yet_grown = DIM ** DIM

	def add_to_need_planting(x, y):
		_need_planting.append((x, y))
	map_range_all(add_to_need_planting)

def _cycle():
	global _not_yet_grown
	_reset()
	goto(0, 0)
	for x, y in _need_planting:
		goto(x, y)
		
		# grown pumpkin, skip
		if can_harvest():
			_not_yet_grown -= 1
			continue
		
		# pumpkin dead, patch empty or wrong plant, replant
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
			_need_planting.append((x, y))
			continue
	
		# pumpkin is still growing, and fewer or equal to 3 ungrown
		if _not_yet_grown <= 3:
			while not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					_need_planting.append((x, y))
					break
				use_item(Items.Fertilizer)
			continue
		
		# 4 or more pumpkins still growing
		_need_planting.append((x, y))
	fertilise_harvest()

def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()

farm(1000)
