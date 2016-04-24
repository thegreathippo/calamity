class BBox2:
	
	def __init__(self, x, y=None, w=None, h=None):
		if y is None:
			try:
				_x, _y, _w, _h = x.x, x.y, x.w, x.h
			except AttributeError:
				raise TypeError("{0} received invalid args: "
								"{1}".format(type(self).__name__, x))
		elif w is None:
			_x, _y, _w, _h = x[0], x[1], y[0], y[1]
		elif h is None:
			raise TypeError("{0} received invalid args: "
							"{1}".format(type(self).__name__, (x, y, w, h)))
		else:	
			_x, _y, _w, _h = x, y, w, h
		self._x = _x
		self._y = _y
		self._w = _w
		self._h = _h

	def collides(self, x, y=None, w=None, h=None):
		try:
			box = BBox2(x, y, w, h)
		except TypeError:
			return self._collides_point(x, y)
		return (abs(self.x - box.x) * 2 < (self.w + box.w)) and (
				abs(self.y - box.y) * 2 < (self.h + box.h))

	def touches(self, x, y=None, w=None, h=None):
		try:
			box = BBox2(x, y, w, h)
		except TypeError:
			return self._touches_point(x, y)
		return (abs(self.x - box.x) * 2 <= (self.w + box.w)) and (
				abs(self.y - box.y) * 2 <= (self.h + box.h))

	def _collides_point(self, x, y=None):
		if y is None:
			try:
				_x, _y = x.x, x.y
			except AttributeError:
				_x, _y = x[0], x[1]
		else:
			_x, _y = x, y
		if (_x <= self.x or _y <= self.y or _x >= (self.x + self.w) or
				_y >= (self.y + self.h)):
			return False
		return True

	def _touches_point(self, x, y=None):
		if y is None:
			try:
				_x, _y = x.x, x.y
			except AttributeError:
				_x, _y = x[0], x[1]
		else:
			_x, _y = x, y
		if (_x < self.x or _y < self.y or _x > (self.x + self.w) or
				_y > (self.y + self.h)):
			return False
		return True

	@property
	def x(self):
		return self._x
	
	@property
	def y(self):
		return self._y
	
	@property
	def w(self):
		return self._w
	
	@property
	def h(self):
		return self._h
