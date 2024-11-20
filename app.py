from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
from search.search import search_bp
from view.view import view_bp
app.register_blueprint(search_bp, url_prefix="/search")
app.register_blueprint(view_bp, url_prefix="/view")

@app.route('/')
def home():
    return redirect(url_for('search_bp.start'))

if __name__ == '__main__':
  app.run(debug=True)
