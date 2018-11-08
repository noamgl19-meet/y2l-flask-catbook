from flask import Flask, request, redirect, url_for
from flask import render_template
from database import get_all_cats, create_cat, get_cat_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods=['GET','POST'])
def catbook_home():
    cats = get_all_cats()
    if request.method == 'POST':
        name = request.form['name']
        image = request.form['image']
        create_cat(name, image)
        return redirect(url_for('catbook_home'))
    else:
        return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cats(id):

    cat = get_cat_by_id(id)
    return render_template(

        'cat.html',
        cat = cat

        )

@app.route('/search', methods=['GET'.'POST'])
def search():
	if request.method == "POST":
		query = request.form['search']





if __name__ == '__main__':
   app.run(debug = True)
