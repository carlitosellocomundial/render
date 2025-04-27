from flask import Flask, request, Response
import requests

app = Flask(__name__)

GA_ENDPOINT = "https://www.google-analytics.com/mp/collect"

@app.route('/proxy_ga', methods=['POST'])
def proxy_ga():
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        resp = requests.post(GA_ENDPOINT, headers=headers, params=request.args, data=request.data, timeout=5)
        return Response(status=resp.status_code)
    except Exception as e:
        print(f"Error reenviando la petición: {e}")
        return Response("Internal Server Error", status=500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)