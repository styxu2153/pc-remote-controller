from flask import render_template, redirect, url_for, request, flash
from application.sound_controller import bp
from application.sound_controller.controller import master_volume


@bp.route('/master_control', methods=['GET', 'POST'])
def master_control():
    return render_template('master_control.html', master_volume=master_volume)

@bp.route('/master_control/mute_master')
def mute_master():
    master_volume.mute_master()
    return render_template('master_control.html', master_volume=master_volume)

@bp.route('/master_control/unmute_master')
def unmute_master():
    master_volume.unmute_master()
    return render_template('master_control.html', master_volume=master_volume)

@bp.route('/master_control/decrease_volume')
def decrease_volume():
    master_volume.decrease_master_volume()
    return render_template('master_control.html', master_volume=master_volume)

@bp.route('/master_control/increase_volume')
def increase_volume():
    master_volume.increase_master_volume()
    return render_template('master_control.html', master_volume=master_volume)
