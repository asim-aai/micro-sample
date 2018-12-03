from flask import Request
from flask_injector import inject

from models.Item import Item
from services.provider import ItemsProvider

items = {
    0: {"name": "First item"}
}


@inject(data_provider=ItemsProvider)
def search(data_provider) -> list:
    return data_provider.get_serialized()


@inject(item=Item, _request=Request)
def post(item: Item, _request: Request) -> dict:
    print(item)
    return item.serialize
