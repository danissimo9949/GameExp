from django.test import TestCase
from django.utils.text import slugify
from .models import Project, ProjectScreenshot
from .utils import screenshot_upload_path

class ProjectTests(TestCase):
    
    def test_upload_screenshot_path(self):
        project = Project.objects.create(
            title='My Test Project',
            project_url='http://example.com',
            short_description='Short description',
            cover_img='path/to/cover-image.jpg',
            gameplay_video='http://example.com/video.mp4',
            suggested_donate=2.00,
            price=1.00,
            classification='Game',
            kind_of_project='Downloadable',
            is_free_or_donate=True,
            is_paid=False,
            is_free=False,
        )

        screenshot = ProjectScreenshot.objects.create(
            project=project,
            screenshot='path/to/screenshot.jpg',
        )

        self.assertEqual(screenshot.project, project)
        
