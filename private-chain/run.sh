#!/bin/bash

# init
geth13 --datadir . init genesis.json

# run
geth13 --datadir=$pwd \
--syncmode 'full' \
--port 30300 \
--networkid 1515 \
--miner.gasprice 1 \
--http \
--http.addr 0.0.0.0 \
--http.port 30301 \
--http.vhosts '*' \
--http.api="admin,eth,net,txpool,personal,web3,debug,miner" \
--verbosity 3 \
--ws \
--ws.port 30302 \
--allow-insecure-unlock \
--unlock 23155ca57bb606fa07a4ee58ea6eca3bc5c758ed \
--password password.txt \
--miner.etherbase 23155ca57bb606fa07a4ee58ea6eca3bc5c758ed \
--mine \
--nodekey=nodekey \

