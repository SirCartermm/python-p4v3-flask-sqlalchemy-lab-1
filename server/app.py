from flask import jsonify
from models import Earthquake

@app.route("/earthquakes/<int:id>")
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.get(id)
    if earthquake:
        return jsonify({"id": earthquake.id, "location": earthquake.location, "magnitude": earthquake.magnitude, "year": earthquake.year})
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404