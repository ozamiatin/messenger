#!/bin/bash

. runenv.sh

cd $WORK_PATH/messenger
python client/console.py $1

