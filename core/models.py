from django.db import models
from django.shortcuts import render
import requests

# Create your models here.
class input(models.Model):
    # ip_address = models.CharField(max_length=255)
    longitud = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)

class Define(models.Model):
    longitud = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    # def __init__(self, start_point, end_point):
    #     self.start_point = start_point
    #     self.end_point = end_point

    def index(self):
        response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
        geodata = response.json()
        context = {
            'ip': geodata['ip'],
            'country': geodata['country_name'],
            'latitude': geodata.get('latitude', ''),
            'longitude': geodata.get('longitude', ''),
        }
        return render(self, 'core/home.html', context)

    def define(self):
        # code
        context={
            'start':self.start_point,
            'end':self.end_point
        }
        return render(self,'core/index.html',context)
 
class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        if str(value) == '':
            html1 = "<img id='id_image' style='display:block' class='rounded float-left d-block'/>"
        else:
            html1 = "<img id='id_image' style='display:block' class='rounded float-left d-block' src='" + settings.MEDIA_URL + str(value) + "'/>"
        return mark_safe(html1)

class MyForm(forms.ModelForm):

    image_container = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = MYMODEL
        fields = '__all__'
        widgets = {
            'image': PictureWidget(),
        }
    def save(self, commit=True):
        # check image_container data
        self.instance.image.delete(False)
        imgdata = self.cleaned_data['image_container'].split(',')
        try:
            ftype = imgdata[0].split(';')[0].split('/')[1]
            fname = slugify(self.instance.title)
            self.instance.image.save('path/%s.%s' % (fname, ftype), ContentFile(imgdata[1].decode("base64")))
        except:
            pass
        return super(MyForm, self).save(commit=commit)