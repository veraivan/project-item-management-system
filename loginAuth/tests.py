
# Create your tests here.
from django.test import TestCase

from django.urls.base import reverse,resolve

from . import views


""" Si el HTTP status de la pagina es 200 es porque todo va bien
codigo 302  hace una redireccion temporal de una pagina a otra"""
class TestModeloAutenticacion(TestCase):
    #setUp para definir un escenario configurado para usar en los otros test
    def setUp(self):
        self.dato = {
            'username': 'ruizn291',
            'password': 'nelson',
            'email': 'ruizn291@gmail.com',
            'first_name': 'Nelson',
            'last_name': 'Ruiz'
        }

        self.register_url=reverse(views.index)
        self.register_dashboard=reverse(views.dashboard)
        self.register_logout=reverse(views.logout)
        return super().setUp()

    def test_index(self):
        #ver pagina correctamente,deteccion de respuesta de modo que pudimos abrir la pagina correctamente
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200) #cpnfirma si cargo correctamente la pagina
        self.assertTemplateUsed(response,'index.html') #confirmacion de la plantilla usada
        #si queremos probar un caso que no funcione podemos cambiar TemplateUsed por otro

    def test_dashboard(self):
        #prueba de registro de usuario

        response=self.client.post(self.register_dashboard,self.dato)#envia al cliente de prueba la vista con la direccion
        self.assertEqual(response.status_code, 302)
       # m=resolve(self.register_dashboard)
        #print (self.dato)
        #self.assertEqual(self.dato['username'],'ruizn291')
        #caso de error si se cambia el usuario


    def test_logout(self):
        response = self.client.get(self.register_dashboard)  # envia al cliente de prueva la vista con la direccion
        self.assertEqual(response.status_code, 302)