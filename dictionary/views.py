from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import CustomUser, Dictionary, Word
from .serializers import CustomUserSerializer, UserNamesSerializer, DictionarySerializer, WordSerializer
import requests
import csv


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DictionaryViewSet(viewsets.ModelViewSet):
    # queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    filterset_fields = {'dictionary_name': ['icontains'],
                        }
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Dictionary.objects.all()
        else:
            return Dictionary.objects.filter(owner=self.request.user)

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filterset_fields = {'word_rus': ['icontains'], 'word_eng': ['icontains'], 'dictionary': ['exact'],
                        }
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_me(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def init_dict(request):
    pass
    # with open('1.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=' ')
    #     for row in csv_reader:
    #         Word.objects.create(word_rus= row[1], word_eng= row[0], dictionary_id=1)
    # return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_google_access_token(request):
    token_url = "https://oauth2.googleapis.com/token"
    token_args = {
        "code": "4/0AeaYSHD7vPup9XL71UoBVg5_6E4Ab6VCRC3R807Qpz51Icwul20Tga8zdJCFfRS5_Fy8PQ",
        "client_secret": "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",
        "client_id": "203187743059-nogl8fo77e3i3uk118emqgacr6jj5kra.apps.googleusercontent.com",
        "redirect_uri": "http://localhost:8000",
        "grant_type": "authorization_code",
    }
    token_response = requests.post(token_url, data=token_args)

    print(token_response)

    pass

@api_view(['POST'])
def user_registration(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        validated_data['is_active'] = True
        CustomUser.objects.create_user(**validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserNamesViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserNamesSerializer
    filterset_fields = {
        'username': ['exact'],
    }
