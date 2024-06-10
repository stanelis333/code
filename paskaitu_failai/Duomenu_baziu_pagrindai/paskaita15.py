import sqlalchemy as sqla
from sqlalchemy.orm import declarative_base, sessionmaker
 
engine = sqla.create_engine("sqlite:///main_database.db")
 
Base = declarative_base() # pagrindinis sqlalchemy elementas, kuriame yra surisimo (klases su lentele) logika

class Knyga(Base):
    __tablename__ = "Knygos"
    id = sqla.Column(sqla.Integer, primary_key=True)
    autorius = sqla.Column(sqla.String)
    pavadinimas = sqla.Column(sqla.String)
     
    def __init__(self, autorius, pavadinimas):
        self.autorius = autorius
        self.pavadinimas = pavadinimas

    def __repr__(self):
        return f"{self.autorius} {self.pavadinimas}"
    

Base.metadata.create_all(engine)

session = sessionmaker(engine)
Sess = session()
knyga1 = Knyga("J.K", "Haris Poteris")
Sess.add(knyga1)
Sess.commit()

print(Sess.query(Knyga).all())
print(Sess.query(Knyga).filter_by(id=2).first())