from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')


def index_form(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if long_url:
            new_url = shorten_url(long_url)
            return render(request, 'new_url.html', context={'url': new_url})
    return render(request, 'index.html')

def shorten_url(url):
    headers = {
        'Authorization': 'Bearer fdd8f5079b3a79dfbc06e4f59dfe761a4f1d4571',
        'Content-Type': 'application/json'
    }

    data_dict = {"long_url": url, "domain": "bit.ly"}
    data = json.dumps(data_dict)

    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data
    )
    response_dict = json.loads(response.text)
    # print(response_dict['link'])
    return response_dict['link']

