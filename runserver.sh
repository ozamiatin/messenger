#!/bin/bash

. runenv.sh ~/workmsg

cd $WORK_PATH/oslo.messaging/messenger
python server/console.py

