from django import forms

from apps.clients.models import Client


class ClientAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientAdminForm, self).__init__(*args, **kwargs)
        self.fields['ib'].queryset = Client.objects.filter(client_type=Client.CLIENT_TYPE_IB)
        self.fields['sales'].queryset = Client.objects.filter(client_type=Client.CLIENT_TYPE_SALES)