from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django_rest_framework.quickstart.serializers import UserSerializer, GroupSerializer, UploadSerializer
import csv
from io import StringIO
import pandas as pd


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UploadViewSet(viewsets.ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        # get file
        file_uploaded = request.FILES.get('file_uploaded')        
        
        # convert file to string
        str_text = ''
        for line in file_uploaded:
            str_text = str_text + line.decode()

        # convert string to
        str_text = StringIO(str_text)

        # generate dataframe
        df = pd.read_csv(str_text, sep=";", header=[0])
        print(df)

        '''
        # alternative
        reader = csv.reader(str_text, delimiter=';')
        for row in reader:
            print('\t'.join(row))
        '''
        
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)