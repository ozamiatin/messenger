#!/bin/bash

cd work/om-env
. bin/activate

cd ~/workspace/messenger
python server/console.py
#python server/omserver.py