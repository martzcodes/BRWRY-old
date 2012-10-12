from django.db import models
from django import forms
from django.forms import ModelForm

PORT_CHOICES = (
	('NC', 'Not Configured'),
	('A0', 'Analog 0'),
	('A1', 'Analog 1'),
	('A2', 'Analog 2'),
	('A3', 'Analog 3'),
	('A4', 'Analog 4'),
	('A5', 'Analog 5'),
	('D0', 'Digital 0'),
	('D1', 'Digital 1'),
	('D2', 'Digital 2'),
	('D3', 'Digital 3 PWM'),
	('D4', 'Digital 4'),
	('D5', 'Digital 5 PWM'),
	('D6', 'Digital 6 PWM'),
	('D7', 'Digital 7'),
	('D8', 'Digital 8'),
	('D9', 'Digital 9 PWM'),
	('D10', 'Digital 10 PWM'),
	('D11', 'Digital 11 PWM'),
	('D12', 'Digital 12'),
	('D13', 'Digital 13'),
)

PID_CHOICES = (
	('OFF', 'Off'),
	('ON', 'On'),
	('PID', 'PID'),
)

ONOFF_CHOICES = (
	('OFF', 'Off'),
	('ON', 'On'),
)
class Hardware(models.Model):
	temp_bk = models.CharField(max_length=3,blank=True, null=True)
	temp_rims = models.CharField(max_length=3,blank=True, null=True)
	temp_alt1 = models.CharField(max_length=3,blank=True, null=True)
	temp_alt2 = models.CharField(max_length=3,blank=True, null=True)
	temp_alt3 = models.CharField(max_length=3,blank=True, null=True)
	heat_bk = models.CharField(max_length=3,blank=True, null=True)
	heat_rims = models.CharField(max_length=3,blank=True, null=True)
	heat_alt1 = models.CharField(max_length=3,blank=True, null=True)
	valve1 = models.CharField(max_length=3,blank=True, null=True)
	valve2 = models.CharField(max_length=3,blank=True, null=True)
	valve3 = models.CharField(max_length=3,blank=True, null=True)
	valve4 = models.CharField(max_length=3,blank=True, null=True)
	valve5 = models.CharField(max_length=3,blank=True, null=True)
	valve6 = models.CharField(max_length=3,blank=True, null=True)
	pump1 = models.CharField(max_length=3,blank=True, null=True)
	pump2 = models.CharField(max_length=3,blank=True, null=True)
	
	def __unicode__(self):
		return self.name

class Instruction(models.Model):
	bkRadios = models.CharField(max_length=3)
	bktarget = models.CharField(max_length=3)
	rimsRadios = models.CharField(max_length=3)
	rimstarget = models.CharField(max_length=3)
	altRadios = models.CharField(max_length=3)
	alttarget = models.CharField(max_length=3)
	v1Radios = models.CharField(max_length=3)
	v2Radios = models.CharField(max_length=3)
	v3Radios = models.CharField(max_length=3)
	v4Radios = models.CharField(max_length=3)
	v5Radios = models.CharField(max_length=3)
	v6Radios = models.CharField(max_length=3)
	p1Radios = models.CharField(max_length=3)
	p2Radios = models.CharField(max_length=3)
	
	def __unicode__(self):
		return self.name