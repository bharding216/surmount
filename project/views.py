from flask import Blueprint, render_template, request, redirect, flash, url_for

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@views.route('/contact_confirmation', methods=['GET', 'POST'])
def contact_confirmation():
    if request.method == 'POST':

        # Take the form data and send yourself and the user a confirmation email

        return render_template('contact_confirmation.html')