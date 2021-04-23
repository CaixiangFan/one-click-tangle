from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']
# Put your seed here from Tutorial 4.a, or a seed that owns tokens (devnet)
my_seed = "IBFDSSDANPEVADCCRFYAZFMPLUJQFCND9SDIZSMGFWKDVTN9CLUWXVJTYTKQXHPCXYBYIMSXTEUBTNQDA"

# Declare an API object
api = Iota(
    adapter= url,
    seed=my_seed,
    testnet=True,
)

# Addres to receive 1i
# Feel free to replace it. For example, run the code from Tutorial 4.a
# and use that newly generated address with a 'fresh' seed.
receiver = Address(b'YLPMKSARYMVZYFEFRIRWCVKRTYMZBZMIHLBVGFZZYRSECLHYJREJQXRTASEKGWVFXOSXYSQNGGJUJQLSZ')

# print('Constructing transfer of 1i...')

tx = ProposedTransaction(
    address=receiver,
    value=90,
    message=TryteString.from_unicode('I just sent you 1i, use it wisely!'),
    tag=Tag('VALUETX'),
)

input = api.get_inputs(start=0,stop=3)
print(input)

inputs = input['inputs']
tx = api.prepare_transfer(transfers=[tx], inputs=inputs)

result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

print(result)