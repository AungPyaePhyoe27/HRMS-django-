from django.shortcuts import render, redirect
from .models import AttendanceModel
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def search_by(request):
    search = request.GET.get('search')
    if search:    
        attendances = AttendanceModel.objects.filter(
            Q(name__icontains=search) | 
            Q(sequence__icontains=search) |
            Q(signin_time__icontains=search) |
            Q(signout_time__icontains=search) |
            Q(note__icontains=search) |
            Q(status__icontains=search) 
        )
    else:      
        attendances = AttendanceModel.objects.all()
    return render(request, 'attendance_list.html', {'all_attendances': attendances})

def order_by(request):
    order = request.GET.get('order')
    attendances = AttendanceModel.objects.all().order_by("-"+ order).reverse()
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(attendances, 2) #Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'attendance_list.html', {'page_obj': page_obj, 'order_selected': order_selected})
    #return render(request, 'attendance_list.html', {'all_attendances': attendances, 'order_selected': order_selected})

@permission_required('hr_attendances.view_attendancemodel', login_url='login')
def attendance(request, attendance_id):
    if request.method == "GET": 
        attendance = AttendanceModel.objects.get(id=attendance_id)  
        return render(request,'attendance_detail.html', {'attendance': attendance})

@login_required(login_url='login')
def all_attendances(request):
    if request.method == "GET": 
        all_attendances = AttendanceModel.objects.all()
        paginator = Paginator(all_attendances, 2) # Show 2 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'attendance_list.html', {'page_obj': page_obj})

@permission_required('hr_attendances.add_attendancemodel', login_url='login')  
def add_attendance(request):  
    if request.method == "GET": 
        form = AttendanceForm()
        return render(request,'attendance_create.html',{'form':form}) 
    if request.method == "POST" and request.FILES['attachment']:  
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return redirect('/hr_attendances/show_attendance/')  

@permission_required('hr_attendances.change_attendancemodel', login_url='login')  
def update_attendance(request, attendance_id):  
    print('update_attendance call')
    attendance = AttendanceModel.objects.get(id=attendance_id)  
    if request.method == "GET":
        print('update_attendance GET call +++++++++++++++++')
        form = AttendanceForm(instance=attendance)
        return render(request, 'attendance_update.html', {'form': form, 'uploaded_image': attendance.attachment })
    elif request.method == "POST": 
        print('update_attendance POST call +++++++++++++++++')
        form = AttendanceForm(request.POST, request.FILES, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('/hr_attendances/detail/' + str(attendance_id) + '/')

@permission_required('hr_attendances.delete_attendancemodel', login_url='login')  
def delete_attendance(request, attendance_id):
    if request.method == "GET":
    #     attendance = attendanceModel.objects.get(id=attendance_id)  
    #     return render(request, 'attendance_delete.html', {'attendance': attendance})
    # if request.method == "POST": 
        attendance = AttendanceModel.objects.filter(id=attendance_id)
        attendance.delete()
        return redirect('/hr_attendances/show_attendance/')