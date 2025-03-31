from django.shortcuts import render
from .form import TeachersForm
from django.http import HttpResponseRedirect , HttpResponse

# Create your views here.
def Teacher(request):

    if request.method == 'POST':

        form=TeachersForm(request.POST)
        if form.is_valid():
            # form.cleaned_data()

            return HttpResponseRedirect("/thank-you/")
    else:
        form=TeachersForm()
    context={"form":form}
    return render(request,"teacher/form.html",context)


def thanks(request):

    return HttpResponse("Thank You Form Submitted")