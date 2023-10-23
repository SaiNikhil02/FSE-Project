from django.shortcuts import render 
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  
from django.contrib.auth.decorators import login_required
from .models import GameScore  
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm


def show_2048(request):
    return render(request, 'index.html') 

'''
def dashboard(request):
    scores = GameScore.objects.filter(player=request.user)[:5]  # Get the last 5 scores
    return render(request, 'dashboard.html', {'scores': scores}) 
'''
# @require_POST
# @login_required
# def save_score(request):
#     data = json.loads(request.body)
#     score = data.get('score')

#     if score is not None:
#         GameScore.objects.create(player=request.user, score=score)
#         return JsonResponse({"success": True})

#     return JsonResponse({"success": False}, status=400)  

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # or your desired redirect
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form}) 


def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:  # user should be None if authentication failed
                login(request, user)
                return redirect('show_2048')  # Redirect to a success page.
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    # Perform any custom actions you want here before the user is logged out
    logout(request)
    # Redirect to a success page.
    return redirect('show_2048')








