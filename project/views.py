from flask import Blueprint, render_template, request, redirect, flash, url_for, make_response, send_from_directory
from project import mail
from flask_mail import Mail, Message
from helpers import generate_sitemap

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://www.getsurmount.com'
    description = "Ready to elevate your online presence? Let's work together to create a website that truly represents your brand and helps you achieve your online goals."
    budget_options = ['<$2,500', '$2,500-$10,000', '$10,000-20,0000']

    return render_template('index.html',
                           url=url,
                           description=description,
                           options=budget_options)

@views.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@views.route('/pricing', methods=['GET', 'POST'])
def pricing():
    return render_template('pricing.html')

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST': # Handle form submission
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        budget = request.form['budget']
        panda = request.form['panda']

        if panda.lower() != "white":
            flash('Form submission rejected due to spam detection (wrong answer to secret question).', category='error')
            return redirect(url_for('views.contact'))  
        
        msg = Message('New Client Request - Surmount',
                        sender = ("Brandon from Surmount", 'hello@getsurmount.com'),
                        recipients = ['brandon@getsurmount.com'
                                      ]
                        )
        
        msg.html = render_template('contact_email.html',
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   phone=phone,
                                   message=message,
                                   budget=budget
                                   )

        mail.send(msg)

        flash("We received your message, " + first_name + "! We'll get back to you within 24 hours to \
              schedule a time to learn more about your project.", "success")
        return redirect(url_for('views.index'))
    
    else: # Handle GET request
        budget_options = ['<$2,500', '$2,500-$10,000', '$10,000-20,0000']
        return render_template('contact.html',
                               options=budget_options)


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