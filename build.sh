coverage run -m pytest
zip lambda.zip coin_changer.py coinchanger/*.py
mkdir build
cp lambda.zip build