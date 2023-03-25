from flask import Flask, render_template, request, jsonify
import create_wallet 

app = Flask(__name__)

@app.route("/getbalance",methods=['POST'])
def balance():
    user_addr=request.values['address']
    try :
        symbol,balance=create_wallet.get_balance(user_addr)
    except ValueError: 
        return jsonify({"meta":{'status':'fail','message':'Please make sure the address is correct.'},"data":{}}) , 400 


    return jsonify({"meta":{'status':'success','message':''},"data":{'Symbol':symbol,'Balance':balance}}) , 200 
    
@app.route("/createAccount")
def create_account():
    return jsonify({"meta":{'status':'success','message':''},"data":create_wallet.create_account()}) , 200


if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)