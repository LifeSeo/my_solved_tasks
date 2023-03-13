from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewForm

def reviews(request):
    reviews = Reviews.objects.all()
    return render(request, 'reviews/reviews.html', {'reviews': reviews})

def review_add(request):
    form = ReviewForm()
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'The fields are not filled in correctly'
    
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'reviews/review_add.html', data)
