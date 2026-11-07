from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data used by the /data endpoint.
sample_data = [
    {"id": 1, "name": "Java", "category": "Programming Language"},
    {"id": 2, "name": "Python", "category": "Programming Language"},
    {"id": 3, "name": "GitHub", "category": "Development Tool"},
]


@app.route("/hello", methods=["GET"])
def hello():
    """Return a welcome message in JSON format."""
    return jsonify(
        {
            "message": "Hello! Welcome to Carlos's Flask Micro-API.",
            "status": "success",
        }
    ), 200


@app.route("/data", methods=["GET", "POST"])
def data():
    """Return sample data or accept a new JSON item."""
    if request.method == "GET":
        return jsonify(
            {
                "count": len(sample_data),
                "data": sample_data,
                "status": "success",
            }
        ), 200

    new_item = request.get_json(silent=True)

    if not new_item:
        return jsonify(
            {
                "message": "Request body must contain valid JSON.",
                "status": "error",
            }
        ), 400

    required_fields = {"name", "category"}
    if not required_fields.issubset(new_item):
        return jsonify(
            {
                "message": "JSON must include 'name' and 'category'.",
                "status": "error",
            }
        ), 400

    new_record = {
        "id": len(sample_data) + 1,
        "name": new_item["name"],
        "category": new_item["category"],
    }
    sample_data.append(new_record)

    return jsonify(
        {
            "message": "Data added successfully.",
            "item": new_record,
            "status": "success",
        }
    ), 201


if __name__ == "__main__":
    app.run(debug=True)
