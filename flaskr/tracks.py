from flask import (Blueprint, render_template)
from flaskr.db import get_db

bp = Blueprint('tracks', __name__, url_prefix='/tracks')


@bp.route('/')
def tracks():
    db = get_db()
    tracks = db.execute(
        'SELECT COUNT(*) FROM tracks').fetchone()[0]
    return render_template('tracks.html', tracks=tracks)


@bp.route('/<genre>')
def tracks_genre(genre):
    db = get_db()
    genrecount = db.execute(
        'SELECT COUNT(*) FROM tracks WHERE genre = ?', (genre,)).fetchone()[0]
    return render_template('tracks_genre.html', genre=genre, count=genrecount)
