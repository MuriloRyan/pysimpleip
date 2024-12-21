import json
from flask import render_template, request
from api.ipquery import IpQueryClient
from app import app

ipquery = IpQueryClient()

@app.route('/', methods=['GET', 'POST'])
def homepage():
    query = ipquery.own_ip()

    if request.method == 'POST':
        ip = request.form['ip']
        query = ipquery.get_ip(ip) if ip != '' else ipquery.own_ip()
    
    return render_template('homepage.html', ip_to_show=query.json())