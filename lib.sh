mv SinCity ../SinCity
mv tmp ../tmp
mv case ../case
mv __init__.py ../
mv requirements.txt ../
cd ..

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
rm *.sh
echo "Примеры использования в case"
