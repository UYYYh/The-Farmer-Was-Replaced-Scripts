from constants import DIM

def move_by(x, y):
	if x > 0:
		x_d = East
	else:
		x_d = West
	if y > 0:
		y_d = North
	else:
		y_d = South
	
	for i in range(abs(x)):
		move(x_d)
	for j in range(abs(y)):
		move(y_d)

def goto(x, y):
	cur_x, cur_y = get_pos_x(), get_pos_y()
	dx, dy = (x - cur_x) % DIM, (y - cur_y) % DIM
	
	if DIM - dx < dx:
		x_dir = West
		dx = DIM - dx
	else:
		x_dir = East
	
	if DIM - dy < dy:
		y_dir = South
		dy = DIM - dy 
	else:
		y_dir = North
	
	for i in range(dx):
		move(x_dir)
	for i in range(dy):
		move(y_dir)

_flipped_dirs = {East: West, West: East, North: South, South: North}
def flip(dir):
	return _flipped_dirs[dir]
	
