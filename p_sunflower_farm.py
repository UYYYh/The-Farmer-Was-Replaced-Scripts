from constants import DIM
from movements import goto
from p_mappers import pmap_area_all, pmap
from helpers import here, fertilise_harvest, till_plant
from scheduler import schedule_batch, execute_queue

# Each bucket is a list of lists. 
_buckets = []

def _initialise():
	for _ in range(9):
		field = []
		for _ in range(DIM):
			row = []
			for _ in range(DIM):
				row.append(0)
			field.append(row)
		_buckets.append(field)

def _reset_task(arg):
	petals = []
	for i in range(DIM):
		till_plant(Entities.Sunflower)
		petals.append(measure())
		if i < DIM - 1:
			move(East)
	return petals

def _reset():
	batch = []
	for i in range(DIM):
		batch.append((0, i, _reset_task, None))
	schedule_batch(batch)
	res = execute_queue()
	for x in range(DIM):
		for y in range(DIM):
			_buckets[15 - res[y][x]][y].append(x)

def _harvest_task(arg):
	y = get_pos_y()
	for x in arg:
		goto(x, y)
		fertilise_harvest()

def _cycle():
	_reset()
	for bucket in _buckets:
		batch = []
		for i in range(len(bucket)):
			row = bucket[i]
			if not row:
				continue
			batch.append((0, i, _harvest_task, row))
		schedule_batch(batch)
	execute_queue()
	
def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()
farm(1000)
	