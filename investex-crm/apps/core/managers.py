# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class BulkInsertManager(models.Manager):

    def _bulk_insert_on_duplicate(self, create_fields, values, update_fields):
        """
        Bulk insert, update on duplicate key
        @param create_fields : list, required, fields for the insert field declaration
        @param values : list of tuples. each tuple must have same len() as create_fields
        @param update_fields : list, field names to update when duplicate key is detected
        @return False on fail
        Notes on usage :
            create_fields = ['f1', 'f2', 'f3']
            values = [
                (1, 2, 3),
                (4, 5, 6),
                (5, 3, 8)
            ]
        Example usage :
            modelName.objects._bulk_insert_ignore(
                create_fields,
                values
            )
        Usage notes for update_fields :
            update_fields = ['f1', 'f2']
            where f1, f2 are not part of the unique declaration and represent
                fields to be updated on duplicate key
        Remember to add to model declarations:
            objects = BulkInsertManager() # custom manager
        """
        from django.db import connection
        cursor = connection.cursor()

        db_table = self.model._meta.db_table

        values_sql = [
            "(%s)" % (','.join([" %s " for _ in range(len(create_fields))]),)
        ]

        base_sql = "INSERT INTO %s (%s) VALUES " % (db_table, ",".join(create_fields))

        duplicate_syntax = 'ON DUPLICATE KEY UPDATE '
        comma = len(update_fields)
        for f in update_fields:
            comma = comma - 1
            duplicate_syntax = duplicate_syntax + " " + f + '= values(%s)' % f
            if comma > 0:
                duplicate_syntax = '{0},'.format(duplicate_syntax)

        sql = """%s %s %s""" % (base_sql, ", ".join(values_sql), duplicate_syntax)

        cursor.executemany(sql, values)
