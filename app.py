from flask import Flask, render_template, request, redirect, flash
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

app.run()
