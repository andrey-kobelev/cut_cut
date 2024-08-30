from flask import flash, redirect, render_template

from . import app, db
from .forms import CutURLForm
from .models import URLMap
from .utils import URLEncoder
from .constants import SHORT_LINK_EXISTS, SHORT_LINK_CATEGORY


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if short and URLMap.query.filter_by(short=short).first() is not None:
            flash(
                SHORT_LINK_EXISTS,
                SHORT_LINK_CATEGORY
            )
            return render_template('index.html', form=form)
        if not short:
            short = URLEncoder(
                model=URLMap,
                original_url=form.original_link.data
            ).encode()
        url_map = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        return render_template('url_map.html', form=form, url_map=url_map)
    return render_template('index.html', form=form)


@app.route('/<path:id>')
def url_map_view(id):
    url = URLMap.query.filter_by(short=id).first_or_404()
    return redirect(url.original)
