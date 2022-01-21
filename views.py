from flask import Blueprint, render_template

filename = 'counter.txt'

views = Blueprint('views', __name__)


@views.route('/')
def home():
    with open(filename, "r") as f:
        content = f.read()
    return render_template("base.html", content=content)


@views.route('/button_pressed')
def on_button_pressed():
    with open(filename, "r+") as f:
        current_count = int(f.read())
        updated_count = str(current_count + 1)
        f.seek(0)
        f.write(updated_count)
        f.truncate()

    return render_template('button_pressed_page.html')