import hashlib
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from rest_framework import status
from .serializers import UserSerializer


@api_view(['GET'])
def login(request):
    userid = request.query_params.get('username')
    password = request.query_params.get('password')
    if not User.objects.filter(userid=userid).exists():
        return Response({"message": "No such User exists"}, status=status.HTTP_404_NOT_FOUND)
    user = User.objects.get(userid=userid)
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    if hashed_password != user.password_hash:
        return Response({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
    if user.role == "admin":
        serialized_data = UserSerializer(User.objects.all(), many=True).data
        return Response({"userdetails": serialized_data}, status=status.HTTP_200_OK)
    else:
        serialized_data = UserSerializer(user).data
        return Response({"userdetails": serialized_data}, status=status.HTTP_200_OK)
