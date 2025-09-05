set -o errexit

#poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-input
pyhton manage.py migrate