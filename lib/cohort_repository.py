from lib.cohort import Cohort
from lib.student import *
class CohortRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(item)
        return cohorts

    # Find a single artist by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from cohorts WHERE id = %s', [id])
        row = rows[0]
        return Cohort(row["id"], row["name"], row["starting_date"])
    
    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)', [
                                 cohort.name, cohort.starting_date])
        return None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM cohorts WHERE id = %s', [id])
        return None
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            "SELECT cohorts.id as cohort_id, cohorts.name, cohorts.starting_date, students.id AS student_id, students.name, students.cohort_id " \
            "FROM cohorts JOIN students ON cohorts.id = students.cohort_id " \
            "WHERE cohorts.id = %s", [cohort_id])
        students = []
        for row in rows:
            student = Student(row["student_id"], row["name"], row["cohort_id"])
            students.append(student)

        # Each row has the same id, name, and genre, so we just use the first
        return Cohort(rows[0]["cohort_id"], rows[0]["name"], rows[0]["starting_date"], students)
    
    """def find_with_students(self, cohort_id):
        rows = self._connection.execute( 
            "SELECT * FROM cohorts JOIN students ON cohort.id = students.cohort_id"\
            "WHERE cohorts.id = %s", [cohort_id]
        )
        cohorts = []
        for row in rows:
            cohort = Cohort(row["id"], row["name"], row["starting_date"])
            cohorts.append(cohort)

        # Each row has the same id, name, and genre, so we just use the first
            return Cohort(rows[0]["id"], rows[0]["name"], rows[0]["starting_date"], students)

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, cohort_id):
        self._connection.execute('INSERT INTO cohorts (starting_date, name) VALUES (%s, %s)', [start_date, name])
        return None

    # Delete an artist by their id
    def delete(self, cohort_id):
        self._connection.execute(
            'DELETE FROM cohort WHERE id = %s', [cohort_id])
        return None"""