from app import app

def test_index():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b"hello, world"
