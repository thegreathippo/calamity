class EntityIndex(list):

	def new_entity(self):
		new_e = Entity()
		self.append(new_e)
		return new_e


class Entity(dict):
	_id = 0
	
	def __init__(self):
		super().__init__()
		self._id = self._id
		type(self)._id += 1

	@property
	def id(self):
		return self._id

	def __getattr__(self, key):
		if key in self:
			return self[key]
		else:
			return super().__getattribute__(key)

	def __setattr__(self, key, value):
		if not key.startswith("_"):
			self[key] = value
		else:
			super().__setattr__(key, value)

	def __eq__(self, other):
		if type(self) == type(other):
			return self.id == other.id

	def __hash__(self):
		return hash((type(self), self.id))


