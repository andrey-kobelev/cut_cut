from http import HTTPStatus

from flask import flash, redirect, render_template, abort

from . import app
from .forms import CutURLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        return render_template(
            'index.html',
            form=form,
            short_link=URLMap.add_url(
                original=form.original_link.data,
                short=form.custom_id.data
            ).to_dict()['short_link']
        )
    except (
        URLMap.ShortExists, URLMap.FailGenerateShort
    ) as error:
        flash(str(error))
        return render_template('index.html', form=form)


@app.route('/<path:short>')
def url_map_view(short):
    url_map = URLMap.get_url_map(short=short)
    if not url_map:
        abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original)
