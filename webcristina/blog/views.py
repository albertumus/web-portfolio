from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Entrada_de_blog, Entrada_de_blog_category

# Create your views here.

def blog(request):
    query = request.GET.get("q")
    entradas_de_blog = Entrada_de_blog.objects.all()

    if query:
        entradas_de_blog_filtradas = entradas_de_blog.filter(title__icontains=query)
        print(entradas_de_blog_filtradas)
        return render(request, 'blog/blog.html', {"entradas_de_blog_filtradas": entradas_de_blog_filtradas})
    else:
        print(entradas_de_blog)
        return render(request, 'blog/blog.html', {"entradas_de_blog": entradas_de_blog})

    


def entrada_de_blog(request, entrada_de_blog_id, entrada_de_blog_slug):
    entrada_de_blog = get_object_or_404(Entrada_de_blog, id=entrada_de_blog_id)
    return render(request, "blog/entrada.html", {"entrada_de_blog":entrada_de_blog})

def entrada_de_blog_category(request, category_id):
    category = get_object_or_404(Entrada_de_blog_category, id=category_id)

    return render(request, "blog/category.html", {"category": category})