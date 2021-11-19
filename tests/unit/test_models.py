import unittest

from website.models import User


class MyTestCase(unittest.TestCase):
    def test_new_user(self):
        """
        Gitt brukermodell
        Når en ny bruker skapes:
        - Sjekk epostadresse, passord, og om rollene definert korrekt
        id = db.Column(db.Integer, primary_key=True)
        epost = db.Column(db.String(150), unique=True)
        passord = db.Column(db.String(120))
        fornavn = db.Column(db.String(100))
        etternavn = db.Column(db.String(150))
        rolle = db.Column(db.String(150))
        datetime = db.Column(db.DateTime(timezone=True))

        """
        user = User('ronny.wilhelmsen@gmail.com', 'testingtestingonetwothree', 'Ronny', 'Wilhelmsen', 'Admin' )
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
