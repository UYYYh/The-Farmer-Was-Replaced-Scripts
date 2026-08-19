from constants import DIM
from movements import goto, flip 
from deque import *
from helpers import async_spawn_drone_1

# The scheduler manages batches of tasks, allowing concurrent execution of tasks within the same batch.
# Each batch is represented as a list of tasks. The scheduler maintains a queue of these batches, and executes them sequentially. 
# A task is represented by (x, y, func, arg), where the task starts at (x, y) and executes func(arg) at that location.
# Note that func MUST be a unary function as the game does not support *args syntax. 

# Contains batches of tasks, if two tasks are in the same batch, they can be executed concurrently.
_queue = deque()

def schedule_batch(tasks):
    deque_append(_queue, tasks)

def _execute_batch(batch):
    drones = []
    res = []
    for x, y, func, arg in batch:
        goto(x, y)
        drones.append(async_spawn_drone_1(func, arg))
    for drone in drones:
        res.append(wait_for_drone(drone)) 
    return res

def _execute_batch_nr(batch):
    for x, y, func, arg in batch:
        goto(x, y)
        async_spawn_drone_1(func, arg)

def execute_queue():
    res = []
    while _queue:
        batch = deque_popleft(_queue)
        res.append(_execute_batch(batch))
    return res

def execute_queue_nr():
    while _queue:
        batch = deque_popleft(_queue)
        _execute_batch_nr(batch)