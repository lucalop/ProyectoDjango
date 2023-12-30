from django.shortcuts import render, redirect, get_object_or_404
from AppCoder.models import Comments, Trekking 
from AppCoder.forms import TrekkingComment, searchTrekkingForm, UpdateTrekkingImage, searchTrekkingTitleForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class TrekkingList(LoginRequiredMixin, ListView):
    model = Trekking
    template_name = "AppCoder/trekkings.html"

def comment(request):
    if request.method == "POST":
        # Crear course        
        informacion = request.POST
        print(informacion)
        #como invoco el titulo, nombre, apellido?? title=informacion["title"], name=informacion["name"], surname=informacion["surname"],
        trekking = Trekking.objects.get(id= informacion["trekking"])
        save_comment = Comments( usuario = request.user, trekking = trekking, content = informacion["content"] )
        save_comment.save()
        messages.success(request, 'Your comment have been sent!')

        return redirect("/app/trekking/list/")
    
    
    comments = TrekkingComment()

    contexto = {
        "form": comments
    }
    return render(request, "AppCoder/create_trekking.html", contexto)

class CreateTrekking(CreateView):
    model = Trekking
    success_url = "/app/trekking/list/"
    template_name = "AppCoder/create_Trekking.html" #Estro hay que cambiarlo
    fields= "__all__"
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Trekking successfully created!')
        return response

class TrekkingDetail(LoginRequiredMixin, DetailView):
    model = Trekking
    template_name = "AppCoder/trekking_detail.html"

def search_trekking(request):
    city = request.GET["city"]
    print(f"City: {city}")
    trekkings= Trekking.objects.filter(city__icontains=city.strip())
    print(trekkings)

    contexto = {
        "object_list": trekkings,
        "form": searchTrekkingForm(),
        }
    
    return render(request,'AppCoder/trekkings.html',contexto)

def search_trekking_title(request):
    title = request.GET["title"]
    print(f"Title: {title}")
    trekkings= Trekking.objects.filter(title__icontains=title.strip())
    print(trekkings)

    contexto = {
        "object_list": trekkings,
        "form": searchTrekkingTitleForm(),
        }
    
    return render(request,'AppCoder/trekkings.html',contexto)

class AboutMe(TemplateView):
    template_name = "AppCoder/about_me.html"




class AboutMe(TemplateView):
    template_name = "AppCoder/about_me.html"



def edit_trekking_image(request, trekking_id):

    trekking = get_object_or_404(Trekking, id=trekking_id)

    if request.method =="POST":
        form=UpdateTrekkingImage(request.POST, request.FILES, instance=trekking)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Trekking image updated!')
            return redirect("TrekkingList")
        else:
            messages.error(request, 'Error updating trekking image. Please correct the errors. ')

    else:
        form = UpdateTrekkingImage(instance=trekking)

    contexto = {
        "form": form,
        "trekking":trekking
    }
    return render(request, "AppCoder/edit_trekking_image.html", contexto)