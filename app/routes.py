from app import app, mail
from flask import render_template, redirect, flash, url_for, request
from app.forms import ContactForm
from flask_mail import Message


@app.route('/')
def index():
    return render_template(
        'index.html',
    )

@app.route('/about/')
def about():
    return render_template(
        'about.html',
    )

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.object.data, sender='Symeon', recipients=['igor.shiyan@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template(
            'contact.html',
            success=True,
            form=form
        )
    elif request.method == 'GET':
        return render_template(
            'contact.html',
            form=form
        )

@app.route('/portfolio/')
def portfolio():
    return render_template(
        'portfolio.html',
    )

@app.route('/portfolio/project/')
def project():
    return render_template(
        'single-project.html',
    )

@app.route('/services/')
def services():
    return render_template(
        'services.html',
    )