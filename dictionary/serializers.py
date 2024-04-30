from rest_framework import serializers
from .models import CustomUser, Dictionary, Word


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password',
                  'avatar',
                  'is_superuser',
                  'is_staff',
                  'first_name',
                  'last_name',
                  'is_active',
                  'date_joined',
                  'last_login',
                  ]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UserNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class DictionarySerializer(serializers.ModelSerializer):
    # words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Dictionary
        fields = ['id', 'dictionary_name', 'description', 'date_created', 'logo', 'owner', 'get_words_count']