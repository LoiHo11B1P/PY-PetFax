from flask import Flask 
from flask_migrate import Migrate


def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Fr33d0m83*@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             
    
    # config and register database
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)


    # register pet blueprint 
    from . import pet
    from . import fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    # return the app 
    return app

#


          
