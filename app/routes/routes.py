import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.tipos_platazos import Platazos



rutas_platos = Blueprint("routes", __name__)


@rutas_platos.route('/')
def index():
    return render_template('index.html')

@rutas_platos.route('/paella')
def paella():
    return render_template('paella.html')


@rutas_platos.route('/formulario')
def formulario():
    return render_template('formulario.html')

@rutas_platos.route('/datostabla')
def datostabla():
    tipos_platazos = Platazos()

    platos = tipos_platazos.select_all(db)

    return render_template('datostabla.html',platos=platos )



@rutas_platos.route('/nueva')
def nueva():
    loquequiera=random.randint(1,100)
    loquequiera2=random.randint(1,100)


    return render_template('nueva.html',aleatorio1=loquequiera,aleatorio2=loquequiera2)
