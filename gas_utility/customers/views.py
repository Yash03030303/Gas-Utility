from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def home(request):
    return render(request, 'customers/home.html')

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('customers:request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/submit_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-submitted_at')
    return render(request, 'customers/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    return render(request, 'customers/request_detail.html', {'request_obj': service_request})

@login_required
def account_info(request):
    return render(request, 'customers/account_info.html', {'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})