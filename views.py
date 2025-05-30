import csv
from .models import parkinsons
from urllib import request
from django.http import HttpResponse
import joblib
from django.shortcuts import render
from joblib import load

from Admin.models import parkinsons
# model = load('C:/Users/ASUS/park/model.joblib')

model = load('C:/Users/ASUS/park/model.joblib')
# Create your views here.

def index(request):
    return render(request, 'index.html')


def export_to_csv(request):     #export to csv
    Parkinson = parkinsons.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=parkinsons.csv'
    writer = csv.writer(response)
    writer.writerow(['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
                     'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'status','RPDE', 'DFA',
                     'spread1', 'spread2', 'D2', 'PPE'])
    Parkinson_fields = Parkinson.values_list('avgfq', 'maxfq', 'minfq', 'varfq1', 'varfq2', 'varfq3', 'varfq4', 'varfq5', 'amplitude1', 'amplitude2', 'amplitude3',
                                             'amplitude4', 'amplitude5', 'amplitude6', 'noise1', 'noise2', 'result','complexity1', 'scalling', 'nonlinearfq1', 'nonlinearfq2', 'complexity2', 'nonlinearfq3')
    for Parkin in Parkinson_fields:
        writer.writerow(Parkin)
    return response


def results(request):  # ml deployment
    
    if request.method == "POST":
        
        mdfo = request.POST.get('mdfo')
        mdfhi = request.POST.get('mdfhi')
        mdflo = request.POST.get('mdflo')
        mdjit = request.POST.get('mdjit')
        mdjitt = request.POST.get('mdjitt')
        mdrap = request.POST.get('mdrap')
        mdppq = request.POST.get('mdppq')
        jittddp = request.POST.get('jittddp')
        mdshim = request.POST.get('mdshim')
        mdshimmer = request.POST.get('mdshimmer')
        shim = request.POST.get('shim')
        shimm = request.POST.get('shimm')
        mdapq = request.POST.get('mdapq')
        shimdda = request.POST.get('shimdda')
        nhr = request.POST.get('nhr')
        hnr = request.POST.get('hnr')
        rpde = request.POST.get('rpde')
        dfa = request.POST.get('dfa')
        spread1 = request.POST.get('spread1')
        spread2 = request.POST.get('spread2')
        d2 = request.POST.get('d2')
        ppe = request.POST.get('ppe')

        ob = parkinsons()

        y_pred = model.predict([[mdfo, mdfhi, mdflo, mdjit, mdjitt, mdrap, mdppq, jittddp, mdshim,
                               mdshimmer, shim, shimm, mdapq, shimdda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])

        result = y_pred
        if (y_pred[0] == 1):
            y_pred = "the patient has Parkinson's Disease"
        elif (y_pred[0] == 0):
            y_pred = "the patient does not have Parkinson's Disease"
        else:
            y_pred = "some error in processing"

        
        ob.avgfq = mdfo     #database creation
        ob.maxfq = mdfhi
        ob.minfq = mdflo
        ob.varfq1 = mdjit
        ob.varfq2 = mdjitt
        ob.varfq3 = mdrap
        ob.varfq4 = mdppq
        ob.varfq5 = jittddp
        ob.amplitude1 = mdshim
        ob.amplitude2 = mdshimmer
        ob.amplitude3 = shim
        ob.amplitude4 = shimm
        ob.amplitude5 = mdapq
        ob.amplitude6 = shimdda
        ob.noise1 = nhr
        ob.noise2 = hnr
        ob.complexity1 = rpde
        ob.scalling = dfa
        ob.nonlinearfq1 = spread1
        ob.nonlinearfq2 = spread2
        ob.complexity2 = d2
        ob.nonlinearfq3 = ppe
        ob.result = result

        ob.save()

        return render(request, 'results.html', {'results': y_pred})
    
        
    return render(request, 'index.html')


    # return render(request,'results.html',{'results':y_pred ,'mdfo':mdfo,'mdfhi':mdfhi,'mdflo ':mdflo ,'mdjit':mdjit,'mdjitt':mdjitt,'mdrap':mdrap,'mdppq':mdppq,
    #                                           'jittddp':jittddp,'mdshim':mdshim,'mdshimmer':mdshimmer,'shim':shim,'shimm':shimm,'mdapq':mdapq,'shimdda':shimdda,'nhr':nhr,' hnr': hnr ,
    #                                           'rpde':rpde,'dfa':dfa,'spread1':spread1,'spread2':spread2,'d2':d2,'ppe':ppe})


def details(request):
    return render(request, 'details.html')


def risk(request):
    return render(request, 'risk.html')

def export_view(request):
    data = parkinsons.objects.all()
    return render(request,'export.html',{'data':data})
# def export_view(request):
#     view=parkinsons.objects.all()
#     context ={
#         'data':view
#      }
#     return render(request,'export.html')




















