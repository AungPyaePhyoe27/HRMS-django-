from django.shortcuts import render, redirect
from .models import JobModel
from .forms import JobForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def search_by(request):
    search = request.GET.get('search')
    if search:    
        jobs = JobModel.objects.filter(
            Q(name__icontains=search) | 
            Q(sequence__icontains=search) |
            Q(open_date__icontains=search) |
            Q(expected_salary__icontains=search) |
            Q(note__icontains=search) |
            Q(status__icontains=search) |
            Q(create_date__icontains=search)
        )
    else:      
        jobs = JobModel.objects.all()
    return render(request, 'job_list.html', {'all_jobs': jobs})

def order_by(request):
    order = request.GET.get('order')
    jobs = JobModel.objects.all().order_by("-"+ order).reverse()
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(jobs, 2) #Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job_list.html', {'page_obj': page_obj, 'order_selected': order_selected})
    #return render(request, 'job_list.html', {'all_jobs': jobs, 'order_selected': order_selected})

@permission_required('hr_jobs.view_jobmodel', login_url='login')
def job(request, job_id):
    if request.method == "GET": 
        job = JobModel.objects.get(id=job_id)  
        return render(request,'job_detail.html', {'job': job})

@login_required(login_url='login')
def all_jobs(request):
    if request.method == "GET": 
        all_jobs = JobModel.objects.all()
        paginator = Paginator(all_jobs, 2) # Show 2 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'job_list.html', {'page_obj': page_obj})

@permission_required('hr_jobs.add_jobmodel', login_url='login')  
def add_job(request):  
    if request.method == "GET": 
        form = JobForm()
        return render(request,'job_create.html',{'form':form}) 
    if request.method == "POST" and request.FILES['attachment']:  
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return redirect('/hr_jobs/show_job/')  

@permission_required('hr_jobs.change_jobmodel', login_url='login')  
def update_job(request, job_id):
    print('update_job call')
    print('job_id ', job_id)
    job = JobModel.objects.get(id=job_id)
    if request.method == "GET":
        print('update_job GET call')
        form = JobForm(instance=job)
        return render(request, 'job_update.html', {'form': form, 'uploaded_image': job.attachment})
    if request.method == "POST":
        print('update_job POST call')
        print('data => ', request.POST)
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            print('is valid')
            form.save()
            return redirect('/hr_jobs/detail/' + str(job_id) + '/')

@permission_required('hr_jobs.delete_jobmodel', login_url='login')  
def delete_job(request, job_id):
    if request.method == "GET":
    #     job = JobModel.objects.get(id=job_id)  
    #     return render(request, 'job_delete.html', {'job': job})
    # if request.method == "POST": 
        job = JobModel.objects.filter(id=job_id)
        job.delete()
        return redirect('/hr_jobs/show_job/')