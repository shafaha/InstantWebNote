from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from note.forms import InsertNote
from note.models import Notes
from note import AppStarter

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    form = InsertNote()
    if request.method == "POST" and  current_user.is_authenticated:
        if form.validate_on_submit():
            nt = Notes(form.title.data, form.content.data, current_user.id)
            AppStarter.getDb().session.add(nt)
            AppStarter.getDb().session.commit()
            flash("Note Successfully inserted", "success")
        else:
            flash("Note Successfully inserted", "danger")
    return render_template('home.html', title = "Supre Home", form = form)   


@views.route("/user/Notes/")
@login_required         
def showNotes():
    if current_user.is_authenticated:
        all_notes = Notes.query.filter_by(creator = current_user).all()

        return render_template("all_notes.html", all_notes = all_notes)
    flash("Please login")
    return redirect(url_for('views.home'))


@views.route("/user/Notes/<int:note_id>", methods = ["GET", "POST"])
@login_required
def deleteNote(note_id):
    print("Hello App" , int(note_id))
    if current_user.is_authenticated:

        nt = Notes.query.get(note_id)
        AppStarter.getDb().session.delete(nt)
        AppStarter.getDb().session.commit()
    return redirect(url_for("views.showNotes"))

