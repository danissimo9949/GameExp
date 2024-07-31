from django.db import models
from django.utils.text import slugify
from .utils import screenshot_upload_path

class Project(models.Model):

    PROJECT_TYPE_CHOICE = [
        ('Game','Games'),
        ('Mods','Game mods'),
    ]

    PROJECT_KIND = [
        ('Downloadable', 'Downloadable'),
        ('HTML', 'HTML project'),
        ('WebGL', 'Unity WebGL project'),
    ]

    PROJECT_STATUS = [
        ('Released', 'Released project'),
        ('In progress', 'In development (early access)'),
        ('Paused', 'Paused'),
        ('Canceled', 'Canceled project'),
        ('Prototype', 'Prototype project'),
    ]

    """
    General fields for project model
    """
    title = models.CharField(max_length=255, blank=False)
    project_url = models.URLField(max_length=255)
    short_description = models.CharField(max_length=255)
    cover_img = models.ImageField(upload_to=f'projects/{slugify(title)}/cover-image/')
    gameplay_video = models.URLField(max_length=255)

    suggested_donate = models.DecimalField(verbose_name='donate', max_digits=6, decimal_places=2, default=2.00)
    price = models.DecimalField(verbose_name='price', max_digits=6, decimal_places=2, default=1.00)
    
    """
    Choise fields
    """
    classification = models.CharField(choices=PROJECT_TYPE_CHOICE, default='Game')
    kind_of_project = models.CharField(choices=PROJECT_KIND, default='Downloadable')

    """
    Boolean field for state
    """
    is_free_or_donate = models.BooleanField(verbose_name='Free or donate project', default=True)
    is_paid = models.BooleanField(default=False, blank=True)
    is_free = models.BooleanField(default=False, blank=True)




class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, related_name='project_screens', on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to=screenshot_upload_path)

