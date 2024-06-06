echo "BUILD START"

# Install pip if not available
python3.9 -m ensurepip --upgrade
python3.9 -m pip install --upgrade pip

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
