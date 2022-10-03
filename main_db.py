import db.config as db
from db.vecino import Vecino
from db.direccion import Direccion

def run():
    pass
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()