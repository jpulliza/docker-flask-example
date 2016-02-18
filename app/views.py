from app import app


@app.route("/")
def main():
    return "hello world!"

@app.route("/test")
def test_page():
    return "Test Page."
