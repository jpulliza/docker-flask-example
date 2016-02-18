from app import app


@app.route("/")
def main():
    return "hello world!"

@app.route("/test")
def main():
    return "Test Page."
