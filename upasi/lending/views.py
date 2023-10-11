from django.shortcuts import render
from .forms import MyForm


def index(request):
    return render(request, 'main/index.html')


def create_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
    else:
        form = MyForm()

    return render(request, 'lending/index.html', {'form': form})

