from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plagiarism-check-mainpage'),
    # path('download-report/', views.download_report, name='download-report'),
    # path('report/', views.report, name='report'),
    path('compare/', views.fileCompare, name='compare'),
    path('test/', views.test, name='Test'),
    path('filetest/', views.filetest, name='filetest'),
    path('twofiletest1/', views.twofiletest1, name='twofiletest1'),
    path('twofilecompare1/', views.twofilecompare1, name='twofilecompare1'),
]

