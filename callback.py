#python -m uvicorn main:app --reload
#pip install -r path/to/requirements.txt
import pandas as pd
from fastapi import FastAPI,Path, Response
from typing import Optional
import json
import logging
import httpx

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

from utils import parse_json

app = FastAPI()

data    = {}
status  = {}
vecino = {
            "nombre": "MARCO",
            "ap_paterno": "GERTZ",
            "ap_materno": "HINGER",
            "email": "TEST@TEST.CL",
            "rut": "76749842-K",
            "id_region": 13,
            "id_comuna": 271,
            "celular": 68465454,
            "id_direccion": 40773
        }


def callback(info):
    
    print(info)

    url             = "http://192.168.13.12:8081/api/maestros/vecinos"
    data            = {
                        "rut"               : info.rut,
                        "nombre"            : info.nombre,
                        "ap_paterno"        : info.ap_paterno,
                        "ap_materno"        : info.ap_paterno,
                        "email"             : info.email,
                        "celular"           : int('9'+str(info.celular)),
                        "id_comuna"         : info.id_comuna,
                        "id_region"         : info.id_region,
                        "id_direccion"      : info.id_direccion,
                    }

    headers = {'Authorization': 'Bearer EmKVjq8I2jB9VB0','Accept':'application/json','Content-Type':'application/json'}
    
    try:
        resp            = httpx.post(url,params=data,headers=headers)
        status_code     = resp.status_code
        resp.raise_for_status()

    except httpx.HTTPError     as exc:
        status_code = exc.response.status_code
        logger.info(json.load(exc.response))

    return status_code

   
    



@app.get("/load/{nrows}")
async def load_atencion_vecino(all_rows: Optional[int]= 0,nrows: int = Path(title="numero de registros",ge=0)):

    if all_rows:
        df = pd.read_excel('./data/gsut_vecino.xlsx')
    else:
        df = pd.read_excel('./data/gsut_vecino.xlsx',nrows=nrows)

    av = df[["nm_vecino",
                    "ap_paterno",
                    "ap_materno",
                    "nm_mail",
                    "nr_rut",
                    "id_region",
                    "id_comuna",
                    "nr_telefono",
                    "id_ubicacion"]]

    av.columns = [  'nombre',
                    'ap_paterno',
                    'ap_materno',
                    'email',
                    'rut',
                    'id_region',
                    'id_comuna',
                    'celular',
                    'id_direccion']

    for index, row in av.iterrows():
        callback(row)

    return data
