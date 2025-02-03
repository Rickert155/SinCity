cp -r SinCity ../Sin
cp -r case ../case
cp -r tmp ../tmp
cp __init__ ../
cp requirements.txt ../requirements.txt
cd ..
rm -r SinCity
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
