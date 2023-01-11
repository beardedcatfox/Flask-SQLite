CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  length INT NOT NULL
);

INSERT INTO tracks (id, title, artist, genre, length) VALUES
    (1, 'Murder Plot', 'Kordhell', 'Phonk', 180),
    (2, 'Devils eyes', 'ZODVIC', 'Trance', 420),
    (3, 'Highway to hell', 'AC/DC', 'Rock', 380),
    (4, 'Can You Feel My Heart', 'BMTH', 'Rock', 400),
    (5, 'Shot', 'The Rasmus', 'Rock', 330),
    (6, 'Coockie Thumper!', 'DIE ANTWOORD', 'Hip-hop', 240),
    (7, 'Shape of ny heart', 'Sting', 'Pop', 250),
    (8, 'THINKIN OF A DRIVE BY', 'DVRST', 'Phonk', 310),
    (9, 'ATWA', 'SOAD', 'Rock', 330),
    (10, 'Closed eyes', 'DVRST', 'Phonk', 190);
