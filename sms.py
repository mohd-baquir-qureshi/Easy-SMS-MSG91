import requests
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to SMS Python Server"

@app.route('/<sid>/<num>/<msg>')
def msg(sid,num,msg):
    authKey = {YOUR MSG91 AUTH KEY}
    smsUrl = 'http://api.msg91.com/api/sendhttp.php?route=4&sender=%s&mobiles=91%s&authkey=authKey&message=%s&country=91' % (sid,num,msg)
    sendSms = requests.get(smsUrl)
    balanceUrl = 'https://control.msg91.com/api/balance.php?authkey=authKey&type={1=>PROMOTIONAL, 2=>TRANSACTIONAL, 106=>OTP}'
    remainingBalance = requests.get(balanceUrl).text
    return remainingBalance

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
