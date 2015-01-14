#!/bin/bash

. ~/work/om-env/bin/activate
cd ~/workspace/messenger
python server/console.py $1
#python server/omserver.py
#python server/omnotifier.py
#python server/bench_cast_srv.py
