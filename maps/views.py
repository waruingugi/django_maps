from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from maps.tasks import load_csv_coordinates


# Create your views here.
def plotting(request):
    assert isinstance(request, HttpRequest)

    coordinates = load_csv_coordinates()

    return render(
        request, 'maps/index.html',
        {'coordinates': coordinates}
    )
