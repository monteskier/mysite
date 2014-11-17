__author__ = 'joaquin'
from django import forms
from models import Reserva
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.widgets import AdminSplitDateTime
class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['objecte', 'user', 'sala', 'data_inici', 'data_final']
        exclude = ['data_sol']

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)

        self.fields['data_inici'].widget = AdminDateWidget()
        self.fields['data_final'].widget = AdminDateWidget()
