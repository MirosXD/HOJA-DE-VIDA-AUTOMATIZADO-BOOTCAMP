import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hojavida_project.settings')
django.setup()

from django.contrib.auth.models import User

# Crea el usuario mirosxd si no existe
username = 'mirosxd'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, 'admin@test.com', '123456789')
    print("✅ USUARIO CREADO: Ahora puedes entrar con mirosxd y 123456789")
else:
    print("⚠️ EL USUARIO YA EXISTE")