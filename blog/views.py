from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post, Main, Child
from .forms import ContactForm, LoginForm, UserRegistrationForm, UserEditForm, ChildEditForm, PostForm
from django.core.mail import send_mail


class MainView(ListView):
    queryset = Main.objects.all()
    # queryset = Main.published.all()
    context_object_name = 'mains'
    template_name = "blog/post/main.html"


class PostView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    # paginate_by = 3
    template_name = "blog/post/list.html"


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request, 'blog/post/detail.html', {"post": post})


def contact(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(subject=cd['topic'], message=cd['message'], from_email=[cd['email']], recipient_list=['admin@wp.pl'])
            sent = True
    else:
        form = ContactForm()
    return render(request, "blog/post/contact.html", {"contact_form": form,
                                                      "sent": sent})


def register(request):
    if request.method == "POST":
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            new_user.save()
            Child.objects.create(id_name=new_user,
                                 # first_name=new_user.first_name,
                                 # last_name=reg_form.cleaned_data['last_name'],
                                 email=reg_form.cleaned_data['email'])
            return render(request, "registration/register_done.html", {"new_user": new_user})
    else:
        reg_form = UserRegistrationForm
    return render(request, "registration/register.html", {"reg_form": reg_form})


@login_required
def edit(request):
    if request.method == "POST":
        userform = UserEditForm(instance=request.user, data=request.POST)
        childform = ChildEditForm(instance=request.user.child, data=request.POST, files=request.FILES)
        if userform.is_valid() and childform.is_valid():
            userform.save()
            childform.save()
            email = userform.cleaned_data['email']
            first_name = userform.cleaned_data['first_name']
            last_name = userform.cleaned_data['last_name']
            Child.objects.filter(id_name=request.user.id).update(email=email,
                                                                 first_name=first_name,
                                                                 last_name=last_name)

    else:
        userform = UserEditForm(instance=request.user)
        childform = ChildEditForm(instance=request.user.child)

    return render(request, "registration/edit.html", {"userform": userform, "childform": childform})


@login_required
def add_post(request):
    if request.method == "POST":

        post_form = PostForm(request.POST)
        post_form.author = request.user
        if post_form.is_valid():
            Post.objects.create(title=post_form.cleaned_data['title'],
                                body=post_form.cleaned_data['body'],
                                comments=post_form.cleaned_data['comments'],
                                author=request.user)

    else:
        post_form = PostForm()

    return render(request, "blog/post/add_post.html", {"post_form": post_form})