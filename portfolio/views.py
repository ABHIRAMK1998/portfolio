from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio,Project
from .forms import PortfolioForm,ProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def view_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    if created:
        portfolio.title = ""
        portfolio.description = ""
        portfolio.project_showcase = ""
        portfolio.education = ""
        portfolio.certifications = ""
        portfolio.work_experience = ""
        portfolio.save()

    return render(request, 'view_portfolio.html', {'portfolio': portfolio})


@login_required
def create_portfolio(request):
    existing_portfolio = Portfolio.objects.filter(user=request.user).first()
    if existing_portfolio:
        return redirect('edit_portfolio')

    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('view_portfolio')
    else:
        form = PortfolioForm()
    return render(request, 'create_portfolio.html', {'form': form})


@login_required
def edit_portfolio(request):
    portfolio = get_object_or_404(Portfolio, user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('view_portfolio')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'edit_portfolio.html', {'form': form})
@login_required
def create_project(request):
    existing_project = Project.objects.filter(user=request.user).first()
    if existing_project:
        return redirect('edit_project')

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('view_project')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})
@login_required
def view_project(request):
    project, created = Project.objects.get_or_create(user=request.user)
    if created:
        project.title = ""
        project.description = ""
        project.image = ""
        project.github_link = ""
        project.demo_link = ""
        project.save()

    return render(request, 'view_project.html', {'project': project})

@login_required
def edit_project(request):
    project = get_object_or_404(Project, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('view_project')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form})

def ProjectHome(request):
    return render(request,'project_index.html')
