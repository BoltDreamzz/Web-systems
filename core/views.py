from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Project, Testimonial, Technology, Comment
from .forms import CommentForm


def home(request):
    projects = Project.objects.all()
    # messages.success(request, "Waddup fam!")
    testimonials = Testimonial.objects.all()
    project_count = projects.count()

    technologies = Technology.objects.all()[:3]

    context = {
        "projects": projects,
        "technologies": technologies,
        "project_count": project_count,
        "testimonials": testimonials,
    }
    return render(request, "core/home.html", context)


def all_projects(request):
    projects = Project.objects.all()
    project_count = projects.count()

    context = {
        "projects": projects,
        "project_count": project_count,
    }
    return render(request, "core/projects.html", context)


@login_required
def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    comments = project.comments.all()
    comment_count = comments.count()

    project_count = Project.objects.all().count()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()

            messages.success(request, f"Your comment was posted.")

            return redirect("core:project_detail", project_id=project.id)

    context = {
        "project": project,
        "project_count": project_count,
        "comments": comments,
        "comment_count": comment_count,
    }
    return render(request, "core/project_detail.html", context)



@login_required
def edit_comment(request, pk):
    comment = Comment.objects.filter(pk=pk)
    form = CommentForm(instance=comment)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }
    return render(request, "core/edit_comment.html", context)



@login_required
def delete_comment(request, pk):
    comment = Comment.objects.filter(pk=pk)

    comment.delete()
    return redirect(request, "core:project_detail", pk=comment.pk)


# @login_required
# def delete_comment(request, comment_id):
#     comment = get_object_or_404(Comment, pk=comment_id)
#     project_id = comment.project.id
#     comment.delete()
#     return redirect('app:project_detail', project_id=project_id)


# def splash(request):
#     return render(request, "core/splash.html")





