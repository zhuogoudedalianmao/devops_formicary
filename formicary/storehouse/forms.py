#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms

from .models import School, Server


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'city']

    i_am_sure = forms.BooleanField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)

        if self.errors.get('i_am_sure'):
            # show the 'are you sure' checkbox when we want confirmation
            self.fields['i_am_sure'].widget = forms.CheckboxInput()

    def clean(self):
        cleaned_data = super(SchoolForm, self).clean()

        if not self.errors:
            # only validate i_am_sure once all other validation has passed
            i_am_sure = cleaned_data.get('i_am_sure')
            if self.instance.id and not i_am_sure:
                self._errors['i_am_sure'] = self.error_class(["Are you sure you want to change this school?"])
                del cleaned_data['i_am_sure']
        return cleaned_data


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = [
            'core_number',
            'memory_capacity',
            'disk_capacity',
            'device_type',
            'os_type',
            'access_type',
            'access_addr',
            'username',
            'password',
            'public_network_addr',
            'private_network_addr',
            'domain_name',
            'remark',
            'manage_url',
            'school_url',
            'deploymentversion',
            'special_modify',
            'deploymentremake'
        ]

    i_am_sure = forms.BooleanField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)

        if self.errors.get('i_am_sure'):
            # show the 'are you sure' checkbox when we want confirmation
            self.fields['i_am_sure'].widget = forms.CheckboxInput()

    def clean(self):
        cleaned_data = super(ServerForm, self).clean()

        if not self.errors:
            # only validate i_am_sure once all other validation has passed
            i_am_sure = cleaned_data.get('i_am_sure')
            if self.instance.id and not i_am_sure:
                self._errors['i_am_sure'] = self.error_class(["Are you sure you want to change this server?"])
                del cleaned_data['i_am_sure']
        return cleaned_data
