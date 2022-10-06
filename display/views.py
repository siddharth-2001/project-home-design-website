from django.shortcuts import render
from .models import Design, Concept, ConceptCategory
from django.core.paginator import Paginator

def all_designs_view(request,choice):
    designs = Design.objects.filter(design_type = choice)
    paginator = Paginator(designs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'designs' : page_obj,
        'type'    : choice.capitalize()
    }
    return render(request, 'designs.html', context)

def detail_design_view(request, id):
    design = Design.objects.get(id = id)
    images = design.design_image.all()
    context = {
        'design' : design,
        'images' : images
    }
    return render(request, 'design-detail.html', context)

def all_concept_ctgry_view(request):
    concept_ctgry = ConceptCategory.objects.all()
    paginator  = Paginator(concept_ctgry, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'concept_ctgry' : page_obj,
    }

    return render(request, 'concepts.html', context)

def all_concepts_view(request, id):
    concepts = Concept.objects.filter(concept_type = id)
    category = ConceptCategory.objects.get(id = id)
    context = {
        'concepts' : concepts,
        'category' : category,
    }
    return render(request, 'all-concepts.html', context)

def concept_detail_view(request, id):
    concept = Concept.objects.get(id = id)
    images =  concept.concept_image.all()
    cover  = concept.concept_cover_image.url
    context = {
        'concept' : concept,
        'images'  : images,
        'cover'   : cover,
    }
    return render(request, 'concept-detail.html', context)