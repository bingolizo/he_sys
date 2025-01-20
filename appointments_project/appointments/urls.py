from django.urls import path
from .views import SetAppointmentView, CancelAppointmentView, RescheduleAppointmentView, ListAppointmentsView

urlpatterns = [
    path('set/', SetAppointmentView.as_view(), name='set-appointment'),
    path('cancel/<int:pk>/', CancelAppointmentView.as_view(), name='cancel-appointment'),
    path('reschedule/<int:pk>/', RescheduleAppointmentView.as_view(), name='reschedule-appointment'),
    path('list/', ListAppointmentsView.as_view(), name='list-appointments'),
]
