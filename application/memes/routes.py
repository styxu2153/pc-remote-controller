from flask import render_template, redirect, flash, url_for
from application.memes import bp
from application.memes.controller import youtube_controller

@bp.route('/meme')
def meme():
    return render_template('memes.html')

@bp.route('/meme/wapiesz')
def wapiesz():
    youtube_controller.open_url('https://www.youtube.com/watch?v=2yusdx60_aw')
    return redirect(url_for('memes.meme'))

@bp.route('/meme/harnold')
def harnold():
    youtube_controller.open_url('https://www.youtube.com/watch?v=3dHpEfmegOA')
    return redirect(url_for('memes.meme'))

@bp.route('/meme/caramelldansen')
def caramelldansen():
    youtube_controller.open_url('https://www.youtube.com/watch?v=A67ZkAd1wmI')
    return redirect(url_for('memes.meme'))

@bp.route('/meme/coco')
def coco():
    youtube_controller.open_url('https://www.youtube.com/watch?v=2-ffgjRGtiY')
    return redirect(url_for('memes.meme'))

@bp.route('/meme/pause_play')
def pause_play():
    youtube_controller.pause_play_video()
    return ''

@bp.route('/meme/close_video')
def close_video():
    youtube_controller.close_video()
    return ''