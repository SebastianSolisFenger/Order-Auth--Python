# IMPORT PRODUCTS FROM FILE
from MockedDatabase.dataBase import products


def checkProductPrice(productName):
    for product in products:
        if product["name"] == productName:
            return product["price"]
