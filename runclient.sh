#!/bin/bash

. runenv.sh ~/workmsg

cd $WORK_PATH/messenger
python client/console.py $1

