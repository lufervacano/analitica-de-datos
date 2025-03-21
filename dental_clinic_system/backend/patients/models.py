from django.db import models
from authentication.models import User

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    
    MARITAL_STATUS_CHOICES = (
        ('soltero', 'Soltero/a'),
        ('casado', 'Casado/a'),
        ('divorciado', 'Divorciado/a'),
        ('viudo', 'Viudo/a'),
        ('union_libre', 'Unión Libre'),
    )
    
    BENEFICIARY_TYPE_CHOICES = (
        ('cotizante', 'Cotizante'),
        ('beneficiario', 'Beneficiario'),
    )
    
    # Información básica del paciente
    medical_record_number = models.CharField(max_length=20, unique=True, verbose_name="Número de Historia Clínica")
    record_date = models.DateField(verbose_name="Fecha de Diligenciamiento")
    assigned_dentist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patients',
                                      verbose_name="Odontólogo Asignado")
    
    # Información personal
    first_name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos")
    id_number = models.CharField(max_length=20, unique=True, verbose_name="Cédula de Ciudadanía")
    age = models.PositiveIntegerField(verbose_name="Edad")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento")
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, verbose_name="Estado Civil")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Sexo")
    
    # Información de seguridad social
    eps = models.CharField(max_length=50, verbose_name="EPS")
    beneficiary_type = models.CharField(max_length=20, choices=BENEFICIARY_TYPE_CHOICES, 
                                        verbose_name="Cotizante o Beneficiario")
    
    # Información de contacto
    address = models.CharField(max_length=100, verbose_name="Dirección")
    neighborhood = models.CharField(max_length=50, verbose_name="Barrio")
    city = models.CharField(max_length=50, verbose_name="Municipio")
    home_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono Residencia")
    office_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono Oficina")
    occupation = models.CharField(max_length=100, verbose_name="Ocupación")
    
    # Información de emergencia
    emergency_contact = models.CharField(max_length=100, verbose_name="En caso de emergencia avisar a")
    emergency_relationship = models.CharField(max_length=50, verbose_name="Parentesco")
    emergency_phone = models.CharField(max_length=20, verbose_name="Teléfono de Emergencia")
    
    # Motivo de consulta
    reason_for_consultation = models.TextField(verbose_name="Motivo de la Consulta")
    
    # Metadatos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.medical_record_number}"
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['-created_at']
