from flask import Flask, render_template, redirect # type: ignore
import random

app = Flask(__name__)

def process_and_save_data():
    x, y = None, None
    return x, y #return None hvis der ikke er data i receive registeret

@app.route('/')
def display_data_to_user():
    x, y = random.randint(0, 100), random.randint(0, 100)

    # Hvis ingen data modtages, sendes client til error page
    if x is None or y is None:
        return redirect("/error")

    return render_template('hjemmeside.html', x=x, y=y)

@app.route("/error")
def display_data_error_to_user():
    x = "ERROR, DATA NOT RECEIVED"
    y = "ERROR, DATA NOT RECEIVED"
    return render_template('hjemmeside.html', x= x, y= y)


if __name__ == '__main__':
    app.run()
