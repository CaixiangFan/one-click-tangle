#////////////////////////////////////////////////
#// Generate an unspent address
#////////////////////////////////////////////////

from iota import Iota
from iota.crypto.types import Seed
import sys
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

seed = Seed.random()

if len(sys.argv) == 2:
    seed = sys.argv[1]

print("seed: ", seed)

# The seed that will be used to generate an address
# seed = 'PUETPSEITFEVEWCWBTSIZM9NKRGJEIMXTULBACGFRQK9IMGICLBKW9TTEVSDQMGWKBXPVCBMMCXWMNPDX'

# Connect to a node
api = Iota(url, seed, testnet = True)

# Define the security level of the address
security_level = 2

# Generate an unspent address with security level 2
address = api.get_new_addresses(index=0, count=1, security_level = security_level)['addresses'][0]

is_spent = api.were_addresses_spent_from([address])['states'][0]

if is_spent:
    print('Address %s is spent!' % address )
else:
    print('Your address is: %s' % address )