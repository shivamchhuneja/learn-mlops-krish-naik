from flask import Flask, jsonify, request

app = Flask(__name__)


## Initial data
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample app"

## Retrieve items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get: item by id

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id))
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## Post: create a new task
@app.route('/items'.methods['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1
        "name":request.json


    }



if __name__ == '__main__':
    app.run(debug=True)


