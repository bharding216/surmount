from flask import Flask, session, request, redirect
from flask_mail import Mail
import os

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .views import views
        app.register_blueprint(views, url_prefix="/")

        @app.before_request
        def redirect_to_https():
            # Ensure that all requests are secure (HTTPS)
            if not request.is_secure and request.host != 'localhost:2000':
                return redirect(request.url.replace('http://', 'https://'), code=301)

        return app