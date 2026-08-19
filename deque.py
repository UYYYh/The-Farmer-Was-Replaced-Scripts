

def deque():
	# head, tail, storage dictionary
	return [0, 0, {}]

def deque_append(dq, value):
	head, tail, storage = dq
	storage[tail] = value
	dq[1] = tail + 1

def deque_pop_left(dq):
	head, tail, storage = dq
	if head == tail:
		return None
	value = storage[head]
	storage.remove(head)
	dq[0] = head + 1
	return value

def deque_pop(dq):
	head, tail, storage = dq
	if head == tail:
		return None
	value = storage[tail - 1]
	dq[1] = tail - 1
	return value

def deque_peek_left(dq):
	head, tail, storage = dq
	if head == tail:
		return None
	return storage[head]

def deque_peek_right(dq):
	head, tail, storage = dq
	if head == tail:
		return None
	return storage[tail - 1]

def deque_length(dq):
	head, tail, _ = dq
	return tail - head