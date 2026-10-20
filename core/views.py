from django.shortcuts import render, redirect
from .models import MultimediaItem
from .forms import MultimediaForm

def index(request):
    if request.method == 'POST':
        form = MultimediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MultimediaForm()
    
    items = MultimediaItem.objects.all().order_by('-uploaded_at')
    return render(request, 'core/index.html', {'form': form, 'items': items})