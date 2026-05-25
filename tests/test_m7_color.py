def test_color_stored_in_note(client, app):
    client.post("/notes/new", data={"title": "Colorful", "body": "Hello", "tags": "", "color": "#ffcdd2"})
    assert app.notes[-1]["color"] == "#ffcdd2"


def test_color_default_white(client, app):
    client.post("/notes/new", data={"title": "Plain", "body": "Hi", "tags": ""})
    assert app.notes[-1]["color"] == "#ffffff"


def test_color_rendered_in_home(client, app):
    client.post("/notes/new", data={"title": "Blue", "body": "Sky", "tags": "", "color": "#bbdefb"})
    rv = client.get("/")
    assert b"background-color: #bbdefb" in rv.data


def test_note_without_color_key_renders_safely(client, app):
    app.notes.append({"title": "Old", "body": "Legacy note", "tags": []})
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Legacy note" in rv.data
