from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    with app.app_context():
        from src.dashboard.dashboard import dashboard_bp

        app.register_blueprint(dashboard_bp)
        return app
