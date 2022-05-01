from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Qua3chaiime2Leva'
    app.config['SECURITY_PASSWORD_SALT'] = 'phohJu9u'

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
