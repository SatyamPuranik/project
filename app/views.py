from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'app/home.html')

def ask(request):
  return render(request, 'app/ask.html')

def icecream(request):
  return render(request, 'app/icecream.html')

def thankyou(request):
  return render(request, 'app/thankyou.html')