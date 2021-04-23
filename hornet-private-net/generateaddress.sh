#!/bin/bash

# Generates a new seed ensuring last trit is always 0
generateSeed() {
  local seed=$(cat /dev/urandom | LC_ALL=C tr -dc 'A-Z9' | fold -w 80 | head -n 1)$(cat /dev/urandom | LC_ALL=C tr -dc 'A-DW-Z9' | fold -w 1 | head -n 1)
  echo "$seed"
}

generateAddress() {
  echo "Generating an IOTA address holding all IOTAs..."

  local seed=$(generateSeed)
  echo $seed >./utils/nodex.seed

  # Now we run a tiny Node.js utility to get the first address to be on the snapshot
  docker-compose run --rm -w /usr/src/app address-generator sh -c 'npm install --prefix=/package "@iota/core" > /dev/null && node address-generator.js $(cat nodex.seed) 2> /dev/null > address.txt'
}

generateAddress2() {
  echo "Generating an IOTA address holding all IOTAs..."

  echo $1 >./utils/nodex.seed

  # Now we run a tiny Node.js utility to get the first address to be on the snapshot
  docker-compose run --rm -w /usr/src/app address-generator sh -c 'npm install --prefix=/package "@iota/core" > /dev/null && node address-generator.js $(cat nodex.seed) 2> /dev/null > address.txt'
}

if [ $# -lt 1 ]; then
  generateAddress
else
  generateAddress2 $1
fi

echo "Seed:$(cat ./utils/nodex.seed)" >> seeds.txt
echo "Addr:$(cat ./utils/address.txt)" >> seeds.txt
