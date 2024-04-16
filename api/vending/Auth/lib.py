from django.db.models.manager import EmptyManager
from django.contrib.auth.models import Group, Permission

from vending.Customers.models import Customer

class CustomerUser:
    id = None
    pk = None
    username = None
    customer = None
    is_staff = False
    is_active = False
    is_superuser = False
    _groups = EmptyManager(Group)
    _user_permissions = EmptyManager(Permission)

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __hash__(self):
        return self.pk

    def __init__( self, auth_token ):
        self.customer = Customer.objects.get( pk=auth_token )
        self.username = self.customer.name
        self.id = self.customer.pk
        self.pk = self.id

    def __int__( self ):
        raise TypeError('Cannot cast CustomerUser to int')

    def save(self):
        raise NotImplementedError("No DB representation for CustomerUser.")

    def delete(self):
        raise NotImplementedError("No DB representation for CustomerUser.")

    def set_password(self, raw_password):
        raise NotImplementedError("No DB representation for CustomerUser.")

    def check_password(self, raw_password):
        raise NotImplementedError("No DB representation for CustomerUser.")

    @property
    def groups(self):
        return self._groups

    @property
    def user_permissions(self):
        return self._user_permissions

    def get_user_permissions(self, obj=None):
        return set()

    def get_group_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return set()

    def has_perm(self, perm, obj=None):
        if perm in ( 'Customers.view_customer', 'Products.view_product' ):
            return True

        print( '-------------------- Has perm "{0}" for "{1}"'.format( perm, obj ) )
        return False

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, module):
        print( '-------------------- Has module perm "{0}"'.format( module))
        return False

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def get_username(self):
        return self.username
