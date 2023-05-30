import logging
import os

import requests

from model.demoshop import DemoShop


def test_demoshop(demoqashop_session):
    # demoqashop_session.post(url="/addproducttocart/catalog/31/1/1")
    # responce = demoqashop_session.post(url="/addproducttocart/catalog/31/1/1")
    #
    # assert responce.json()["success"] is True
    # assert responce.json()["updatetopcartsectionhtml"] == "(42)"
    pass


def test_demoshop_with_object_model(demoqashop_session):
    demoshop = DemoShop(demoqashop_session)
    demoshop.add_to_cart
    cart = demoshop.add_to_cart

    assert cart.addition_success_status is True
    assert demoshop.cart.products_count == "(42)"

