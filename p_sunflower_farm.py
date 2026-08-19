from constants import DIM
from movements import goto
from p_mappers import pmap_area_all, pmap
from helpers import here, fertilise_harvest, till_plant


_buckets = []

def _initialise():
	for _ in range(9):
		_buckets.append([])
	
def _reset():
	def till_plant_measure_sunflower():
		till_plant(Entities.Sunflower)
		return measure()
		# _buckets[15 - measure()].append(here())
	
	petals = pmap_area_all(till_plant_measure_sunflower)
	for x in range(DIM):
		for y in range(DIM):
			_buckets[15 - petals[x][y]].append((x, y))

def _target_harvest(coordinates):
	x, y = coordinates
	goto(x, y)
	fertilise_harvest()

def _cycle():
	_reset()
	goto(DIM // 2, DIM // 2)
	
	for bucket in _buckets:
		pmap(_target_harvest, bucket)

def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()
farm(1000)
	