import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hojavida_project.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin' # Puedes cambiarlo
email = 'miroslavxde@gmail.com'
password = 'Miroslav03' # Pon una clave real aquí

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superusuario '{username}' creado exitosamente.")
else:
    print(f"El usuario '{username}' ya existe.")