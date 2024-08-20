from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import IncidentSerializer, UserSerializer
from incident_app.models import Incident
from rest_framework import status
from api.utility import get_incident_id, update_user_info, create_user
from django.contrib.auth.models import User




class IncidentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # content = {'message': 'Hello, World!'}
        query_set = Incident.objects.all()
        serializer = IncidentSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        print("data: ", data)
        incident_id = get_incident_id()
        data.update({'incident_id': incident_id})
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, incident_id, format=None):
        query_set = Incident.objects.get(incident_id=incident_id)
        data = request.data
        data.update({'incident_id': query_set.incident_id, 'user': User.objects.get(id=query_set.user_id).pk})
        serializer = IncidentSerializer(query_set, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        # device = self.get_object(user_id)
        data = request.data
        query_set = User.objects.get(id=user_id)
        serializer = UserSerializer(query_set)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        print("data: ", data)
        res = create_user(data)
        if res[0]:
            return Response({'msg': 'user created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg': res[1]}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'msg': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        res = update_user_info(user, request.data)
        if res[0]:
            return Response({'msg': 'user profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(res[1], status=status.HTTP_400_BAD_REQUEST)


