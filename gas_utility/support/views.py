from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
from .forms import UpdateStatusForm
from customers.models import ServiceRequest

@login_required
@permission_required('customers.view_servicerequest', raise_exception=True)
def manage_requests(request):
    requests = ServiceRequest.objects.all().order_by('-submitted_at')
    return render(request, 'support/manage_requests.html', {'requests': requests})

@login_required
@permission_required('customers.change_servicerequest', raise_exception=True)
def update_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=service_request)
        if form.is_valid():
            updated_request = form.save(commit=False)
            if updated_request.status == 'RESOLVED' and not service_request.resolved_at:
                updated_request.resolved_at = timezone.now()
            updated_request.save()
            # Optionally, send a notification to the customer
            return redirect('support:manage_requests')
    else:
        form = UpdateStatusForm(instance=service_request)
    return render(request, 'support/update_request_status.html', {'form': form, 'request_obj': service_request})
