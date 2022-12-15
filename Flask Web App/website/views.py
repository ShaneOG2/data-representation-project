from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import DAO


views = Blueprint('views', __name__)

notes = DAO.Notes_Class()
notes.create_note_table()


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    current_user_id = current_user.uid
    current_user_notes = notes.get_user_notes(current_user_id)

    if request.method == 'POST':
        note_data = request.form.get('note')

        if len(note_data) < 1:
            flash('Note is too short!', category='error')
        else:
            notes.create_note((note_data,
                            current_user_id))
            flash('Note added!', category='success')


    return render_template("home.html", user = current_user, notes = current_user_notes)