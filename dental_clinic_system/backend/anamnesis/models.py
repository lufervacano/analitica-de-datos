from django.db import models
from patients.models import Patient

class Anamnesis(models.Model):
    YES_NO_CHOICES = (
        ('S', 'Sí'),
        ('N', 'No'),
        ('NS', 'No Sabe'),
    )
    
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='anamnesis')
    date = models.DateField(auto_now_add=True)
    
    # Antecedentes médicos - campos S/N/NS
    medical_treatment = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                        verbose_name="Recibe tratamiento médico")
    medication = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                verbose_name="Toma algún medicamento")
    allergic_reactions = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                        verbose_name="Reacciones alérgicas")
    hemorrhages = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                verbose_name="Hemorragias")
    irradiated = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                verbose_name="Ha sido irradiado")
    blood_pressure_disorders = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                            verbose_name="Trastornos en presión arterial")
    sinusitis_tonsillitis = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                            verbose_name="Sinusitis y/o amigdalitis")
    respiratory_diseases = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                            verbose_name="Enfermedades respiratorias")
    heart_disease = models.CharField(max_length=2, choices=YES_NO_CHOICES, 
                                    verbose_name="Cardiopatías")
    diabetes = model# Let's complete the migration process and apply migrations to create the database
python manage.py makemigrations
python manage.py migrate

# Let's create a superuser for accessing the admin panel
python manage.py createsuperuser --username admin --email admin@example.com

# Now let's create serializers for each app
# First, let's create the authentication serializers
mkdir -p authentication/api
touch authentication/api/__init__.py
cat > authentication/api/serializers.py << 'EOF'
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']
        read_only_fields = ['id']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'password', 'password2']
        read_only_fields = ['id']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']
        read_only_fields = ['id', 'username']
