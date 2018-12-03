import connexion
from flasgger import Swagger
from flask import Request

from injector import Binder
from flask_injector import FlaskInjector, inject
from connexion.resolver import RestyResolver

from models.Item import Item
from services.provider import ItemsProvider


# Initial bindings
def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider()
    )
    return binder


connexionApp = connexion.App(__name__, specification_dir='swagger/', port=9090)
connexionApp.add_api('app.yaml', resolver=RestyResolver('api'), strict_validation=True)
swagger = Swagger(connexionApp.app)


# Runtime bindings
@connexionApp.app.before_request
@inject(request=Request)
def before_request(request):
    connexionApp.app.flask_injector.injector.binder.bind(Request, request)
    item = Item.from_dict(request.get_json())
    connexionApp.app.flask_injector.injector.binder.bind(Item, item)


if __name__ == '__main__':
    connexionApp.app.flask_injector = FlaskInjector(app=connexionApp.app, modules=[configure])
    connexionApp.run()
