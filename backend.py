from flask import Flask, request, jsonify
from chatsql import chat_with_sql

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the AI-powered SQL Chatbot!"

@app.route('/query', methods=['GET', 'POST'])
def query_database():
    if request.method == 'GET':
        return jsonify({"message": "Use a POST request with the required data."})
    
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON format or no data received"}), 400

        query = data.get('query')
        db_user = data.get('db_user')
        db_password = data.get('db_password')
        db_host = data.get('db_host')
        db_name = data.get('db_name')

        if not all([query, db_user, db_password, db_host, db_name]):
            return jsonify({"error": "Missing required fields"}), 400

        response = chat_with_sql(query, db_user, db_password, db_host, db_name)
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
