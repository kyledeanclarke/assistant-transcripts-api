from flask import Flask, jsonify
app = Flask(__name__)

# In-memory transcripts; replace with your real data source later
transcripts = [
    {"caller": "John Doe", "date": "2025-05-20", "summary": "Final expense inquiry."},
    {"caller": "Mary Smith", "date": "2025-05-21", "summary": "Burial plan request."},
    {"caller": "Inbound Lead", "date": "2025-05-22", "summary": "Asked about rates."}
]

@app.route('/get_transcripts', methods=['GET'])
def get_transcripts():
    return jsonify(transcripts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
