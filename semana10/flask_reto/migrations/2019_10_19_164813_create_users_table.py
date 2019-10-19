from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('username', 50)
            table.string('userpass')
            table.string('name', 50)
            table.string('last_name', 50)
            table.timestamps() #En mariadb nullable_timestamps

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
