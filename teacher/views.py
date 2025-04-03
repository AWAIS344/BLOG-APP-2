from django.shortcuts import render
from .form import TeachersForm
from django.http import HttpResponseRedirect , HttpResponse
from .models import Teacher
from .form import TeachersForm

# Create your views here.
def Teacher_view(request):

    if request.method == 'POST':

        form=TeachersForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            bio=form.cleaned_data['Bio']
            teacher=Teacher.objects.create(name=name,email=email,phone_number=phone_number,bio=bio)

            return HttpResponseRedirect("/thank-you/")
    else:
        form=TeachersForm()
    context={"form":form}
    return render(request,"teacher/form.html",context)




def all_data(request):
    teacher=Teacher.objects.all()
    context={"teacher":teacher}

    return render(request,"teacher/all_data.html",context)


def thanks(request):

    return HttpResponse("Thank You Form Submitted")