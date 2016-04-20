class EntityIndex(list):
	def __init__(self):
		super().__init__()
		self.append(Entity())

	def new_entity(self):
		for e in self:
			if "eid" not in e:
				e.allocate()
				return e
		new_e = Entity()
		new_e.allocate()
		self.append(new_e)
		return new_e


class Entity(dict):
	_id = 0

	def __init__(self):
		super().__init__()

	def allocate(self):
		self["eid"] = self._id
		type(self)._id += 1

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
