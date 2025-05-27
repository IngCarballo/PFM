# `from` es una palabra reservada en Python que se utiliza para importar módulos o clases específicas de un módulo.
from django.db import models  # Importa el módulo `models` de Django para definir modelos de base de datos.
from django.contrib.auth.models import AbstractUser  # Importa `AbstractUser`, una clase base para personalizar el modelo de usuario.

# `class` es una palabra reservada en Python que se utiliza para definir una clase.
class User(AbstractUser):  # `User` es el nombre de la clase que define un modelo personalizado de usuario. Hereda de `AbstractUser`.
    # `doc_number` es un campo adicional que almacena un número de documento único para cada usuario.
    # `CharField` define un campo de texto con un límite de caracteres.
    # Documentación: https://docs.djangoproject.com/en/stable/ref/models/fields/#charfield
    doc_number = models.CharField(max_length=20, unique=True)
    
    # `rol` es un campo adicional que almacena el rol del usuario.
    rol = models.CharField(max_length=50)

# Lista de tipos de campos disponibles en Django y su documentación:
# 1. CharField: https://docs.djangoproject.com/en/stable/ref/models/fields/#charfield
# 2. TextField: https://docs.djangoproject.com/en/stable/ref/models/fields/#textfield
# 3. IntegerField: https://docs.djangoproject.com/en/stable/ref/models/fields/#integerfield
# 4. FloatField: https://docs.djangoproject.com/en/stable/ref/models/fields/#floatfield
# 5. DecimalField: https://docs.djangoproject.com/en/stable/ref/models/fields/#decimalfield
# 6. BooleanField: https://docs.djangoproject.com/en/stable/ref/models/fields/#booleanfield
# 7. DateField: https://docs.djangoproject.com/en/stable/ref/models/fields/#datefield
# 8. DateTimeField: https://docs.djangoproject.com/en/stable/ref/models/fields/#datetimefield
# 9. EmailField: https://docs.djangoproject.com/en/stable/ref/models/fields/#emailfield
# 10. URLField: https://docs.djangoproject.com/en/stable/ref/models/fields/#urlfield
# 11. FileField: https://docs.djangoproject.com/en/stable/ref/models/fields/#filefield
# 12. ImageField: https://docs.djangoproject.com/en/stable/ref/models/fields/#imagefield
# 13. ForeignKey: https://docs.djangoproject.com/en/stable/ref/models/fields/#foreignkey
# 14. ManyToManyField: https://docs.djangoproject.com/en/stable/ref/models/fields/#manytomanyfield
# 15. OneToOneField: https://docs.djangoproject.com/en/stable/ref/models/fields/#onetoonefield
# 16. SlugField: https://docs.djangoproject.com/en/stable/ref/models/fields/#slugfield
# 17. UUIDField: https://docs.djangoproject.com/en/stable/ref/models/fields/#uuidfield