from enum import unique
from db.config import Base
from sqlalchemy import Column, Integer, String,BigInteger,Float,Date,Boolean

class Direccion(Base):
    __tablename__ = 'maestro_direcciones'

    id                       = Column(BigInteger, primary_key=True,autoincrement=True,nullable=False,unique=True)
    tp_via                   = Column(String(255), nullable=True)
    nm_calle                 = Column(String(255), nullable=True)
    nr_calle                 = Column(Integer, nullable=True)
    nm_direccion             = Column(String(255), nullable=True)
    rol_sii                  = Column(String(30), nullable=True,unique=True)
    str_latitud              = Column(String(255), nullable=True)
    str_longitud             = Column(String(255), nullable=True)
    cod_territorial          = Column(String(255), nullable=True)
    cod_unidadvecinal        = Column(String(255), nullable=True)
    tp_activo                = Column(Integer, nullable=True,default=1)


    def __init__(self,tp_via,nm_calle,nr_calle,nm_direccion,rol_sii,str_latitud,str_longitud,cod_territorial,cod_unidadvecinal,tp_activo):
        self.tp_via                 = tp_via
        self.nm_calle               = nm_calle
        self.nr_calle               = nr_calle
        self.nm_direccion           = nm_direccion
        self.rol_sii                = rol_sii
        self.str_latitud            = str_latitud
        self.str_longitud           = str_longitud
        self.cod_territorial        = cod_territorial
        self.cod_unidadvecinal     = cod_unidadvecinal
        self.tp_activo              = tp_activo
                

