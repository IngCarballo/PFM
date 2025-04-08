from rest_framework import serializers
from .models import Movement, Category

class MovementSerializer(serializers.ModelSerializer):
    # Esta línea define cómo se serializa el campo 'category'.
    # En este caso, se usará el ID de la categoría (clave foránea).
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        # Aquí le decimos al serializer qué modelo va a utilizar.
        model = Movement

        # Estos son los campos que queremos incluir en la serialización.
        # Pueden ser leídos y/o escritos por la API.
        fields = [
            'id',            # ID del movimiento (clave primaria, solo lectura por defecto)
            'user',          # Usuario al que pertenece el movimiento
            'amount',        # Monto del ingreso o egreso
            'description',   # Descripción opcional del movimiento
            'payment_method',# Forma de pago (efectivo, tarjeta, etc.)
            'link',          # Link opcional (por ejemplo, a una factura)
            'icon',          # Nombre del icono asociado
            'date',          # Fecha del movimiento
            'category',      # Categoría del movimiento
        ]

        # Por seguridad, vamos a declarar que el campo user no se puede modificar desde el cliente directamente.
        extra_kwargs = {
            'user': {'read_only': True}
        }

    # Este método se puede usar si querés asociar automáticamente el usuario desde la request
    def create(self, validated_data):
        # Obtenemos el usuario desde el contexto (por ejemplo desde la vista)
        user = self.context['request'].user
        # Asignamos el usuario al movimiento antes de guardarlo
        validated_data['user'] = user
        # Creamos y devolvemos la instancia del modelo
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Category.
    Se usa para crear, listar o representar categorías de movimientos.
    """

    class Meta:
        model = Category           # Modelo asociado
        fields = '__all__'         # Incluye todos los campos del modelo

        # Alternativamente, podrías especificar los campos manualmente:
        # fields = ['id', 'name']
