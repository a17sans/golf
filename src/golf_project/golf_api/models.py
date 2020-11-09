from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import datetime

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Class required by Django for managing our users from the management
    command.
    """

    def create_user(self, email, lastname, firstname, handicap, password=None):
        """Creates a new user with the given detials."""

        # Check that the user provided an email.
        if not email:
            raise ValueError('Users must have an email address.')

        # Create a new user object.
        user = self.model(
            email=self.normalize_email(email),
            lastname=lastname,
            firstname=firstname,
            handicap=handicap,
        )

        # Set the users password. We use this to create a password
        # hash instead of storing it in clear text.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, lastname, firstname, handicap, password):
        """Creates and saves a new superuser with given detials."""

        # Create a new user with the function we created above.
        user = self.create_user(
            email,
            lastname,
            firstname,
            handicap,
            password
        )

        # Make this user an admin.
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """A user profile in our system."""

    # Django fields
    email = models.EmailField(max_length=255, unique=True)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Club fields
    handicap = models.IntegerField()

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['lastname', 'firstname', 'handicap']

    def get_full_name(self):
        """
        Required function so Django knows what to use as the users full name.
        """

        return f'{self.firstname} {self.lastname}'

    def get_short_name(self):
        """
        Required function so Django knows what to use as the users short name.
        """

        return self.firstname

    def __str__(self):
        """What to show when we output an object as a string."""

        return f'{self.firstname} {self.lastname} {self.handicap}'


class Course(models.Model):
    """Describes a golf course in our system."""

    name = models.CharField(max_length=100)
    nb_holes = models.IntegerField()

    objects = models.Manager()


class Hole(models.Model):
    """Describes a hole belonging to a course in our system."""

    course = models.ForeignKey('Course', related_name='fk_course_id', on_delete=models.CASCADE)
    index = models.IntegerField()
    s_index = models.IntegerField()
    par = models.IntegerField()

    objects = models.Manager()


class MatchStrike(models.Model):
    """Describes the strikes in one match in our system."""

    date = models.DateField()
    player = models.ForeignKey('UserProfile', related_name='fk_player_id', on_delete=models.CASCADE)
    hole = models.ForeignKey('Hole', related_name='fk_hole_id', on_delete=models.CASCADE)
    hole_player_par = models.IntegerField()
    score = models.IntegerField()

    objects = models.Manager()