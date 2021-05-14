from iota.crypto.types import Seed
from iota import Iota
import json,sys

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

my_seed = 'YGCOACXP9SCGRWZBXLMIINVDFSDHKKIFCPNWYQGX9VRMM99VCHXFTNLELCHNJQTLTFTXRZBGEKUUGOPM9'

if len(sys.argv) == 2:
    my_seed = sys.argv[1]

api = Iota(adapter = url, seed = my_seed)

input = api.get_inputs(start=0,stop=10)
print(input)