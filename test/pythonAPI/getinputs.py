from iota.crypto.types import Seed
from iota import Iota
import json,sys

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

my_seed = 'JSFCIXUGZADG9UWIIXKXKQXHNWPUJLWTOUJWMVMLSOI9BR9ONMSOBTNSN9XHITHHUQR9HVLFBIPHJUZEB'

if len(sys.argv) == 2:
    my_seed = sys.argv[1]

api = Iota(adapter = url, seed = my_seed)

input = api.get_inputs(start=0, stop=3)
print(input)