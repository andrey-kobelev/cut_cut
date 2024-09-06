from http import HTTPStatus

from flask import flash, redirect, render_template, abort
from werkzeug.exceptions import NotFound

from . import app
from .forms import CutURLForm
from .models import URLMap
from .constants import SHORT_EXISTS
from .exceptions import ShortExists


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data
    original = form.original_link.data
    try:
        url_map = URLMap.add_url(original=original, short=short)
    except ShortExists:
        flash(
            SHORT_EXISTS
        )
        return render_template('index.html', form=form)
    return render_template(
        'index.html',
        form=form,
        short_link=url_map.to_dict()['short_link']
    )


@app.route('/<path:short>')
def url_map_view(short):
    try:
        url_map = URLMap.get_url_map(short=short, not_found_exception=True)
    except NotFound:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original)
