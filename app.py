from flask import Flask, render_template, request, redirect, flash
import spotipy
import requests
app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_string'

from stockify.forms import StockForm

# Homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'


# About
@app.route('/about', methods=['GET','POST'])
def about():
	if request.method == 'POST':
		return render_template('about.html', name=request.form['name'], age=request.form['age'])
	else:
		return render_template('about.html')

@app.route('/stockpage',methods=['GET','POST'])
def stocks():
    form = StockForm()
    if form.validate_on_submit():
        flash('Bought {} stocks of {}.'.format(form.quantity.data,form.ticker.data))
        return redirect('/stockpage')
    return render_template('stockpage.html',form=form)

@app.route('/music',methods=['GET','POST'])
def show_playlist():

    try:
        sp = spotipy.Spotify(auth=access_token)
    except:
        # client_id
        # client_secret

        grant_type = 'client_credentials'
        body_params = {'grant_type' : grant_type}

        url='https://accounts.spotify.com/api/token'

        r=requests.post(url, data=body_params, auth = (client_id, client_secret))
        data = r.json()
        access_token = data['access_token']

        sp = spotipy.Spotify(auth=access_token)

    happytracks = sp.search(q='happy', limit=20, type='playlist')

    list = happytracks['playlists']['items']

    first = list[0]['name']

    flash('Play some {}.'.format(first))
    # return redirect('/music')
    return render_template('music.html')



app.run()
