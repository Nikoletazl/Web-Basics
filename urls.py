from django.urls import path

from employees.employee.views import department_details, departments_list, not_found

urlpatterns = (
    path('<int:id>/', department_details),
    path('<str:id>/', department_details, name='department details'),  # departments/ID =>

    path('', departments_list, name='list departments'),
    path('not-found/', not_found),
)