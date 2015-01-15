#!/bin/bash

export WORK_PATH=$1
export OM_ENV_PATH=$WORK_PATH/om-env

if [ ! -d "$OM_ENV_PATH" ]; then

	virtualenv $OM_ENV_PATH
	
	. $OM_ENV_PATH/bin/activate
#	pip install -r $WORK_PATH/oslo.messaging/requirements.txt
#	pip install -e $WORK_PATH/oslo.messaging/
	pip install oslo.messaging
	pip install pyzmq
else
	. $OM_ENV_PATH/bin/activate
fi

export PYTHONPATH=$PYTHONPATH:$WORK_PATH/messenger:$WORK_PATH/oslo.messaging

