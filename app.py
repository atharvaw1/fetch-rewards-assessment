from flask import Flask, request, jsonify
from flask_cors import CORS
from main import compare_docs


app = Flask(__name__)
CORS(app)

@app.route('/compare', methods=['POST'])
def compare_texts():
    try:
        # Get texts from the JSON payload
        data = request.get_json()
        text1 = data['text1']
        text2 = data['text2']
        metric = data['metric'] if "metric" in data else "cosine"
        n_gram = data["n_gram"] if "n_gram" in data else 2
        score = compare_docs(text1,text2,metric,n_gram)

        # Return the result as JSON
        response = {
            'similarity_score': score,
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

