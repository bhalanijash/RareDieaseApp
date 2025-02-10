from flask import Flask, render_template, request, redirect, url_for
from tables import create_tables  # Ensures tables exist
from disease import get_all_diseases, add_disease, get_disease_by_id, update_disease, delete_disease

app = Flask(__name__)

# Ensure database tables exist when app starts
with app.app_context():
    create_tables()

@app.route('/')
def home():
    diseases = get_all_diseases()
    return render_template('home.html', diseases=diseases)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        add_disease(name, description)
        return redirect(url_for('home'))
    return render_template('form.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    disease = get_disease_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        update_disease(id, name, description)
        return redirect(url_for('home'))
    return render_template('form.html', disease=disease)

@app.route('/delete/<int:id>')
def delete(id):
    delete_disease(id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
