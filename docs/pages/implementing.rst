########################################################
Implementing a Photologue gallery in your Django project
########################################################

Model
=====
Adding a foreign key to Photologue's `Gallery` model object is all it takes to
start connecting your galleries to other objects in your project. So in your
`models.py` for your app `cats_app`, you might have a model as follows.::

    from django.db import models
    from photologue.models import Gallery

    class Cat(models.Model):
        rainbows = models.PositiveIntegerField()
        nyan = models.BooleanField()
        cat_gallery = models.ForeignKey(Gallery)

View
====
Using a class-based view which targets the `Cat` model, a selection of
the methods starting with "get_" are called on all the `Photo` objects in the
`Gallery` for that instance of the `Cat` model.::

    from django.views.generic.detail import DetailView

    class CatGalleryView(DetailView):

    model = Cat
    context_object_name = 'cat'
    template_name = 'cats_app/cat.html'

    def image_data(self,image):
        gets = [ 
            'absolute_url',
            'display_size',
            'display_url',
            'thumbnail_size',
            'thumbnail_url',
        ]
        return dict(zip(gets,[getattr(image,'get_'+attr)() for attr in gets]))

    def get_context_data(self, **kwargs): 
        context = super(ShowView, self).get_context_data(**kwargs)
        context['image_dicts'] = {
            image.title:self.image_data(image)
            for image in self.object.cat_gallery.photos.all()
        }
        return context

This will give you a simple dicitionary in your template `cats_app/cat.html`
with all the information you need to produce a slideshow or another presentation
of your cat gallery.
