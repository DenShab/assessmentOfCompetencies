from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('userCard/<int:idcard>/', views.userCard, name='userCard'),
    path('addUser', views.addUser, name='addUser'),
    path('assessmentOfCompetencies', views.assessmentOfCompetencies, name='assessmentOfCompetencies'),
    path('department_autocomplete/', views.department_autocomplete, name='department_autocomplete'),
    path('employee_autocomplete/', views.employee_autocomplete, name='employee_autocomplete'),
    path('structuralDivision_autocomplete/', views.structuralDivision_autocomplete, name='structuralDivision_autocomplete'),
    path('materialsForEvaluation', views.materialsForEvaluation, name='materialsForEvaluation'),
    path('analysisOfResults', views.analysisOfResults, name='analysisOfResults'),
]
