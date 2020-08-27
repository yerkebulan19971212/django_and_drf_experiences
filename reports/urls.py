from django.urls import path
from .views import write_data_to_csv_file

app_name = 'reports'
urlpatterns = [
    path('write-data-to-csv-file/', write_data_to_csv_file, name='write-data-to-csv-file')
]
