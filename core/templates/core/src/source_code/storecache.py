from django.shortcuts import render
import requests
def home(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        params = {'access_key': settings.IPSTACK_API_KEY}
        response = requests.get('http://api.ipstack.com/103.216.51.117?access_key=c3ae01b20017a4dc59fa423101f5fe05')
        # response = requests.get('http://api.ipstack.com/%s' % ip_address, params=params)
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    return render(request, 'core/home.html', {
        'ip': geodata.get('ip'),
        'country': geodata.get('country_name', ''),
        'latitude': geodata.get('latitude', ''),
        'longitude': geodata.get('longitude', ''),
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'is_cached': is_cached
    })