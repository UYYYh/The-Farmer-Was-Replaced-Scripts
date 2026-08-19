from helpers import here, adj, till_plant
from movements import goto, flip
from constants import DIM

_t_x, _t_y = 0, 0

_seen  = set()
_dirs  = [North, West, South, East] 
_dir_to_delta = { North: (0, 1), South: (0, -1), East: (1, 0), West: (-1, 0) }

def _dfs():
	global _t_x 
	global _t_y 
	x, y = here()
	
	if (x, y) in _seen:
		return False
		
	if x == _t_x and y == _t_y:
		harvest()
		return True
		
	_seen.add((x, y))
	
	for dir in _dirs:
		dx, dy = _dir_to_delta[dir]
		nc = (x + dx, y + dy)
		if not can_move(dir) or nc in _seen:
			continue
		
		move(dir)
		if _dfs():
			return True
		move(flip(dir))
	return False

def _reset():
	global _t_x
	global _t_y
	global _seen
	_seen = set()
	goto(DIM // 2, DIM // 2)
	till_plant(Entities.Bush)
	amount = DIM * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, amount)
	_t_x, _t_y = measure()

def _cycle():
	_reset()
	_dfs()

def farm(cycles):
	clear()
	for _ in range(cycles):
		_cycle()
farm(1)