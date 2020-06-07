from django.shortcuts import render ,get_object_or_404 , redirect

from .models import post
from .forms import postform



# Create your views here.

def all_posts(request):
    all_posts = post.objects.filter(active=True)

    context = {
        'all_posts' : all_posts
    }
    return render(request, 'all_posts.html',context)


def get_post(request,id):
    # current_post = post.objects.get(id = id)
    current_post = get_object_or_404(post,id=id)

    context = {
        'post': current_post 
    }
    return render( request,'detail.html',context)


def create_post(request):
    if request.method =='POST':
        form = postform(request.POST)
        if form.is_valid():
            new_form =form.save(commit= False)
            new_form.user=request.user
            new_form.save()
            return redirect('/')


    else :
        form = postform()


    context = {
        'form': form
    }

    return render(request,'create.html',context) 









def edit_post(request,id):
    cur_post = get_object_or_404(post,id=id)
    if request.method =='POST':
        form = postform(request.POST, instance=cur_post )
        if form.is_valid():
            new_form =form.save(commit= False)
            new_form.user=request.user
            new_form.save()
            return redirect('/')

    else :
        form = postform(instance=cur_post)


    context = {
        'form': form
    }

    return render(request,'edit_post.html',context) 

def admin(request):
    return redirect('admin')




def delete_post(request,id):
    cr_post = get_object_or_404(post,id=id)
    cr_post.delete()
    return redirect("/")
