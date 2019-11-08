from flask import Flask, render_template, url_for, redirect, flash
from forms import CalculatorForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '54a4fb9118ald7s1e26797a6314e43'


@app.route("/", methods=['GET', 'POST'])
def home():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash(f'The answer is {eval(form.myFunction.data)}', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)


app.run(debug=True, threaded=True)
