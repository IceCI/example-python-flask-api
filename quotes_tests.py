import pytest
import quotes


@pytest.fixture()
def app():
    app = quotes.app
    return app


@pytest.fixture()
def create_quote():
    q = quotes.Quote(author='Guido van Rossum',
                     quote="Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered.")
    quotes.db.session.add(q)
    quotes.db.session.commit()


def test_index(client):
    assert client.get('/').status_code == 200


@pytest.mark.usefixtures('create_quote')
def test_quote(client):
    result = client.get('/quote')
    assert result.status_code == 200
    data = result.json
    assert len(data['quotes']) == 1
