########################################################
Implementing a Photologue gallery in your Django project
########################################################

Model
=====
Adding a foreign key to Photologue's Gallery model object is all it takes to get
::

  from django.db import models
  from photologue.models import Gallery

  class BlogPost(models.Model):
      title = models.CharField(max_length=1024)   
      date = models.DateField(auto_add_now=True)
      gallery = models.ForeignKey(Gallery)
      body = models.TextField()

Using a class-based view, the Post object targeted has its context dressed up
with a dict containing all the information required to present ::

  class PostView(DetailView):

      model = BlogPost
      context_object_name = 'post' 
      template_name = 'single-post.html'

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
              for image in self.object.gallery.photos.all()
          }
          return context

This will give you a simple dicitionary in your template `single-post.html` with
all the information you need to produce a slideshow or another presentation of
your Photologue gallery.
