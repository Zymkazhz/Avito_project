from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm, GalleryForm, ScootersForm, MotorcyclesForm
from django.utils import timezone
from .models import Gallery, Car, Scooters, Motorcycles
from django.views.generic import ListView
from django.db.models import Q
from mycart.forms import CartAddProductForm


def home(request):
    car_objects = Car.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    scooters_objects = Scooters.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    motorcycles_objects = Motorcycles.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    ads = []
    ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                 'published_date': model.published_date, 'pk': model.pk,
                 'image_one': model.gallery.image_one} for model in car_objects])
    ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                 'published_date': model.published_date, 'pk': model.pk,
                 'image_one': model.gallery.image_one} for model in scooters_objects])
    ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                 'published_date': model.published_date, 'pk': model.pk,
                 'image_one': model.gallery.image_one} for model in motorcycles_objects])
    ads.sort(key=lambda dictionary: dictionary['published_date'], reverse=True)
    context = {
        'ads': ads,
        'car_objects': car_objects,
    }
    return render(request, 'appsite/home.html', context)


def ad_detail_car(request, pk):
    cars = get_object_or_404(Car, pk=pk)
    cart_product_form = CartAddProductForm
    context = {
        'cart_product_form': cart_product_form,
        'car': cars,
    }
    return render(request, 'appsite/ad_detail_car.html', context)


def ad_detail_scooters(request, pk):
    scooters = get_object_or_404(Scooters, pk=pk)
    cart_product_form = CartAddProductForm
    context = {
        'cart_product_form': cart_product_form,
        'scooters': scooters,
    }
    return render(request, 'appsite/ad_detail_scooters.html', context)


def ad_detail_motorcycles(request, pk):
    motorcycles = get_object_or_404(Motorcycles, pk=pk)
    cart_product_form = CartAddProductForm
    context = {
        'cart_product_form': cart_product_form,
        'motorcycles': motorcycles,
    }
    return render(request, 'appsite/ad_detail_motorcycles.html', context)


def get_class(class_name):
    return eval(class_name)


def item_add(request):
    if request.method == 'POST':
        category_form = request.POST.get('category_form')
        category_image_form = request.POST.get('category_image_form')
        category = request.POST.get('category')
        category_image = request.POST.get('category_image')
        form = get_class(category_form)(request.POST)
        form_image = get_class(category_image_form)(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid() and form_image.is_valid():
            #item = form.save(commit=False)
            #item.author = request.user
            #item.published_date = timezone.now()
            #item.save()
            item_image = form_image.save(commit=False)
            item_image.user = request.user
            #item_image.gallery = get_class(category).objects.get(pk=item.id)
            item_image.save()
            item = form.save(commit=False)
            item.author = request.user
            item.gallery = get_class(category_image).objects.get(pk=item_image.id)
            item.published_date = timezone.now()
            item.save()
            #for photo in files:
            #    file_instance = get_class(category_image)(image=photo,
            #                                              #product=get_class(category).objects.get(pk=item.id),
            #                                              user=request.user)
            #    file_instance.save()
            return redirect('itemadd')
        else:
            error = "Error"
    error = ''
    form_car = CarForm
    form_image_car = GalleryForm
    form_scooters = ScootersForm
    form_image_scooters = GalleryForm
    form_motorcycles = MotorcyclesForm
    form_image_motorcycles = GalleryForm

    data = {
        'form_car': form_car,
        'error': error,
        'form_image_car': form_image_car,
        'form_scooters': form_scooters,
        'form_image_scooters': form_image_scooters,
        'form_motorcycles': form_motorcycles,
        'form_image_motorcycles': form_image_motorcycles,
    }
    return render(request, 'appsite/itemadd.html', data)


class Search(ListView):
    paginate_by = 10
    template_name = 'appsite/index.html'

    def get_queryset(self):
        ads = []
        q = self.request.GET.get('q')
        query_search_list = q.split(' ')
        for query_search in query_search_list:
            if query_search.isdigit():
                car_objects = Car.objects.filter(year=query_search)
                scooters_objects = Scooters.objects.filter(year=query_search)
                motorcycles_objects = Motorcycles.objects.filter(year=query_search)
                ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                             'published_date': model.published_date, 'pk': model.pk, 'year': model.year,
                             'image_one': model.gallery.image_one, 'mileage': model.mileage,
                             'description': model.description} for model in car_objects])
                ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                             'published_date': model.published_date, 'pk': model.pk, 'year': model.year,
                             'image_one': model.gallery.image_one, 'mileage': model.mileage,
                             'description': model.description} for model in scooters_objects])
                ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                             'published_date': model.published_date, 'pk': model.pk, 'year': model.year,
                             'image_one': model.gallery.image_one, 'mileage': model.mileage,
                             'description': model.description} for model in motorcycles_objects])
            else:
                car_objects = Car.objects.filter(
                    Q(brand__icontains=query_search) | Q(description__icontains=query_search)
                )
                scooters_objects = Scooters.objects.filter(
                    Q(brand__icontains=query_search) | Q(description__icontains=query_search)
                )
                motorcycles_objects = Motorcycles.objects.filter(
                    Q(brand__icontains=query_search) | Q(description__icontains=query_search)
                )
                ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                             'published_date': model.published_date, 'pk': model.pk, 'year': model.year,
                             'image_one': model.gallery.image_one, 'mileage': model.mileage,
                             'description': model.description} for model in car_objects])
                ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                             'published_date': model.published_date, 'pk': model.pk, 'year': model.year,
                             'image_one': model.gallery.image_one, 'mileage': model.mileage,
                             'description': model.description} for model in scooters_objects])
                ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                             'published_date': model.published_date, 'pk': model.pk, 'year': model.year,
                             'image_one': model.gallery.image_one, 'mileage': model.mileage,
                             'description': model.description} for model in motorcycles_objects])
        return ads

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

