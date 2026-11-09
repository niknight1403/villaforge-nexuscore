from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for registered villages
registered_villages = {}

@app.route('/villages', methods=['POST'])
def register_village():
    data = request.get_json()
    village_id = data['id']
    registered_villages[village_id] = data
    return jsonify({'message': 'Village registered successfully'}), 201

@app.route('/villages', methods=['GET'])
def get_villages():
    return jsonify(registered_villages)

if __name__ == '__main__':
    app.run(debug=True)