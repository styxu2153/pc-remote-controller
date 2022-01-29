from flask import render_template, redirect, flash, url_for, request
from application.twitch_streams import bp
from application.twitch_streams.models import TwitchController, twitch_windows

@bp.route('/twitch', methods=['GET', 'POST'])
def twitch():
    if request.method == "POST":
        streamer_username = request.form['username']
        twitch_windows[streamer_username] = TwitchController(streamer_username)
        redirect(url_for('twitch_streams.twitch'))
    return render_template('twitch_streams.html', twitch_windows=twitch_windows)
        
@bp.route('/twitch/<streamer>/close')
def close(streamer):
    twitch_windows[streamer].close_video()
    twitch_windows.pop(streamer, None)
    return redirect(url_for('twitch_streams.twitch')) 

@bp.route('/twitch/<streamer>/increase_volume')
def increase_volume(streamer):
    twitch_windows[streamer].increase_volume(10)
    return redirect(url_for('twitch_streams.twitch'))

@bp.route('/twitch/<streamer>/decrease_volume')
def decrease_volume(streamer):
    twitch_windows[streamer].decrease_volume(10)
    return redirect(url_for('twitch_streams.twitch'))