from flask import Flask

def app(config_name='DevelopmentConfig'):
    create_app = Flask(__name__)
    create_app.config.from_object(f'config.{config_name}')

    # Register blueprints and other setup here
    from .views import main
    create_app.register_blueprint(main)

    return create_app

# from .routes import main
# app.register_blueprint(main)

