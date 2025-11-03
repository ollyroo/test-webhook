from flask import Flask, request

app = Flask(__name__)


@app.route('/webook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        payload = request.get_json()
        print(payload)
        # Here you can add your business logic to process the payload
        return 'Webhook received successfully', 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)