from sqlalchemy import func

from main import db
import hashlib


class Dna(db.Model):
    __tablename__ = 'dna'

    key = db.Column(db.String(32), primary_key=True)
    dna = db.Column(db.String(300), unique=True)
    mutant = db.Column(db.Boolean())

    def __init__(self, dna, mutant):
        self.key = hashlib.md5(str(dna).encode('utf-8')).hexdigest()
        self.dna = str(dna)
        self.mutant = mutant

    def save(self):
        dna = Dna.query.get(self.key)
        if dna is None:
            db.session.add(self)
            db.session.commit()
            print (">> nuevo registro")

    @staticmethod
    def stats():
        mutant = human = 0
        result = db.session.query(
            Dna.mutant,
            func.count()
        ).group_by(Dna.mutant).order_by(Dna.mutant).all()

        if len(result) == 1:
            mutant = 0 if result[0][0] else result[0][1]
            human = 0 if not result[0][0] else result[0][1]
        if len(result) == 2:
            mutant = result[0][1]
            human = result[1][1]

        return mutant, human