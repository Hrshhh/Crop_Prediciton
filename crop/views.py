from django.shortcuts import render
from .models import PredictCrop
from django.http import JsonResponse
import pandas as pd

# Create your views here.

def index(request):
    return render(request,'index.html')

def predict(request):
    if request.POST.get('action') == 'post':
        n = float(request.POST.get("n"))
        p = float(request.POST.get("p"))
        k = float(request.POST.get("k"))
        temperature = float(request.POST.get("temp"))
        humidity = float(request.POST.get("humidity"))
        ph = float(request.POST.get("ph"))
        rainfall = float(request.POST.get("rainfall"))
        model = pd.read_pickle(r'C:\Users\Dell\Downloads\cropprediction\cropprediction\RFmodel.pkl')
        result = model.predict([[n,p,k,temperature,humidity,ph,rainfall]])
        label = result[0]
        print(n,p,k,temperature,humidity,ph,rainfall,label)
        PredictCrop.objects.create(n=n,p=p,k=k,temperature=temperature,humidity=humidity,ph=ph,rainfall=rainfall)
        return JsonResponse({'n':n,
            'p':p,
            'k':k,
            'temperature':temperature,
            'humidity': humidity,
            'ph': ph,
            'rainfall': rainfall,
            'label':label},safe=False)

def crop(request):
    return render(request,'predict.html')