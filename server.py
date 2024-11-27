from flask import Flask, render_template, redirect # type: ignore

app = Flask(__name__)

# UART-indstillinger
def process_and_save_data():
    x, y = None, None
    return x, y #return None hvis der ikke er data i receive registeret

@app.route('/')
def display_data_to_user():
    x, y = process_and_save_data()

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
