from flask import flash, redirect, render_template

from . import app
from .forms import CutURLForm
from .models import URLMap
from .constants import SHORT_LINK_EXISTS, SHORT_LINK_CATEGORY


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = CutURLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data
    if short and URLMap.is_short_exists(short):
        flash(
            SHORT_LINK_EXISTS,
            SHORT_LINK_CATEGORY
        )
        return render_template('index.html', form=form)
    url_map = URLMap.add_url(data=form.data)
    return render_template(
        'index.html',
        form=form,
        short=url_map.to_dict()['short_link']
    )


@app.route('/<path:short>')
def url_map_view(short):
    url = URLMap.get_url(short=short)
    return redirect(url.original)
