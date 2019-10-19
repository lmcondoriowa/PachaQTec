from orator.migrations import Migration


class CreateBusinessTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('business') as table:
            table.increments('id')
            table.string('name', 50)
            table.string('ruc', 11)
            table.string('address', 80)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('business')
