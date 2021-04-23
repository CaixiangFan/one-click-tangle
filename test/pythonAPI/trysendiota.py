from iota.crypto.types import Seed
from iota import Iota,ProposedTransaction,Address,Tag,TryteString
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

my_seed = 'PZBAJMHQOWHZUMBPNAWASU9YQMQ9AEJQSDCRVPKKIQOTVCSPLNKTSOGVNFTCGDMX9IYTLAQDIEKLALLHB'

api = Iota(adapter = url, seed = my_seed)

receiver = 'B9WSEPNPHMEIWIAUQIKUVBGKSBTIVZHFKDNWAVNWTRQUKBUWBE9VUME9DGFEHVAWNJZMEBNCOURPHYDAB'

tx = ProposedTransaction(
    address=Address(receiver),
    message=TryteString.from_unicode('This transaction should include 1i!'),
    tag=Tag('VALUETX'),
    value=1
)

input = api.get_inputs(start=0, stop=3)
print(input)
# inputs = input['inputs']
# tx = api.prepare_transfer(transfers=[tx], inputs=inputs)

# result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

# print(result)