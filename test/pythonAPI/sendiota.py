from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']
# Put your seed here from Tutorial 4.a, or a seed that owns tokens (devnet)
my_seed = "PZBAJMHQOWHZUMBPNAWASU9YQMQ9AEJQSDCRVPKKIQOTVCSPLNKTSOGVNFTCGDMX9IYTLAQDIEKLALLHB"

# Declare an API object
api = Iota(
    adapter= url,
    seed=my_seed,
    testnet=True,
)

# Addres to receive 1i
# Feel free to replace it. For example, run the code from Tutorial 4.a
# and use that newly generated address with a 'fresh' seed.
receiver = Address(b'B9WSEPNPHMEIWIAUQIKUVBGKSBTIVZHFKDNWAVNWTRQUKBUWBE9VUME9DGFEHVAWNJZMEBNCOURPHYDAB')

# print('Constructing transfer of 1i...')
# Create the transfer object
tx = ProposedTransaction(
    address=receiver,
    value=1,
    message=TryteString.from_unicode('I just sent you 1i, use it wisely!'),
    tag=Tag('VALUETX'),
)

# print(tx.as_tryte_string())

# print('Preparing bundle and sending it to the network...')
# Prepare the transfer and send it to the network
# response = api.send_transfer(transfers=[tx], security_level=2)
response = api.get_inputs(start=0)
print(response)
# print(api.get_balances())
# input0 = response['inputs'][0] # type: Address  
# print(input0.balance) # 42 
# print('Check your transaction on the Tangle!')
# print('https://utils.iota.org/bundle/%s/devnet' % response['bundle'].hash)