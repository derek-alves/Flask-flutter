from flask import request, jsonify
from flask_api import FlaskAPI 
import transitfeed


def create_app(config_name):
    app = FlaskAPI(__name__)
    
    # Cria rota com o metodo e caminho desejado e a função que vai ser esse executado por meio de caminha
    # ex: def exemplo(parametros) 
    @app.route("/open-gtfs", methods = ["GET"])
    def open(this):
        
        extension_module = transitfeed
        dump(extension_module)
        gtfs_factory = extension_module.GetGtfsFactory()
        loader = gtfs_factory.Loader("../assets/google_transit.zip")
        schedule = loader.Load()
        
        return schedule
    return app