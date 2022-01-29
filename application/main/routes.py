from flask import render_template, redirect, flash, url_for, request
from application import app
from application.main import bp
from application.main.controller import sleep_pc, shutdown_pc

@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        
        if 'submit1' in request.form:
            if request.form['pin1'] == app.config['SYSTEM_CONTROL_PIN']:
                print('Made it to form1')
                sleep_pc()
            else:
                flash('Invalid PIN!')
            
        if 'submit2' in request.form:
            if request.form['pin2'] == app.config['SYSTEM_CONTROL_PIN']:
                print('Made it to form2')
                shutdown_pc()
            else:
                flash('Invalid PIN!')
    
    return render_template('index.html', title='Home')
