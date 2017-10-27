# Install

1. cd theshop_server
2. conda create -n theshop-server python=3.6
3. source activate theshop-server
4. pip install -r requirements.txt
5. python manage.py makemigration
6. python manage.py createsuperuser