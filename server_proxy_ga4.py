from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

GA_ENDPOINT = "https://www.google-analytics.com/mp/collect"

@app.route('/proxy_ga', methods=['POST', 'GET'])  # <-- aceptar también GET
def proxy_ga():
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        if request.method == 'POST':
            data = request.data
            params = request.args
        else:  # Si es GET, sacar el JSON de un parámetro 'payload'
            payload = request.args.get('payload')
            if not payload:
                return Response("Missing payload", status=400)
            data = payload.encode('utf-8')
            params = {
                'measurement_id': request.args.get('measurement_id'),
                'api_secret': request.args.get('api_secret', 'fake_secret')
            }
        
        resp = requests.post(GA_ENDPOINT, headers=headers, params=params, data=data, timeout=5)
        return Response(status=resp.status_code)
    except Exception as e:
        print(f"Error reenviando la petición: {e}")
        return Response("Internal Server Error", status=500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
