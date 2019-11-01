from django.test import TestCase

from wagtail_transfer.operations import ImportPlanner
from tests.models import SimplePage


class TestImport(TestCase):
    fixtures = ['test.json']

    def test_import_pages(self):
        data = """[
            {
                "uid": "22222222-2222-2222-2222-222222222222",
                "model": "tests.simplepage",
                "pk": 12,
                "parent_id": 1,
                "fields": {
                    "title": "Home",
                    "show_in_menus": false,
                    "live": true,
                    "slug": "home",
                    "intro": "This is the updated homepage"
                }
            },
            {
                "uid": "55555555-5555-5555-5555-555555555555",
                "model": "tests.simplepage",
                "pk": 15,
                "parent_id": 12,
                "fields": {
                    "title": "Imported child page",
                    "show_in_menus": false,
                    "live": true,
                    "slug": "imported-child-page",
                    "intro": "This page is imported from the source site"
                }
            }
        ]"""

        importer = ImportPlanner(12, None)
        importer.add_json_objects_for_import(data)
        importer.run()

        updated_page = SimplePage.objects.get(url_path='/home/')
        self.assertEqual(updated_page.intro, "This is the updated homepage")

        created_page = SimplePage.objects.get(url_path='/home/imported-child-page/')
        self.assertEqual(created_page.intro, "This page is imported from the source site")
