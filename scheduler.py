from movements import goto
from helpers import async_spawn_drone_1

# Runs a batch of tasks concurrently, one drone per task.
# A task is (x, y, func, arg): a drone starts at (x, y) and evaluates func(arg) there.
# func MUST be unary as the game does not support *args syntax.

# Runs tasks[lo:hi] concurrently and appends their results to res in task order.
def _run_wave(tasks, lo, hi, res):
	drones = []
	for i in range(lo, hi - 1):
		x, y, func, arg = tasks[i]
		goto(x, y)
		drones.append(async_spawn_drone_1(func, arg))

	# The main drone counts against max_drones(), so it runs the last task of the
	# wave itself rather than holding a slot idle inside wait_for().
	x, y, func, arg = tasks[hi - 1]
	goto(x, y)
	own = func(arg)

	for i in range(len(drones)):
		res.append(wait_for(drones[i]))
	res.append(own)

def run_batch(tasks):
	res = []
	n = len(tasks)
	# max_drones() counts the drone this code is running on, so a wave of that
	# width is exactly one spawn per free slot plus the main drone's own task.
	width = max_drones()
	if width < 1:
		width = 1
	lo = 0
	while lo < n:
		hi = min(lo + width, n)
		_run_wave(tasks, lo, hi, res)
		lo = hi
	return res
