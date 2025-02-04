#!/usr/bin/bash
cp -r SinCity ../Sin
cp -r case ../case
cp -r tmp ../tmp
cp __init__.py ../
cp requirements.txt ../requirements.txt
cp manifest.py ../manifest.py
cd ..
rm -rf SinCity
mv Sin SinCity
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
