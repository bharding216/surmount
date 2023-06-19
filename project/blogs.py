from flask import Blueprint, render_template, request, redirect, flash, url_for, make_response, send_from_directory
from project import mail
from flask_mail import Mail, Message
from helpers import generate_sitemap

blogs = Blueprint('blogs', __name__, template_folder='blog_templates')


@blogs.route('', methods=['GET', 'POST'])
def blog_home():
    return render_template('/blog_templates/blog_home.html')

@blogs.route('/responsive-design-tips', methods=['GET', 'POST'])
def responsive_design_tips():
    title = 'How to Create a Website that Looks Great on Any Device | Surmount'
    url = 'https://www.getsurmount.com/blog/responsive-design-tips'
    description = "Responsive web design has become increasingly important as more and more people access the internet from their smartphones and tablets. It's crucial to ensure that your website looks great and functions well on any device."
    return render_template('/blog_templates/responsive_design_tips.html',
                           title = title,
                           url = url,
                           description = description)

@blogs.route('/ux-guide', methods=['GET', 'POST'])
def web_app_factors():
    title = '5 Key Factors to Consider When Building a Web App: A Guide to UX'
    url = 'https://www.getsurmount.com/blog/ux-guide'
    description = "Web applications are an integral part of many modern businesses. Let's discuss the most important UX factors to consider when building a web application."
    return render_template('/blog_templates/web_app_factors.html',
                           title = title,
                           url = url,
                           description = description)

@blogs.route('/san-antonio-web-developers', methods=['GET', 'POST'])
def satx1():
    title = 'San Antonio Web Developer | Surmount'
    url = 'https://www.getsurmount.com/blog/san-antonio-web-developers'
    description = "In our fast-paced digital world, having a strong online presence is crucial for any business in San Antonio, Texas. Whether you&apos;re a small startup or an established enterprise, a well-designed and responsive website can make all the difference."
    return render_template('/blog_templates/cities/satx1.html',
                           title = title,
                           url = url,
                           description = description)

@blogs.route('/laredo-web-developers', methods=['GET', 'POST'])
def laredo1():
    title = 'Laredo Web Developer | Surmount'
    url = 'https://www.getsurmount.com/blog/laredo-web-developers'
    description = "In our fast-paced digital world, having a strong online presence is crucial for any business in Laredo, Texas. Whether you&apos;re a small startup or an established enterprise, a well-designed and responsive website can make all the difference."
    return render_template('/blog_templates/cities/laredo1.html',
                           title = title,
                           url = url,
                           description = description)