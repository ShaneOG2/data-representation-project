from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import DAO
import json
import re 
import requests


views = Blueprint('views', __name__)

notes = DAO.Notes_Class()
notes.create_note_table()


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    vals = getCoinDesk()
    current_user_id = current_user.uid
    current_user_notes = notes.get_user_notes(current_user_id)
    current_user_dates = notes.get_user_date(current_user_id)
    current_user_times = notes.get_user_time(current_user_id)
    current_user_euros = notes.get_user_euro(current_user_id)
    current_user_usds = notes.get_user_usd(current_user_id)
    current_user_gbps = notes.get_user_gbp(current_user_id)
    current_user_nids = notes.get_user_nid(current_user_id)

    if request.method == 'POST':
        note_data = request.form.get('note')
        
        if len(note_data) < 1:
            flash('Note is too short!', category='error')
        else:
            notes.create_note((note_data, str(vals[0]), str(vals[1]), str(vals[2]), str(vals[3]), str(vals[4]), current_user_id))
            flash('Note added!', category='success')


    return render_template("home.html",
                            current_date = vals[0],
                            current_time = vals[1],
                            current_euro = vals[2],
                            current_usd = vals[3],
                            current_gbp = vals[4],
                            user = current_user, 
                            notes = current_user_notes,
                            dates = current_user_dates,
                            times = current_user_times,
                            euros = current_user_euros,
                            usds = current_user_usds,
                            gbps = current_user_gbps,
                            nids = current_user_nids,
                            n = len(current_user_notes))

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    notes.delete_note_by_nid(noteId)

def getCoinDesk():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()

    euro_object = data["bpi"]["EUR"]
    euro_rate = euro_object["rate"]

    dollar_object = data["bpi"]["USD"]
    dollar_rate = dollar_object["rate"]

    pound_object = data["bpi"]["GBP"]
    pound_rate = pound_object["rate"]

    date_time = data["time"]["updated"]
    split_date_time = re.split("\s", date_time)
    date = " ".join(split_date_time[0:3])
    time = " ".join(split_date_time[3:])

    return date, time, euro_rate, dollar_rate, pound_rate