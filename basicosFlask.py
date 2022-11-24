#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      LENOVO
#
# Created:     27/04/2022
# Copyright:   (c) LENOVO 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask,request,render_template,session
import wikipedia
from deep_translator import GoogleTranslator
aplicacion=Flask(__name__)
#aplicacion.secret_key='miPalabraSecreta'
@aplicacion.route('/')
def bienvenida():
    return 'Bienvenido a la pagina'

@aplicacion.route('/viernes')
def metodoViernes():
    return 'dia previo al fin de semana'

@aplicacion.route('/josue')
def metodoJosue():
    return 'esta pagina es la vista de josue'

@aplicacion.route('/recibeNombre')
def metodorecibeNombre():
    nombre=request.args.get('elNombre')
    if str(nombre)=='None':
        nombre='No se ingreso ningun nombre'
    return f'hola {nombre}'

@aplicacion.route('/saludaDosPersonas')#vista
def metodoSaluda2personas():#metodo
    nombre1=request.args.get('N1')
    nombre2=request.args.get('N2')
    return f'saludos {nombre1} y {nombre2}'


#s (SAVE)
@aplicacion.route('/concepto')#vista
def metodoConcepto():#metodo
    concepto=request.args.get('elConcepto')
    if concepto==None:
        return 'debes agregar un concepto'
    else:
        if concepto.upper()=='MARTES':
            return 'segundo dia de la semana'
        elif concepto.upper()=='PYTHON':
            return 'es un lenguaje de programacion'
        elif concepto.upper()=='PERRO':
            return 'mejor amigo del hombre'
        elif concepto.upper()=='GATITO':
            return 'OTRO mejor amigo del hombre'
        else:
            return 'concepto no hallado'

    return f'saludos {nombre1} y {nombre2}'

@aplicacion.route('/mayorEdad')#vista
def metodoMayorEdad():#metodo
    edad=request.args.get('laEdad')
    edad=int(edad)
    if edad>=18:
        return 'edad de un mayor de edad'
    else:
        return 'edad de un menor de edad'

@aplicacion.route('/diasSemana')#vista
def metodoDiasSemana():#metodo
    dias={'lunes':'dia 1',
    'martes':'dia 2','miercoles':'dia 3',
    'jueves':'dia 4',  'viernes':'dia 5',
    'sabado':'dia 6','domingo':'dia 7' }
    numerodeDia=''
    nombreDia=request.args.get('elDia')
    nombreDia=nombreDia.lower()#conversion a minusculas
    if nombreDia in dias.keys():
        numerodeDia=dias[nombreDia]
    else:
        return 'dia no hallado'
    return numerodeDia

@aplicacion.route('/hola')#vista
def metodoHola():#metodo
    return render_template('hola.html')

@aplicacion.route('/sumaNumerosPlantilla')#vista
def metodoSumaNumerosPlantilla():#metodo
    return render_template('sumadosnumeros.html')

@aplicacion.route('/recibeSumaNumeros')#vista
def metodorecibeSumaNumeros():#metodo
    n1=request.args.get('numerito1')
    n2=request.args.get('numerito2')
    n1=int(n1)
    n2=int(n2)
    r=n1+n2
    return f'la suma de {n1} y {n2} es {r}'+\
            '<br><a href="/sumaNumerosPlantilla">ir a suma</a>'

@aplicacion.route('/listaOpciones')#vista
def metodolistaOpciones():#metodo
    return render_template('formlista.html')

@aplicacion.route('/recibeLista')#vista
def metodorecibeLista():#metodo
    color=request.args.get('miListilla')
    return f'el color elegido es {color}'+\
            '<br><a href="/listaOpciones">ir a Lista</a>'

@aplicacion.route('/formularioChecks')#vista
def metodoformularioChecks():#metodo
    return render_template('formularioCheckboxes.html')

@aplicacion.route('/recibeChecks')#vista
def metodorecibeChecks():#metodo
    colores=request.args.getlist('colorcito')
    return f'los colores elegidos {colores}'+\
            '<br><a href="/formularioChecks">ir a Checkboxes</a>'

@aplicacion.route('/formularioRadios')#vista
def metodoformularioRadios():#metodo
    return render_template('formularioRadioBotones.html')

@aplicacion.route('/recibeRadios')#vista
def metodorecibeRadios():#metodo
    color=request.args.get('colorOpcion')
    return f'el color elegido es {color}'+\
            '<br><a href="/formularioRadios">ir a formulario radios</a>'

@aplicacion.route('/formularioCajas')#vista
def metodoformularioCajas():#metodo
    return render_template('formularioCajasTexto.html')

@aplicacion.route('/recibeCajas')#vista
def metodorecibeCajas():#metodo
    nombre=request.args.get('nombrecillo')
    apellido=request.args.get('apellido')
    return f'el nombre es {nombre} {apellido}'+\
            '<br><a href="/formularioCajas">ir a formulario cajas</a>'

@aplicacion.route('/buscarWikipedia')#vista
def metodobuscarWikipedia():#metodo
    palabra=request.args.get('laPalabra')
    wikipedia.set_lang('es')#respuestas en español
    try:
        busqueda=wikipedia.page(palabra)
        resultado=busqueda.summary#resumen
        return resultado+'<br><a href="/formularioWikipedia">ir a formulario wikipedia</a>'
    except:
        return 'ocurrio un error en la busqueda'+\
        '<br><a href="/formularioWikipedia">ir a formulario wikipedia</a>'

@aplicacion.route('/formularioWikipedia')#vista
def metodoformularioWikipedia():#metodo
    return render_template('busquedaWikipedia.html')

@aplicacion.route('/traducirAIngles')#vista
def metodotraducirAIngles():#metodo
    textoEspañol=request.args.get('textoAtraducir')
    traduccion=GoogleTranslator(source='auto',target='english').\
    translate(textoEspañol)
    return traduccion+\
    '<br><a href="/formularioTraduccion">ir a formulario traduccion</a>'

@aplicacion.route('/formularioTraduccion')#vista
def metodoformularioTraduccion():#metodo
    return render_template('traduccionAingles.html')

@aplicacion.route('/formularioImagen')#vista
def metodoformularioImagen():#metodo
    return render_template('mostrarImagen.html')

@aplicacion.route('/recibeEdad')#vista
def metodorecibeEdad():#metodo
    laEdad=request.args.get('unaEdad')
    laEdad=int(laEdad)
    #return laEdad
    return render_template('usoIfPlantilla.html',edad=laEdad)

@aplicacion.route('/recibeNumeroCiclo')#vista
def metodorecibeNumeroCiclo():#metodo
    unNumero=request.args.get('elNumero')
    unNumero=int(unNumero)
    return render_template('forPlantilla.html',numero=unNumero)

@aplicacion.route('/muestraListaPlantilla')#vista
def metodomuestraListaPlantilla():#metodo
    paises=['Mexico','Francia','Africa','Alemania']
    return render_template('listaPlantilla.html',losPaises=paises)

@aplicacion.route('/recibeTextoComas')#vista
def metodorecibeTextoComas():#metodo
    textoConComas=request.args.get('elTexto')
    return textoConComas

@aplicacion.route('/formularioCubo')#vista
def metodoformularioCubo():#metodo
    return render_template('cubo.html')

@aplicacion.route('/recibeNumeroCubo')#vista
def metodorecibeNumeroCubo():#metodo
    elNumero=request.args.get('unNumero')
    elNumero=int(elNumero)
    cubo=elNumero**3
    return f'el cubo de {elNumero} es {cubo}'+\
    '<br><a href="/formularioCubo">Ir a formulario cubo</a>'

@aplicacion.route('/formularioPerimetroCuadrado')#vista
def metodoformularioPerimetroCuadrado():#metodo
    return render_template('cuadrado.html')

@aplicacion.route('/recibeNumeroPerimetro')#vista
def metodorecibeNumeroPerimetro():#metodo
    lado=request.args.get('elLado')
    lado=int(lado)
    perimetro=lado+lado+lado+lado
    return f'el cuadrado con lado {lado} es igual {perimetro}'+\
    '<br><a href="/formularioPerimetroCuadrado">ir a perimetro cuadrado</a>'

@aplicacion.route('/formularioAreaRectangulo')#vista
def metodoformularioAreaRectangulo():#metodo
    return render_template('areaRectangulo.html')


if __name__ == '__main__':
    aplicacion.run(host='0.0.0.0',port='8010',
    debug=True )
