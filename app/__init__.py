from flask import Flask

def app(config_name='DevelopmentConfig'):
    create_app = Flask(__name__)
    create_app.config.from_object(f'config.{config_name}')

    create_app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
    create_app.config['EXISTING_FILE'] = 'app/static/original'
    create_app.config['GENERATED_FILE'] = 'app/static/generated'

    # Register blueprints and other setup here
    from .views import main
    create_app.register_blueprint(main)

    return create_app

# from .routes import main
# app.register_blueprint(main)

