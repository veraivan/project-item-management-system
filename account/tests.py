from django.test import TestCase, SimpleTestCase,Client
from django.urls import reverse,resolve
# Create your tests here.
from .models import MyUserManager,ProjectUser
from . import views, urls
from account.views import Registro


""" si el http status de la pagina es 200 es porque todo va bien
codigo 302  hace una redireccion temporal de una pagina a otra"""
class testmodeloautenticacion(TestCase):
    #setup para definir un escenario configurado para usar en los otros test
    def setUp(self):


        self.register_url=reverse(views.loggin)
        self.register_dashboard=reverse(views.dashboard)
        self.register_logout=reverse(views.logout)



        return super().setUp()




    def test_index(self):
        #ver pagina correctamente,deteccion de respuesta de modo que pudimos abrir la pagina correctamente
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200) #cpnfirma si cargo correctamente la pagina
        self.assertTemplateUsed(response,'base.html') #confirmacion de la plantilla usada
        #si queremos probar un caso que no funcione podemos cambiar templateused por otro

    def test_dashboard(self):
        #prueba de registro de usuario

        response=self.client.post(self.register_dashboard)#envia al cliente de prueba la vista con la direccion
        self.assertEqual(response.status_code, 302)
        print("El test de retorno de dashboard corrio correctamente")

       # m=resolve(self.register_dashboard)
        #print (self.dato)
        #self.assertequal(self.dato['username'],'ruizn291')
        #caso de error si se cambia el usuario
    def test_logout(self):
        response = self.client.get(self.register_logout)  #hace la solicitud get de la pagina para probar la ruta de codigo
        self.assertEqual(response.status_code, 302)

