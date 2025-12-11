from flask import Flask,jsonify,request
app = Flask(__name__)
employee=["anu","divya","arthi"]

#GET->return full list
@app.route("/list",methods=["GET"])
def get_list():
    return jsonify(employee)

#POST-> add a new item
@app.route("/list",methods=["POST"])
def add_list():
    data=request.get_json()
    new_employee=data.get("employee")
    employee.append(new_employee)
    return "POST EXECUTED"

#PUT->update an item by index
@app.route("/list/<int:index>",methods=["PUT"])
def update_list(index):
    data=request.get_json()
    new_employee=data.get("employee")
    employee[index]=new_employee
    return "PUT EXECUTED"


#DELETE-> delete an item by index
@app.route("/list/<int:index>",methods=["DELETE"])
def delete_list(index):
    employee.pop(index)
    return "DELETE EXECUTED"

if __name__ == "__main__":
    app.run(debug=True)