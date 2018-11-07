from charative.models import Profile, RomanceType, Genre, Chara
from django.contrib.auth.models import User
from django import forms
from django.forms import extras
from pytz import common_timezones
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class MatchingQuestions(forms.Form):

    birth_date = forms.DateField(widget=extras.SelectDateWidget)

    timezone = forms.ChoiceField(
        label=('Time Zone'),
        choices=[(t, t) for t in common_timezones]
    )

    gender = forms.ChoiceField(
        label=('Gender'),
        choices=[
            (0, 'Unknown'),
            (1, 'Female'),
            (2, 'Male'),
            (3, 'Non-Binary'),
                 ]
    )

    def __init__(self, *args, **kwargs):
        super(MatchingQuestions, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'MatchingQuestionsID'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edituser')
        self.helper.add_input(Submit('submit', 'Submit'))