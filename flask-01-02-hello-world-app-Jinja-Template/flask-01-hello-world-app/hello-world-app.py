from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Haci Eli</h1>"
@app.route("/2")
def second():
     return "This is second page"

@app.route("/3")
def third():
    return "this is subpath"

@app.route("/fourth/<string:id>")
def fourth(id):
    return f"<h1>Id of this page is {id}</h1>"
   
if __name__ == "__main__":
    app.run(debug=True)