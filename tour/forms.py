from django import forms

from tour.models import Reservation


class ApplyForm(forms.ModelForm):

    adult = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',

    }),
        choices=(
            [('1', '1'),
             ('2', '2'),
             ('3', '3'),
             ('4', '4'), ]
        ), required=True, )

    child = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',

    }),
        choices=(
            [('1', 'Çocuk Yok'),
             ('2', '1'),
             ('3', '2'),
             ('4', '3'), ]
        ), required=True, )

    baby = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',

    }),
        choices=(
            [('1', 'Çocuk Yok'),
             ('2', '1'),
             ('3', '2'),
             ('4', '3'), ]
        ), required=True, )

    class Meta:
        model = Reservation
        fields = ['user', 'email', 'phone', 'date', 'adult', 'child', 'baby']

        widgets = {
            'user': forms.TextInput(attrs={
                'class': 'form-control '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control ',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control ',

            }),

            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'type': 'date',
                       }),

        }
