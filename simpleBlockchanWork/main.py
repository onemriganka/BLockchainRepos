from flask import Flask, jsonify, request, render_template

import blockchain as _blockchain

app = Flask(__name__)
blockchain = _blockchain.Blockchain()

# Route to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to mine a new block
@app.route('/mine_block', methods=['POST'])
def mine_block():
    data = request.form.get('data')  # Get data from form submission
    if not blockchain.is_chain_valid():
        return jsonify({'message': 'The blockchain is invalid'}), 400

    block = blockchain.mine_block(data=data)
    return jsonify(block), 200

# Route to get the entire blockchain
@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    if not blockchain.is_chain_valid():
        return jsonify({'message': 'The blockchain is invalid'}), 400

    chain = blockchain.chain
    return jsonify(chain), 200

# Route to validate the blockchain
@app.route('/validate', methods=['GET'])
def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return jsonify({'message': 'The blockchain is invalid'}), 400

    return jsonify({'valid': blockchain.is_chain_valid()}), 200

# Route to get the last block
@app.route('/blockchain/last', methods=['GET'])
def previous_block():
    if not blockchain.is_chain_valid():
        return jsonify({'message': 'The blockchain is invalid'}), 400

    return jsonify(blockchain.get_previous_block()), 200


if __name__ == '__main__':
    app.run(debug=True)
