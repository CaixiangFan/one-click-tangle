from iota.crypto.types import Seed
from iota import Iota
import json,sys

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

my_seed = 'YNXXCRIRSDQURJBUOBOVGIDEOOYLCNAQKJSCVMLZWQQ99BYE9GLJNFIJNVHWSGFBCIECXJJZFSL9RCROA'

if len(sys.argv) == 2:
    my_seed = sys.argv[1]

api = Iota(adapter = url, seed = my_seed)

acount_data = api.get_account_data(start=0)
print(acount_data)