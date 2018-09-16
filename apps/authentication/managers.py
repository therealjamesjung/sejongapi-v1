from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, student_id, password=None):
        if email is None:
            raise TypeError('Users must have an email.')

        if username is None:
            raise TypeError('Users must have a username.')

        if student_id is None:
            raise TypeError('Users must have a student id.')

        user = self.model(email=self.normalize_email(email), username=username, student_id=student_id)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, student_id, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, username, student_id, password)
        user.is_superuser = user.is_staff = True
        user.save()

        return user
