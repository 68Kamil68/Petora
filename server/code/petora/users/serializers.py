from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from better_profanity import profanity


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]

    def validate_username(self, value):
        if profanity.contains_profanity(value):
            raise serializers.ValidationError("Your username cannot contain swear words")
        else:
            return value

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
