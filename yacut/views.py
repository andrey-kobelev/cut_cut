from crypt import methods

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import CutURLForm
from .models import URLMap
from .utils import URLEncoder


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if short and URLMap.query.filter_by(short=short).first() is not None:
            flash('Такая ссылка уже существует! Попробуйте дрогой вариант', 'link-exists')
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
        return redirect(url_for('url_map_view', id=url_map.id))
    return render_template('index.html', form=form)


@app.route('/show-url/<int:id>')
def url_map_view(id):
    form = CutURLForm()
    url_map = URLMap.query.get_or_404(id)
    return render_template('url_map.html', form=form, url_map=url_map)
