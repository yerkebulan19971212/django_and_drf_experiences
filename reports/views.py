from .models import TestCallResults, TestCallResultFile
from django.http import HttpResponse
from .serializers import TestCallResultSerializer, FileUpload
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
import csv
from django.views.generic import View


class WriteToCSVFile(APIView):

    def get(self, request):
        test_call_results = TestCallResults.objects.all()
        serializer = TestCallResultSerializer(test_call_results, many=True)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        header = TestCallResultSerializer.Meta.fields
        # writer = csv.DictWriter(response, fieldnames=header)
        # writer.writeheader()
        with open('playerss.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            for row in serializer.data:
                writer.writerow(row)
        data = {
            "file": file
        }
        print(data)
        fgh = TestCallResultFile.objects.create(file=file)
        fgh.save()
        serializer_file = FileUpload(data=data)
        if serializer_file.is_valid():
            print("d")
            serializer_file.save()
        # TestCallResultFile.objects.create(file=file).save()

        if serializer_file.is_valid():
            print("ss")
            serializer_file.save()
        return Response("as", status=status.HTTP_200_OK)
        # return response


write_data_to_csv_file = WriteToCSVFile.as_view()
