from flask import Flask, request, Response
import requests
import urllib.parse

app = Flask(__name__)

GA_ENDPOINT = "https://region1.analytics.google.com/g/collect"

@app.route('/proxy_ga', methods=['GET'])
def proxy_ga():
    try:
        # Capturar todos los parámetros
        params = request.args.to_dict()

        # Codificar los parámetros como x-www-form-urlencoded
        data_encoded = urllib.parse.urlencode(params)

        # Headers para el POST
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Hacer POST con los parámetros en el BODY (no en la URL)
        resp = requests.post(
            GA_ENDPOINT,
            headers=headers,
            data=data_encoded,  # 🔥 Aquí está el cambio 🔥
            timeout=5
        )

        return Response(status=resp.status_code)
    except Exception as e:
        print(f"Error reenviando la petición: {e}")
        return Response("Internal Server Error", status=500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
