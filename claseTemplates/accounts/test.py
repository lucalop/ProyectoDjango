from django.test import TestCase
from models import Avatar
from django.contrib.auth.models import User

class AvatarTestCase(TestCase):

    def setUp(self):
        user = User.object.create(
            username="pepe",
            password="pepe"
        )

        Avatar.objects.create(
            user=user,
            imagen = "/media/avatares/asdasd.png"
        )
    
    def test_creacion_avatares (self):
        avatar=Avatar.objects.get(imagen="asdasd.png")
        self.assertEqual(avatar.user.username,"pepe")