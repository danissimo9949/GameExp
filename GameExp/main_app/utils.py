from django.utils.text import slugify

def screenshot_upload_path(instance, filename):
    project_slug = slugify(instance.project.title)
    return f'projects/{project_slug}/screenshots/{filename}'
