from flask import Flask, request
from model import dog_race as dr

app = Flask(__name__)

dog_races = ["Labrador", "Golden retriever", "Poodle", "Australian shepherd", "Pitbull"]
dog_races_objects = [
    dr.DogRace("Labrador", 500.23),
    dr.DogRace("Golden retriever", 600.45),
    dr.DogRace("poodle", 1500.50)
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/races", methods=["GET"])
def show_races():
    return dog_races


@app.route("/races/<int:id>", methods=["GET"])
def show_race_by_id(id):
    if id < len(dog_races):
        return dog_races[id]
    else:
        return "not found"


@app.route("/racesv2", methods=["GET"])
def show_races_objects():
    return dog_races_objects


# data in header, niet echt super safe
@app.route("/racesv2", methods=["POST"])
def add_race_objects():
    name = request.args.get("name")
    price = float(request.args.get("price"))

    new_dog_race = dr.DogRace(name, price)
    dog_races_objects.append(new_dog_race)
    return "great succes"


@app.route("/racesv2/good", methods=["POST"])
def add_race_objects_but_good():
    name = request.form["name"]
    price: float = float(request.form["price"])

    new_dog_race = dr.DogRace(name, price)
    dog_races_objects.append(new_dog_race)
    return "greater succes"


@app.route("/racesv2", methods=["DELETE"])
def remove_race_object():
    position:int = int(request.form["pos"])

    dog_races_objects.pop(position)
    return "greatest succes"


if __name__ == '__main__':
    app.run()
