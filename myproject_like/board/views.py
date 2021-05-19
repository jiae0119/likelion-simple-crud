from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog

# Create your views here.
def create(request):
	if request.method == 'POST':
		blog_object = Blog()
		blog_object.title = request.POST['title']
		blog_object.body = request.POST['body']
		blog_object.save()
		return redirect('/read/' + str(blog_object.id))
	return render(request, 'create.html')

def read(request, id):
	blog_object = get_object_or_404(Blog, pk = id)
	return render(request, 'read.html', {'data': blog_object})