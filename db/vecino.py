from enum import unique
from db.config import Base
from sqlalchemy import Column, Integer, String,BigInteger,Float,Date,Boolean

class Vecino(Base):
    __tablename__ = 'maestro_vecinos'
    id                              = Column(BigInteger, primary_key=True,autoincrement=True,nullable=False,unique=True)
    nombre                          = Column(String(255), nullable=True)
    ap_paterno                      = Column(String(255), nullable=True)
    ap_materno                      = Column(String(255), nullable=True)
    email                           = Column(String(255), nullable=True)
    rut                             = Column(String(30), nullable=True,unique=True)
    sexo                            = Column(Boolean, nullable=True,default=True)
    id_region                       = Column(Integer, nullable=True)
    id_comuna                       = Column(Integer, nullable=True)
    fc_nacimiento                   = Column(Date, nullable=True)
    celular                         = Column(Integer, nullable=True)
    id_direccion                    = Column(Integer, nullable=True)


    def __init__(self,nombre,ap_paterno,ap_materno,email,rut,sexo,id_region,id_comuna,fc_nacimiento,celular,id_direccion):
        self.nombre        = nombre
        self.ap_paterno    = ap_paterno
        self.ap_materno    = ap_materno
        self.email         = email
        self.rut           = rut
        self.sexo          = sexo
        self.id_region     = id_region
        self.id_comuna     = id_comuna
        self.fc_nacimiento = fc_nacimiento
        self.celular       = celular
        self.id_direccion  = id_direccion
         

