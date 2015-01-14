export WORK_PATH=$1

git clone git@github.com:ozamiatin/messenger.git $WORK_PATH/messenger
cd $WORK_PATH/messenger

git checkout origin/om
git checkout -b om

cd ~
ln -s $WORK_PATH/messenger/runenv.sh
ln -s $WORK_PATH/messenger/runserver.sh
ln -s $WORK_PATH/messenger/runclient.sh
