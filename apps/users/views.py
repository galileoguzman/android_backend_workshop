from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# IMPORTS FOR DJANGO AUTH PATTERN
from django.contrib.auth import authenticate, login, logout
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required

# Create your views here.
# --------------------------------------------------------------------
# LOGIN PATTERN MANAGEMENT
# --------------------------------------------------------------------
def user_login(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:

				try:
					remember = request.POST['remember_me']
					if remember:
						settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
				except MultiValueDictKeyError:
					is_private = False
					settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True

				login(request, user)
				return redirect('/')
			else:
				return redirect('/login/?next=%s' % request.path)
		else:
			return render(request, 'login.html', {'errors': True})
	else:
		return render(request, 'login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


def handler404(request):
    return redirect('/')

def handler500(request):
    return redirect('/')