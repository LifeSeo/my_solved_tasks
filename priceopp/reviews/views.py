from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewForm

# def reviews(request):
#     reviews = Reviews.objects.all()
#     return render(request, 'reviews/reviews.html', {'reviews': reviews})

def reviews(request):
    error = ''
    if request.method == 'POST':
        
        form = ReviewForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')

        else:
            error = 'The fields are not filled in correctly'
            
    form = ReviewForm()
    
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'reviews/reviews.html', data)
