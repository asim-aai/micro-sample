class Item:
    def __init__(self, id: int, name: str) -> None:
        self._id = None
        self._name = None

        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: dict):
        if _dict is None:
            return None
        item = cls(_dict['id'], _dict['name'])
        return item

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id == 10:
            raise IndexError
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name}
