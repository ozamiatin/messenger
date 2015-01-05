#!/bin/bash

cd work/om-env
. bin/activate

cd ~/workspace/messenger
python server/console.py
#python server/omserver.py
#python server/omnotifier.py
#python server/bench_cast_srv.py
