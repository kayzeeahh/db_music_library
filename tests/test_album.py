from lib.album import Album

def test_album_constructs():
    album = Album(1, "Test title", "Test release_year", "Test artist_id" )
    assert album.id == 1
    assert album.title == "Test title"
    assert album.release_year == "Test release_year"
    assert album.artist_id == "Test artist_id"
    
def test_albums_are_equal():
    album1 = Album(1, "Test title", "Test release_year", "Test artist_id")
    album2 = Album(1, "Test title", "Test release_year", "Test artist_id")
    assert album1 == album2
    
def test_album_format_nicely():
    album = Album(1, "Test title", "Test release_year", "Test artist_id")
    assert str(album) == "Album(1, Test title, Test release_year, Test artist_id)"
    
