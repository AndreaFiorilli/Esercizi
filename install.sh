mkdir /home/user/cercastringa
copy ./cerca.py /home/user/cercastringa
copy ./requirements.txt /home/user/cercastringa
cd /home/user/cercastringa
pip3 install virtualenv
virtualenv cerca
source cerca/bin/activate
pip3 install -r requirements.txt
