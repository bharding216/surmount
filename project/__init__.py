from flask import Flask, request, redirect, render_template
from flask_mail import Mail
from helpers import generate_sitemap
from dotenv import load_dotenv
import os
import logging

# Create an instance 'mail' of the class 'Mail()'.
mail = Mail()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv('secret_key')

    app.jinja_env.globals.update(generate_sitemap = generate_sitemap)

    # Mail config settings:
    app.config['MAIL_SERVER']='live.smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'api'
    app.config['MAIL_PASSWORD'] = os.getenv('mail_password')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    mail.init_app(app)

    with app.app_context():
        from .views import views
        app.register_blueprint(views, url_prefix="/")

        from .blogs import blogs
        app.register_blueprint(blogs, url_prefix="/blog")

        @app.before_request
        def redirect_to_https():
            # Ensure that all requests are secure (HTTPS)
            if not request.is_secure and request.host != 'localhost:2000':
                return redirect(request.url.replace('http://', 'https://'), code=301)

        def handle_error(error):
            error_code = getattr(error, 'code', 500)  # Get the error code, default to 500
            return render_template('error.html', error_code=error_code), error_code

        app.register_error_handler(404, handle_error)
        app.register_error_handler(500, handle_error)
        app.register_error_handler(400, handle_error)
        app.register_error_handler(403, handle_error)
        app.register_error_handler(401, handle_error)
        app.register_error_handler(405, handle_error)
        app.register_error_handler(503, handle_error)
        app.register_error_handler(504, handle_error)

        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

        return app