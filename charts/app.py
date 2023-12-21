from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def graph():
    render_template(graph.html,values=values)


if __name__ == '__main__':
    app.run(debug=True)