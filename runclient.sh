#!/bin/bash

. ~/work/om-env/bin/activate
cd ~/workspace/messenger
python client/console.py $1
#python ~/work/client/console.py $1

#cd ~/workspace/messenger
#python client/console.py $1
#python client/ui/ui.py
#python client/omclient.py
#python client/omlistener.py

#python client/bench_cast.py

#. ~/work/rmq-samples/runclient.sh
