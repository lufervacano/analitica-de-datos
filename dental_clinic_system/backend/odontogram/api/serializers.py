from rest_framework import serializers
from odontogram.models import Odontogram

class OdontogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odontogram
        fields = '__all__'
   # Let's check if the migrations were created properly and apply them
python manage.py makemigrations
python manage.py migrate

# Let's create a superuser for accessing the admin panel
python manage.py createsuperuser --username admin --email admin@example.com --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin'); user.set_password('admin123'); user.save()"

# Let's update the authentication models and URL configuration
cat > authentication/api/views.py << 'EOF'
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return super().get_permissions()

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
