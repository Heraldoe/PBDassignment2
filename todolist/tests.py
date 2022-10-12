from urllib import response
from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.
def test_show_todolist_ajax_ok(self):
    response: HttpResponse = self.client.get("/todolist/ajax")

    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, "todolist_ajax.html")
