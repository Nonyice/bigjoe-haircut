from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

haircut_styles = [
    "Short Crop",
    "Long Layers",
    "Crew Cut",
    "Bob",
    "Pixie Cut",
    "Punk",
    "Afro",
    "Fade",
    "Undercut"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/choose_style', methods=['GET', 'POST'])
def choose_style():
    enumerated_styles = list(enumerate(haircut_styles))
    
    if request.method == 'POST':
        chosen_style = haircut_styles[int(request.form['style'])]
        return render_template('choose_style.html', styles=enumerated_styles, chosen_style=chosen_style)
    
    return render_template('choose_style.html', styles=enumerated_styles)

if __name__ == '__main__':
    app.run(debug=True)
