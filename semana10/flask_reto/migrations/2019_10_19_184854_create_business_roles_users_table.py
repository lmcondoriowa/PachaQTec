from orator.migrations import Migration


class CreateBusinessRolesUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('business_roles_users') as table:
            table.increments('id')
            table.integer('business_id')
            table.integer('users_id')
            table.integer('roles_id')
            table.timestamps()  

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('business_roles_users')
