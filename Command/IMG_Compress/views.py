from django.shortcuts import render

# Create your views here.

def fronted_look(request):
    print("Rendering the template...")
    return render(request,"Image-Compression/index.html")