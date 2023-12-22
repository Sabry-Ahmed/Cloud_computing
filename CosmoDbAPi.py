from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from pymongo import MongoClient



app = Flask(__name__)
load_dotenv()
mongodb_password = os.getenv("MONGODB_PASSWORD")

connection_string = "mongodb+srv://test:{mongodb_password}@joker.mongocluster.cosmos.azure.com/?authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000&appName=mongosh+1.10.1"
client = MongoClient(connection_string)
db = client['quickstartDB']
collection = db['sampleCollection']

# API endpoints

# Get all documents in the collection
@app.route('/api/data', methods=['GET'])
def get_all_data():
    documents = list(collection.find())
    return jsonify(documents), 200

# Get a specific document by ID
@app.route('/api/data/<string:data_id>', methods=['GET'])
def get_data(data_id):
    data = collection.find_one({'_id': ObjectId(data_id)})
    if data:
        return jsonify(data), 200
    return jsonify({'message': 'Data not found'}), 404

# Insert a new document
@app.route('/api/data', methods=['POST'])
def insert_data():
    new_data = request.json
    if new_data:
        insert_result = collection.insert_one(new_data)
        return jsonify({'message': 'Data inserted', 'id': str(insert_result.inserted_id)}), 201
    return jsonify({'message': 'No data provided'}), 400

# Update a document
@app.route('/api/data/<string:data_id>', methods=['PUT'])
def update_data(data_id):
    update_data = request.json
    if update_data:
        result = collection.update_one({'_id': ObjectId(data_id)}, {'$set': update_data})
        if result.modified_count > 0:
            return jsonify({'message': 'Data updated'}), 200
        return jsonify({'message': 'Data not found'}), 404
    return jsonify({'message': 'No data provided'}), 400

# Delete a document
@app.route('/api/data/<string:data_id>', methods=['DELETE'])
def delete_data(data_id):
    result = collection.delete_one({'_id': ObjectId(data_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Data deleted'}), 200
    return jsonify({'message': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
