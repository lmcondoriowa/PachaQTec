from orator.migrations import Migration


class CreateRolesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('roles') as table:
            table.increments('id')
            table.string('name', 50)
            table.integer('state')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('roles')
