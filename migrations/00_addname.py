from peewee import *
name_field = CharField(default='unknown name')

from ..models import UserPoints

def upgrade(migrator: SchemaMigrator):
    migrate(
        migrator.add_column(UserPoints._meta.db_table, 'name', name_field)
    )

def downgrade(migrator: SchemaMigrator):
    pass