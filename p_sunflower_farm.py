from constants import DIM
from movements import goto
from helpers import fertilise_harvest, till_plant
from scheduler import schedule_batch, execute_queue

# Each bucket is a list of lists. 
_MIN_PETALS = 7
_MAX_PETALS = 15
_buckets = []

def _initialise():
	for _ in range(_MAX_PETALS - _MIN_PETALS + 1):
		field = []
		for _ in range(DIM):
			field.append([])
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
	for field in _buckets:
		for y in range(DIM):
			field[y] = []
	batch = []
	for i in range(DIM):
		batch.append((0, i, _reset_task, None))
	schedule_batch(batch)
	res = execute_queue()[0]
	for y in range(DIM):
		for x in range(DIM):
			_buckets[_MAX_PETALS - res[y][x]][y].append(x)

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
			if len(row) == 0:
				continue
			batch.append((0, i, _harvest_task, row))
		if len(batch) > 0:
			schedule_batch(batch)
	execute_queue()

def farm(cycles):
	clear()
	_initialise()
	for _ in range(cycles):
		_cycle()
farm(1000)
