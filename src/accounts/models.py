from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q

from marque.models import Marque

from sayaradz import settings


class UserManager(BaseUserManager):

    def create_user(self, email, **kwargs):
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            email = self.normalize_email(email)
        )
        if 'password' in kwargs.keys():
            password = kwargs['password']
            user.set_password(password)

        user.save(using= self._db)
        return user

    def create_superuser(self, email, password, **kwargs):

        user = self.create_user(email,password= password)
        user.is_admin = True
        user.save(using= self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique= True, primary_key= True)
    is_admin = models.BooleanField(default= False)
    is_automobiliste = models.BooleanField(default=False)
    is_admin_fabriquant = models.BooleanField(default=False)
    is_fabriquant = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class AutomobisteManger(UserManager):
    def create_user(self, email, **kwargs):
        automobiliste = super().create_user(email=email)
        automobiliste.is_automobiliste = True
        automobiliste.save(using=self._db)
        return automobiliste


class Automobiliste(User):
    objects = AutomobisteManger()



class FabriquantManager(UserManager):


    def create_user(self, email, **kwargs):
        fabriquant = super().create_user(email, password= kwargs['password'])
        fabriquant.is_fabriquant = True
        if 'nom' in kwargs.keys():
            fabriquant.nom = kwargs['nom']
        if 'prenom' in kwargs.keys():
            fabriquant.prenom = kwargs['prenom']
        if 'adresse' in kwargs.keys():
            fabriquant.adresse = kwargs['adresse']
        if 'tel' in kwargs.keys():
            fabriquant.tel = kwargs['tel']

        if (not 'marque' in kwargs.keys()) :
            raise ValueError("L'utilisateur fabriquant doit avoir une maruqe")
        elif not kwargs['marque'] :
            raise ValueError("L'utilisateur fabriquant doit avoir une maruqe")
        else:
            fabriquant.marque = kwargs['marque']
        fabriquant.save(using=self._db)
        return fabriquant

    def create_superuser(self, email, password, **kwargs):
        admin_fabriquant = self.create_user(email=email,
                                            password= password, **kwargs
                                            # nom= kwargs['nom'],
                                            # prenom=kwargs['prenom'],
                                            # adresse= kwargs['adresse'],
                                            # tel= kwargs['tel'],
                                            # marque=kwargs['marque']
                                            )
        admin_fabriquant.is_admin_fabriquant = True
        admin_fabriquant.save(using=self._db)
        return admin_fabriquant

    def has_admin(self, marque):
        return self.filter(Q(marque_id=marque) & Q(is_admin_fabriquant=True)).count() > 0



class Fabriquant(User):
    nom     =           models.CharField(max_length=255)
    prenom  =           models.CharField(max_length=255)
    adresse =           models.CharField(max_length=255)
    tel     =           models.CharField(max_length=12, blank=True)
    marque  =           models.ForeignKey(Marque,on_delete=models.CASCADE, null=True, parent_link=False, primary_key=False)
    #TODO phone number validation
    objects = FabriquantManager()






class AdministratuerManager(UserManager):
    def create_superuser(self, email, **kwargs):
        adiministrateur = super().create_superuser(email=email, password= kwargs['password'])
        adiministrateur.save(using=self._db)
        return adiministrateur


class Administrateur(User):

    objects = AdministratuerManager()

