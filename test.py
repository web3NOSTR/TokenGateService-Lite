from web3 import Web3
w3 = Web3(
Web3.HTTPProvider(
"https://mainnet.base.org"
)
)
# get latest block details
w3.eth.getBlock('latest')
# get latest block number
w3.eth.blockNumber




