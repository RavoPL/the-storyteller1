from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Post
from django.views import generic, View
from .forms import CommentForm, SubmissionForm

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class SubmissionView(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objets.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "base.html",
            {
                "submission_form": SubmissionForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
            
        submission_form = SubmissionForm(data=request.POST)
        if submission_form.is_valid():
            submission_form.instance.name = request.user.username
            submission = submission_form.save(commit=False)
            submission.post = post
            submission.save()
        else:
            submission_form = SubmissionForm()
            
        return render(
            request,
            "base.html",
            {
                "submission_form": submission_form,
            },
        )

        return HttpResponseRedirect(reverse('base.html', args=[slug]))

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
                "submission_form": SubmissionForm(),
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
        
        submission_form = SubmissionForm(data=request.POST)
        if submission_form.is_valid():
            submission_form.instance.name = request.user.username
            submission = submission_form.save(commit=False)
            submission.post = post
            submission.save()
        else:
            submission_form = SubmissionForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True if comment_form.is_valid() else False,
                "comment_form": comment_form,
                "submission_form": submission_form,
                "liked": liked
            },
        )

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def aboutpage(request):
    return render(request, "aboutpage.html", {'title': 'About Page'})