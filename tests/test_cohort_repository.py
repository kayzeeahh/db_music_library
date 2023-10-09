from lib.cohort_repository import CohortRepository
from lib.cohort import *
from lib.student import *

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = CohortRepository(db_connection) # Create a new ArtistRepository

    cohorts = repository.all() # Get all artists

    # Assert on the results
    assert cohorts == [
        Cohort(1, 'Andrew1', '2023-10-06'),
        Cohort(2, 'Andrew2', '2023-10-07'),
        Cohort(3, 'Andrew3', '2023-10-08'),
        Cohort(4, 'Andrew4', '2023-10-09'),
    ]

def test_find_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohorts = repository.find(3)
    assert cohorts == Cohort(3, 'Andrew3', '2023-10-08')
    
def test_create_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    repository.create(Cohort(None, "Andrew5", "2023-10-10"))

    result = repository.all()
    assert result == [
        Cohort(1, 'Andrew1', '2023-10-06'),
        Cohort(2, 'Andrew2', '2023-10-07'),
        Cohort(3, 'Andrew3', '2023-10-08'),
        Cohort(4, 'Andrew4', '2023-10-09'),
        Cohort(5, 'Andrew5', '2023-10-10')
    ]
    
def test_delete_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Cohort(1, 'Andrew1', '2023-10-06'),
        Cohort(2, 'Andrew2', '2023-10-07'),
        Cohort(4, 'Andrew4', '2023-10-09'),
    ]

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, 'Andrew1', '2023-10-06', [
        Student(1, "Andrew1", 1),
    ])