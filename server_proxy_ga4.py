# server_proxy_ga4.py

from flask import Flask, request, Response
import requests

app = Flask(__name__)

GA_ENDPOINT = "https://region1.analytics.google.com/g/collect"  # Usamos el endpoint correcto que has capturado

@app.route('/proxy_ga', methods=['GET'])
def proxy_ga():
    try:
        # Capturar todos los parámetros que llegan
        params = request.args.to_dict()

        # Hacer un POST al endpoint de GA4 (el real)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',  # Importantísimo
        }

        resp = requests.post(
            GA_ENDPOINT,
            headers=headers,
            params=params,
            data=b'',  # Body vacío, como has capturado
            timeout=5
        )

        return Response(status=resp.status_code)
    except Exception as e:
        print(f"Error reenviando la petición: {e}")
        return Response("Internal Server Error", status=500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
