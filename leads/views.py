from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Lead , Agent
from .forms import LeadModelForm , LeadForm
from django.views import generic

# Create your views here.



class LandingPageView(generic.TemplateView):
    template_name = '_templates/pages/landing.html'
    
    
def landing_page(request):
    
    return render(request , '_templates/pages/landing.html')
    
    
class LeadListView(generic.ListView):
    
    template_name = '_templates/leads/leads_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"
    

def lead_list(request):
    
    leads = Lead.objects.all()
    
    context = {
        
        'leads' : leads
    }
    
    return render(request , '_templates/leads/leads_list.html', context)
    
    
class LeadDetailView(generic.DetailView):
    
    template_name = '_templates/leads/leads_details.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
    
def lead_detail(request,id):
    
    lead = Lead.objects.get(pk = id)
    
    print(lead)
    
    context = {
        
        'lead' : lead
    }
    return render(request , '_templates/leads/leads_details.html' , context )

    
class LeadCreateView(generic.CreateView):
    
    template_name = '_templates/leads/leads-create.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
        
        return reverse("leads_list")
    
    
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
    
class LeadUpdateView(generic.UpdateView):
    
    template_name = '_templates/leads/leads-update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads_list")
    
    
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