from flask import Flask, request, redirect, url_for, jsonify
from wifi_change import changer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def received_api():
    request_data = request.get_json()
    wifi_name = request_data['wifi_name']
    wifi_password = request_data['wifi_password']
    ip = request_data['ip']
    keep_ssid = request_data['keep_ssid']
    if len(wifi_name) >= 1 and len(wifi_password) >= 8 and int(keep_ssid) == True:
        if keep_ssid == 1 or keep_ssid == 2:           
            changer(ip, wifi_name, wifi_password, keep_ssid)
            return jsonify({'message': 'Foi feito a configuração do wifi com sucesso'})
        else:
            return jsonify({'message': 'Separar redes inválido', 'success' : False})
    else:
        return jsonify({'message': 'Condições invalidas, verifique os valores.', 'success' : False})

app.run(host="0.0.0.0", port=5000, ssl_context='adhoc', debug=False)