from rest_framework import serializers
from .models import User, Student, Teacher
import jwt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password','is_student','is_teacher']
        extra_kwargs = {
        'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        if validated_data.get('is_student'):
            Student.objects.create(user=instance, phone_number=validated_data.get('phone_number'))
        elif validated_data.get('is_teacher'):
            Teacher.objects.create(user=instance, phone_number=validated_data.get('phone_number'))
        return instance
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'phone_number','email', 'password','is_student','is_teacher']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'phone_number','email', 'password','is_student','is_teacher']