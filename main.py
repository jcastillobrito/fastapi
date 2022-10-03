#python -m uvicorn main:app --reload
#pip install -r path/to/requirements.txt
import pandas as pd
import re
from rut_chile import rut_chile

from fastapi import FastAPI,Path, Response
from typing import Optional
import json
import logging
import httpx

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

from utils import parse_json

from db.config import session
from db.vecino import Vecino
from db.direccion import Direccion
app = FastAPI()

data    = {}
status  = {}

def quitar_espacio(texto):
    return re.sub(re.compile(r'\s+'), '', str(texto))


def callback(info):
    
    exists  = None
    ve      = None
    exists  = session.query(Vecino).filter(Vecino.rut == info.rut.strip()).count()

    print(rut_chile.is_valid_rut(info.rut))
    return 

    data_df = dict(     rut               = info.rut,
                        nombre            = info.nombre,
                        ap_paterno        = info.ap_paterno,
                        ap_materno        = info.ap_paterno,
                        email             = info.email.lower(),
                        celular           = int('9'+str(quitar_espacio(info.celular))),
                        id_comuna         = info.id_comuna,
                        id_region         = info.id_region,
                        id_direccion      = info.id_direccion,
                        sexo              = None,
                        fc_nacimiento     = None)
    if exists == 0:

        exists_dir  = session.query(Direccion).filter(Direccion.id == info.id_direccion).count()

        if exists_dir == 0:
            data_df.id_direccion = None

        ve = Vecino(    rut               = info.rut,
                        nombre            = info.nombre,
                        ap_paterno        = info.ap_paterno,
                        ap_materno        = info.ap_paterno,
                        email             = info.email.lower(),
                        celular           = int('9'+str(quitar_espacio(info.celular))),
                        id_comuna         = info.id_comuna,
                        id_region         = info.id_region,
                        id_direccion      = info.id_direccion,
                        sexo              = None,
                        fc_nacimiento     = None)

        session.add(ve)
            
    else:
        session.query(Vecino).filter(Vecino.rut == info.rut.strip()).update({'nombre'           : info.nombre,
                                                                            'ap_paterno'        : info.ap_paterno,
                                                                            'ap_materno'        : info.ap_paterno,
                                                                            'email'             : info.email.lower(),
                                                                            'celular'           : int('9'+str(quitar_espacio(info.celular))),
                                                                            'id_comuna'         : info.id_comuna,
                                                                            'id_region'         : info.id_region,
                                                                            'id_direccion'      : info.id_direccion,
                                                                            'sexo'              : None,
                                                                            'fc_nacimiento'     : None})

    session.commit()
    return exists


@app.get("/load/{nrows}")
async def load_atencion_vecino(all_rows: Optional[int]= 0,nrows: int = Path(title="numero de registros",ge=0)):

    if all_rows:
        df = pd.read_excel('./data/gsut_vecino.xlsx')
    else:
        df = pd.read_excel('./data/gsut_vecino.xlsx',nrows=nrows)

    av          = df[["nm_vecino","ap_paterno","ap_materno","nm_mail", "nr_rut","id_region","id_comuna","nr_telefono","id_ubicacion"]]

    av.columns  = ['nombre','ap_paterno','ap_materno','email','rut','id_region','id_comuna','celular','id_direccion']

    for index, row in av.iterrows():
        callback(row)

    return data
