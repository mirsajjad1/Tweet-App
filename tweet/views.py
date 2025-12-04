from django.shortcuts import render
from .forms import post_form, UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'app/post_list.html', {'posts' : posts})


@login_required
def post_create(request):
    if request.method == 'POST':
     
     form = post_form(request.POST, request.FILES)
     if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('post_list')
    else:
       form = post_form()
    return render(request, 'app/post_form.html', { 'form' : form } )

@login_required
def post_edit(request, post_id):
   post = get_object_or_404(Post, pk=post_id, user=request.user)
   if request.method == 'POST':
    form = post_form(request.POST, request.FILES, instance=post)
    if form.is_valid():
       post = form.save(commit=False)
       post.user = request.user
       post.save()
       return redirect('post_list')
    
   else:
      form = post_form(instance=post)


   return render(request, 'app/post_form.html', { 'form' : form } )


@login_required
def post_delete(request, post_id):
   post = get_object_or_404(Post, pk=post_id, user=request.user )
   if request.method == 'POST':
      post.delete()
      return redirect('post_list')
   return render(request, 'app/post_confirm_delete.html', { 'post' : post } )


def register(request):
   if request.method == 'POST':
     form = UserRegistrationForm(request.POST)
     if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(request, user)
        return redirect('post_list')
      
   else:
      form = UserRegistrationForm()


   return render(request, 'registration/register.html', { 'form' : form } )