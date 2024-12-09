import serial # type: ignore
from flask import Flask, render_template, redirect # type: ignore

app = Flask(__name__, template_folder='templates')

# UART-indstillinger
uart_port = '/dev/serial0'
baud_rate = 9600
ser = serial.Serial(uart_port, baud_rate)
def process_and_save_data():
    x, y = None, None

    # Læs data fra UART indtil begge værdier er fundet
    while ser.in_waiting > 0:
        uart_reading = ser.readline().decode('utf-8').strip()

        # Tjek om linjen starter med "watt" eller "Sol" og tildel til x eller y
        if uart_reading.startswith("watt"):
            x = uart_reading.split()[1]  # Henter watt-værdien
        elif uart_reading.startswith("Sol"):
            y = uart_reading.split()[1]  # Henter sol-værdien
        elif uart_reading.startswith("test"):
            x="Kommunikation oprettet"
            y="Kommunikation oprettet"
            

        # Stop, hvis begge værdier er modtaget
        if x is not None and y is not None and ser.in_waiting==0:
            return x, y
        
    return x, y #return None hvis der ikke er data i receive registeret


@app.route('/')
def display_data_to_user():
    x, y = process_and_save_data()

    # Hvis ingen data modtages, sendes client til error page
    if x is None and y is None:
        display_data_error_to_user()

    return render_template('hjemmeside.html', x=x, y=y)


def display_data_error_to_user():
    x = "ERROR, DATA NOT RECEIVED"
    y = "ERROR, DATA NOT RECEIVED"
    
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
