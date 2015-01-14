#!/bin/bash

. runenv.sh ~/workmsg

cd $WORK_PATH/oslo.messaging/messenger
python client/console.py $1

