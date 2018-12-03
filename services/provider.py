from models.Item import Item


class ItemsProvider(object):
    def __init__(self, items: list = []):
        if len(items) == 0:
            items = [
                Item(0, 'First item'),
                Item(1, 'Second item'),
                Item(2, 'Third item'),
                Item(3, 'Fourth item'),
                Item(4, 'Fifth item'),
                Item(5, 'Sixth item'),
                Item(6, 'Seventh item')
            ]

        self._items = items

    def get(self, number_of_items: int = 5) -> list:
        if not self._items:
            return []

        if number_of_items > len(self._items):
            number_of_items = len(self._items)

        return self._items[0:number_of_items]

    def get_serialized(self, number_of_items: int = 5) -> list:
        if not self._items:
            return []

        if number_of_items > len(self._items):
            number_of_items = len(self._items)

        return [item.serialize for item in self._items[0:number_of_items]]
