from pytest_voluptuous import S
from schemas.cats import cats_list

def test_abyssinian_cat(ninjas):
    responce = ninjas.get(url='/cats',
                          params={"name": 'abyssinian'})
    print(responce.text)
    assert S(cats_list) == responce.json()
