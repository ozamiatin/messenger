#!/bin/bash

export WORK_PATH="~/workspace"
export OM_ENV_PATH="~/work/om-env"

if [! -d "$OM_ENV_PATH"]; then

	virtualenv $OM_ENV_PATH
	git clone git@github.com:openstack/oslo.messaging.git $WORK_PATH
	
	. $OM_ENV_PATH/bin/activate
	pip install -r $WORK_PATH/oslo.messaging/requirements.txt
else
	. $OM_ENV_PATH/bin/activate
	export PYTHONPATH=$PYTHONPATH:$WORK_PATH/messenger:$WORK_PATH/oslo.messaging
fi

