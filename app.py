from flask import Flask, session, request, jsonify, send_from_directory, render_template
from web3 import Web3
from eth_account.messages import encode_defunct
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Access environment variables
web3_provider_url = os.getenv('WEB3_HTTP_PROVIDER')
token_contract_address = Web3.toChecksumAddress(os.getenv('TOKEN_CONTRACT_ADDRESS'))
SECRET_FLASK_KEY = os.getenv('SECRET_FLASK_KEY')

app.secret_key = SECRET_FLASK_KEY

# Setup Web3
web3 = Web3(Web3.HTTPProvider(web3_provider_url))

# ERC-20 Token standard ABI snippet for balanceOf method
TOKEN_ABI_SNIPPET = '''
[
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
'''


def validateUser():
    session['tokenHolder'] = True

@app.route('/verify-token', methods=['POST'])
def verify_token():
    data = request.get_json()
    message = data.get('message')
    signature = data.get('signature')

  

    try:
        # Recover the address from the signature
        message = encode_defunct(text=message)
        recovered_address = Account.recover_message(message, signature=signature)
        recovered_address = Web3.toChecksumAddress(recovered_address)

        # Check if the recovered address holds the token
        token_contract = web3.eth.contract(address=token_contract_address, abi=TOKEN_ABI_SNIPPET)
        balance = token_contract.functions.balanceOf(recovered_address).call()
        holding = balance > 0


        print(f"token_contract {token_contract_address} address: {recovered_address} balance: {balance}")



        if holding:
            validateUser()

        return jsonify({'success': True, 'address': recovered_address, 'holding': holding}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/')
def serve_html():
    return send_from_directory(os.path.join(os.getcwd(), 'static'), 'index.html')


@app.route('/test')
def index():
    # Check if the user is logged in (example use case)
    if 'tokenHolder' in session:
        tokenHolder = session['tokenHolder']
        return f'Currently the valid user is  {tokenHolder}'
    return 'You are not logged in'





@app.route('/membersOnly')
def serveMembersOnly():
    if 'tokenHolder' in session:
        tokenHolder = session['tokenHolder']
        # return send_from_directory(os.path.join(os.getcwd(), 'static'), 'membersOnly.html')
        return render_template("membersOnly.html")
    else:
        # return send_from_directory(os.path.join(os.getcwd(), 'static'), 'denied.html')
        return render_template("denied.html")



if __name__ == '__main__':
    app.run(debug=True)
