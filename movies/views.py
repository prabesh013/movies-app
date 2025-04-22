from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'movies':['Ironman', 'Batman', 'Interstellar']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    context = {
        'contacts':['prabesh@gmail.com', '1234567890', 'github/prabesh013']
    }
    return render(request, 'movies/about.html', context)
