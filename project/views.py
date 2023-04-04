from flask import Blueprint, render_template, request, redirect, flash, url_for, make_response, send_from_directory
from project import mail
from flask_mail import Mail, Message
from helpers import generate_sitemap

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@views.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@views.route('/pricing', methods=['GET', 'POST'])
def pricing():
    return render_template('pricing.html')

@views.route('/contact_confirmation', methods=['GET', 'POST'])
def contact_confirmation():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        msg = Message('New Client Request - Surmount',
                        sender = ("Brandon from Surmount", 'hello@getsurmount.com'),
                        recipients = ['brandon@getsurmount.com'
                                      ]
                        )
        
        msg.html = render_template('contact_email.html',
                                   first_name = first_name,
                                   last_name = last_name,
                                   email = email,
                                   phone = phone,
                                   message = message
                                   )

        mail.send(msg)

        flash("We received your message! We'll get back to you within 24 hours to \
              schedule a time to learn more about your project.", "success")
        return render_template('contact_confirmation.html')
    
@views.route('/sitemap.xml', methods=['GET'])
def sitemap():
    sitemap_xml = generate_sitemap()
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response


@views.route("/robots.txt")
def static_from_root():
    views.static_folder = 'static'
    return send_from_directory(views.static_folder, request.path[1:])