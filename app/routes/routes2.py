import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.tipos_platazos2 import Union_plato
from app.data.tipos_platazos import Platazos
from app.data.modelo.tipos_platos import Plato


rutas_unionplatos = Blueprint("routes", __name__)


@rutas_routes2.route('/del', methods=['GET, POST'])   
def delPlato():
    id = request.form['id']
    equipo_dao = EquipoDao()
    equipo_dao.delete(db,id)
   
    return redirect(url_for('routes.verEquipos'))  




