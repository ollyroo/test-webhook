from flask import Flask, request

app = Flask(__name__)

@app.route('/webook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.get_json()
        print(payload)
        return 'Webhook received successfully', 200
    if request.method == 'GET':
        return 'Webhook endpoint is live', 200

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")