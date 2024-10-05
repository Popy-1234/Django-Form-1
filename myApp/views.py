from django.shortcuts import render


from .models import Student

def form(request):
    

    return render(request,'form.html',{"F":form})