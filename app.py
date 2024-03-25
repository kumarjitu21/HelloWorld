from flask import Flask
import connexion

app = connexion.FlaskApp(__name__, specification_dir='openapi/')

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.add_api('openapi.yaml')
    app.run(port=8080, debug=True)
