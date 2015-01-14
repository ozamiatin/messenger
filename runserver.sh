#!/bin/bash

. runenv.sh ~/workmsg

cd $WORK_PATH/messenger
python server/console.py

