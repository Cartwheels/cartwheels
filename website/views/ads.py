import stripe
from flask import render_template, request, redirect, url_for
from website.views.utils import base_context
from website.settings import STRIPE_SECRET_KEY
from website import users


stripe.api_key = STRIPE_SECRET_KEY


def ads_page():
    context = base_context()

    if context['user'] is None:
        redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form['stripeEmail']
        stripe.Charge.create(
            amount=20,
            currency='usd',
            card=request.form['stripeToken'],
            description='Charge for ' + email
        )

        owner = users.find_one(username=email)
        owner.ad_type = 1
        owner.save()

        return redirect(url_for('profile'))

    return render_template('ads.html', **context)
