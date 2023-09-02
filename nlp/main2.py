from enum import Enum
from fastapi import FastAPI


# class food(str,Enum):
#     fruit = "apple"
#     vegetable = "carrot"
#     sweet = "chocolate"


# app = FastAPI()

# @app.get("/{foodname}")
# def foods(foodname):
#     if foodname == food.fruit:
#         return{f"{foodname}" : "eating fruit is healthy"}
#     elif foodname == food.vegetable:
#         return{f"{foodname} ": "vegetible is good for human health"}
#     return{f"{foodname}" : "i like sweet"}


food = {"fruit" : "apple","veg" : "potato"}

app = FastAPI()

@app.get("/{foodname}")
def foods(foodname):
    if foodname == food["fruit"]:
        return{f"{foodname}":"fruit is good for health"}
    return{f"{foodname}":"veg is good"}