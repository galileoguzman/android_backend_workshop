from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# paginator django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Movie
from forms import MovieForm
# Create your views here.

@login_required()
def home(request):
	movies_list = Movie.objects.all().order_by('-created_at')
	paginator = Paginator(movies_list, 12)

	page = request.GET.get('page')
	try:
		movies = paginator.page(page)
	except PageNotAnInteger:
		movies = paginator.page(1)
	except EmptyPage:
		movies = paginator.page(paginator.num_pages)

	
	return render(request, 'home.html',{'movies': movies})

@login_required()
def movie_new(request):
	if request.method == "POST":
		form = MovieForm(request.POST, request.FILES)
		if form.is_valid():
			movie = form.save(commit=False)
			#movie.author = request.user
			#movie.published_date = timezone.now()
			movie.save()
			return redirect('home')
	else:
		form = MovieForm()
	return render(request, 'movie_edit.html', {
		'form': form,
	})


@login_required()
def movie_edit(request, id):
	movie = get_object_or_404(Movie, pk=id)

	if request.method == "POST":
		form = MovieForm(request.POST, request.FILES, instance=movie)
		if form.is_valid():
			movie = form.save(commit=True)
			movie.save()
			return redirect('home')
	else:
		form = OpinionForm(instance=movie)

	return render(request, 'movie_edit.html', {
		'form': form,
	})

@login_required()
def movie_delete(request, id=None):
	movie = get_object_or_404(Movie, pk=id)
	movie.delete()

	return redirect('home')