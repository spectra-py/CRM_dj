from django.shortcuts import render , redirect
from .models import Lead , Agent
from .forms import LeadModelForm , LeadForm

# Create your views here.

def lead_list(request):
    
    leads = Lead.objects.all()
    
    context = {
        
        'leads' : leads
    }
    
    return render(request , '_templates/leads/leads_list.html', context)
    
    
    
    
def lead_detail(request,id):
    
    lead = Lead.objects.get(pk = id)
    
    print(lead)
    
    context = {
        
        'lead' : lead
    }
    return render(request , '_templates/leads/leads_details.html' , context )
    
    
    
def lead_create(request):
    
    if request.method == 'POST':
        
        form = LeadModelForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('/leads/leads-list/')
            
    context = {
        
        'form' : LeadModelForm
        
    }
    
    return render(request , '_templates/leads/leads-create.html' , context  )
    

    
    
def lead_update(request,id):
    
    

    lead = Lead.objects.get(pk = id)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads/leads-list/')
    
    context = {
        
        'form' : form,
        'lead' : lead,
        
    }
    
    return render(request , '_templates/leads/leads-update.html',context)
    
    
def lead_delete(request,id):
    
    lead = Lead.objects.get(pk = id)
    lead.delete()
    return redirect('/leads/leads-list/')