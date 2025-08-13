#!/usr/bin/bash
cp -r SinCity ../Sin
cp -r tests ../tests
cp -r tmp ../tmp
cp __init__.py ../
cp requirements.txt ../requirements.txt
cd ..
rm -rf SinCity
mv Sin SinCity
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
