from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import ThreatIncident
from .forms import ThreatIncidentForm

# 1. User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

# 2. User Logout View
def logout_view(request):
    auth_logout(request)
    return redirect('login')

# 3. User-Friendly Dashboard View (Protected)
@login_required(login_url='login')
def dashboard_view(request):
    incidents = ThreatIncident.objects.all().order_by('-detected_at')
    
    # Calculate key metrics for dashboard indicators
    total_incidents = incidents.filter(is_false_positive=False).count()
    false_positives = incidents.filter(is_false_positive=True).count()
    critical_incidents = incidents.filter(severity='CRITICAL').count()

    context = {
        'incidents': incidents[:5],  # Display the 5 most recent live events
        'total_incidents': total_incidents,
        'false_positives': false_positives,
        'critical_incidents': critical_incidents,
    }
    return render(request, 'core/dashboard.html', context)

# 4. Report of Threat Incidences View (Protected)
@login_required(login_url='login')
def reports_view(request):
    all_incidents = ThreatIncident.objects.all().order_by('-detected_at')
    
    if request.method == 'POST':
        form = ThreatIncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reports')
    else:
        form = ThreatIncidentForm()
        
    return render(request, 'core/reports.html', {'incidents': all_incidents, 'form': form})