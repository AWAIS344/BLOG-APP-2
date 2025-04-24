from django.shortcuts import render
from .form import TeachersForm
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponse , response
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Teacher
from .form import TeachersForm

# Create your views here.
def Teacher_view(request):
    thanks=reverse("thanks")
    if request.method == 'POST':

        form=TeachersForm(request.POST,request.FILES)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # phone_number=form.cleaned_data['phone_number']
            # bio=form.cleaned_data['Bio']
            # teacher=Teacher.objects.create(name=name,email=email,phone_number=phone_number,bio=bio)
            form.save()

            return HttpResponseRedirect(thanks)
    else:
        form=TeachersForm()
    context={"form":form}
    return render(request,"teacher/form.html",context)




def all_data(request):
    teacher=Teacher.objects.all()

    if request.method == "POST":

        return HttpResponseRedirect("update")
    context={"teacher":teacher}

    return render(request,"teacher/all_data.html",context)


def update(request,id):
    teacher=Teacher.objects.get(id=id)

    if request.method == "POST":
        form = TeachersForm(request.POST , instance=teacher)  # Bind form data
        if form.is_valid():
           
            form.save() # Save changes to DB
                
            return redirect("all_data")
    else:
        form=TeachersForm(instance=teacher)
    context={"teacher":teacher,"form":form }
    return render(request,"teacher/update.html",context)


def delete(request, id):
    if request.method == "POST": 
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
    return redirect("all_data") 


def thanks(request):

    return HttpResponse("Thank You Form Submitted")