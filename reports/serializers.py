from rest_framework import serializers
from .models import TestCallResults, TestCallResultFile


class TestCallResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCallResults
        fields = ('route', 'second_route', 'duration', 'call_date', 'cal_rec')


class FileUpload(serializers.ModelSerializer):

    class Meta:
        model = TestCallResultFile
        fields = ('file',)
