export WORK_PATH=~/workmsg
IM_PATH=$WORK_PATH/messenger

git clone git@github.com:openstack/oslo.messaging.git $WORK_PATH/oslo.messaging
git clone git@github.com:ozamiatin/messenger.git $IM_PATH
cd $IM_PATH

git checkout origin/om
git checkout -b om

cd ~
ln -s $IM_PATH/runenv.sh
ln -s $IM_PATH/runserver.sh
ln -s $IM_PATH/runclient.sh

. runenv.sh $WORK_PATH

