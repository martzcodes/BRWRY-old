from django import forms
from django.contrib.auth.models import User
from BRWRY_bootstrap.models import Hardware, PORT_CHOICES, Instruction, PID_CHOICES, ONOFF_CHOICES
from bootstrap_toolkit.widgets import BootstrapDateInput

class HardwareForm(forms.ModelForm):
	temp_bk = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	temp_rims = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	temp_alt1 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	temp_alt2 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	temp_alt3 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	heat_bk = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	heat_rims = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	heat_alt1 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	valve1 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	valve2 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	valve3 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	valve4 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	valve5 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	valve6 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	pump1 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	pump2 = forms.CharField(max_length=3,widget=forms.Select(choices=PORT_CHOICES),required=False)
	
	class Meta:
		model = Hardware

class InstructionForm(forms.ModelForm):
	bkRadios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=PID_CHOICES),required=False)
	bktarget = forms.CharField(max_length=3,required=False)
	rimsRadios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=PID_CHOICES),required=False)
	rimstarget = forms.CharField(max_length=3,required=False)
	altRadios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=PID_CHOICES),required=False)
	alttarget = forms.CharField(max_length=3,required=False)
	v1Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	v2Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	v3Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	v4Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	v5Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	v6Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	p1Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	p2Radios = forms.CharField(max_length=3,widget=forms.RadioSelect(choices=ONOFF_CHOICES),required=False)
	
	class Meta:
		model = Instruction

class BRWRYForm(forms.Form):
    date = forms.DateField(
        widget=BootstrapDateInput(),
    )
    title = forms.CharField(
        max_length=100,
        help_text=u'This is the standard text input',
    )
    disabled = forms.CharField(
        max_length=100,
        help_text=u'I am read only',
        widget=forms.TextInput(attrs={
            'disabled': 'disabled'
        })
    )
    content = forms.ChoiceField(
        choices=(
            ("text", "Plain text"),
            ("html", "HTML"),
        ),
        help_text=u'Pick your choice',
    )
    email = forms.EmailField()
    like = forms.BooleanField(required=False)
    fruits = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("apple", "Apple"),
            ("pear", "Pear"),
        ),
        help_text=u'As you can see, multiple checkboxes work too',
    )
    veggies = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("broccoli", "Broccoli"),
            ("carrots", "Carrots"),
            ("turnips", "Turnips"),
        ),
        help_text=u'And can be inline',
    )
    color = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ("#f00", "red"),
            ("#0f0", "green"),
            ("#00f", "blue"),
        ),
        help_text=u'And we have <i>radiosets</i>',
    )

    def clean(self):
        cleaned_data = super(BRWRYForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

class BRWRYTest(forms.Form):
    sensors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("t1", "Boil Kettle Temp Sensor"),
            ("t2", "RIMS Temp Sensor"),
            ("t3", "Alt Temp Sensor 1"),
            ("t4", "Alt Temp Sensor 2"),
        ),
    )

    heating = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("h1", "Boil Kettle Element"),
            ("rims", "RIMS"),
        ),
        required=False,
    )

    valves = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("v1", "Valve 1"),
            ("v2", "Valve 2"),
            ("v3", "Valve 3"),
            ("v4", "Valve 4"),
            ("v5", "Valve 5"),
            ("v6", "Valve 6"),
        ),
        required=False,
    )

    pumps = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("p1", "Pump 1"),
            ("p2", "Pump 2"),
        ),
        required=False,
    )

    def clean(self):
        cleaned_data = super(BRWRYTest, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

class BRWRYModelForm(forms.ModelForm):
    class Meta:
        model = User

class BRWRYInlineForm(forms.Form):
    query = forms.CharField(required=False, label="")
    active = forms.ChoiceField(widget=forms.RadioSelect, label="", choices=(
        ('all', 'all'),
        ('active', 'active'),
        ('inactive', 'inactive')
        ), initial='all')
    mine = forms.BooleanField(required=False, label='Mine only', initial=False)

class WidgetsForm(forms.Form):
    date = forms.DateField(widget=BootstrapDateInput)