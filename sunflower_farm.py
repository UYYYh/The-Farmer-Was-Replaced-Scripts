from constants import DIM
from movements import goto
from mappers import map_range, map_area_all
from helpers import here, fertilise_harvest, till_plant


_buckets = []

def _initialise():
	for _ in range(9):
		_buckets.append([])
	
def _reset():
	def till_plant_record_sunflower():
		till_plant(Entities.Sunflower)
		_buckets[15 - measure()].append(here())
	
	map_area_all(till_plant_record_sunflower)

def _cycle():
	_reset()
	goto(0, 0)
	
	for bucket in _buckets:
		for _ in range(len(bucket)):
			x, y = bucket.pop()
			goto(x, y)
			fertilise_harvest()

def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()
farm(1000)
	