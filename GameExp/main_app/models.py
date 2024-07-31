from django.db import models
from django.utils.text import slugify
from .utils import screenshot_upload_path, cover_image_upload_path, uploads_upload_path

class Genre(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


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
    short_description = models.CharField(max_length=255, blank=True, null=True)
    cover_img = models.ImageField(upload_to=cover_image_upload_path, blank=True, null=True)
    gameplay_video = models.URLField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    
    suggested_donate = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=2.00,
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        default=1.00,
        blank=True,
        null=True
    )
    
    """
    Choise fields
    """
    classification = models.CharField(choices=PROJECT_TYPE_CHOICE, default='Game')
    kind_of_project = models.CharField(choices=PROJECT_KIND, default='Downloadable')

    """
    Boolean field for state
    """
    is_free = models.BooleanField(default=False, blank=True, null=True)
    is_community_disabled = models.BooleanField(verbose_name='community', default=False, blank=True, null=True)
    have_commentary = models.BooleanField(verbose_name='commentary', default=True, blank=True, null=True)
    have_discussion_board = models.BooleanField(verbose_name='discussion board', default=False, blank=True, null=True)
    
    """
    Project restriction
    """
    is_draft = models.BooleanField(verbose_name='draft', default=False, blank=True, null=True)
    is_restricted = models.BooleanField(verbose_name='restricted', default=False, blank=True, null=True)
    is_public = models.BooleanField(verbose_name='public restriction', default=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class ProjectScreenshot(models.Model):
    project = models.ForeignKey(Project, related_name='project_screens', on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to=screenshot_upload_path)

    class Meta:
        verbose_name = 'Screenshot'
        verbose_name_plural = 'Screenshots'


class ProjectUploadedFile(models.Model):
    project = models.ForeignKey(Project, related_name='project_uploads', on_delete=models.CASCADE)
    file = models.FileField(upload_to=uploads_upload_path)

    class Meta:
        verbose_name = 'Upload file'
        verbose_name_plural = 'Upload files'
