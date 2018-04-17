import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('')
code_salida = ""
code_destino = ""
rutas = []

def get_html(origen,fecha,destino,hora):
    url = "https://www.metrovalencia.es/planificador.php"
    params = {'origen':origen,'fecha':fecha,'destino':destino,'hora':hora,'calcular':1}
    try:
        response = requests.post(url,params=params,verify=False)
    except:
        return "error"

    if response.status_code == 200:
        return response.text
    else:
        return "error"

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    descriptions = soup.findAll("div", {"class": "description"})
    pasos = []
    for description in descriptions:
        stop = {}
        descripcion = ""
        salida = ""
        llegada = ""
        linea = ""
        duracion = ""
        if description.find('img'):
            linea = description.find('img').get('src')[-5]
        if "Toma la línea" in description.get_text():
            step = description.get_text().split("\n")
            descripcion += step[0]
            salida += step[1]
            llegada += step[4]
            duracion += step[5]
        elif "Transbordo en" in description.get_text():
            step = description.get_text().split("\n")
            descripcion += step[0].split("Tiempo de espera")[0]
            #r = step[1].split("")[0] + linea + step[1].split("")[0]
            salida += step[1]
            llegada += step[4]
            duracion += step[5]
        else:
            parada = description.get_text()  
        stop = {'linea': linea,'parada': parada,'description': descripcion, 'salida':salida, 'llegada':llegada,'duracion': duracion}
        pasos.append(stop)    
    return pasos

def get_time():
    from time import localtime, strftime
    return strftime("%d/%m/%Y %H:%M", localtime())

@bot.message_handler(commands=['rutas'])
def send_rutas(message):
    markup = types.ReplyKeyboardMarkup(row_width=4)
    try:
        for r in rutas:           
            if len(r) < 15:
                markup.add(types.KeyboardButton(r))
        bot.send_message(message.chat.id, "Selecciona tu ruta:", reply_markup=markup)

        bot.register_next_step_handler(message, step_rutas)
    except:
        bot.reply_to(message, "No hay ninguna ruta guardada")

def step_rutas(message):
    for r in range(len(rutas)):
        if len(rutas[r]) > 15:
            bot.send_message(message.chat.id, rutas[r])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Diseña una ruta con /nueva y después puedes guardarla añadiendo un nombre.\nUna vez guardada selecciona /rutas y el nombre con la que la guardaste.")

@bot.message_handler(commands=['nueva'])
def send_new(message):
    markup = types.ReplyKeyboardMarkup(row_width=4)
    alameda = types.KeyboardButton('Alameda')
    albalat = types.KeyboardButton('Albalat dels Sorells')
    alberic = types.KeyboardButton('Alberic')
    alboraya = types.KeyboardButton('Alboraya-Palmaret')
    alboraya_1 = types.KeyboardButton('Alboraya-Peris Aragó')
    alfauir = types.KeyboardButton('Alfauir')
    alginet = types.KeyboardButton('Alginet')
    almassera = types.KeyboardButton('Almàssera')
    amistat = types.KeyboardButton('Amistat-Casa de Salud')
    guimera = types.KeyboardButton('Àngel Guimerà')
    aragon = types.KeyboardButton('Aragón')
    ausias = types.KeyboardButton('Ausiàs March')
    cid = types.KeyboardButton('Av. del Cid')
    ayora = types.KeyboardButton('Ayora')
    bailen = types.KeyboardButton('Bailén')
    betera = types.KeyboardButton('Bétera')
    benaguasil_1 = types.KeyboardButton('Benaguasil 1r')
    benaguasil_2 = types.KeyboardButton('Benaguasil 2n')
    benicalap = types.KeyboardButton('Benicalap')
    beniferri = types.KeyboardButton('Beniferri')
    benimaclet = types.KeyboardButton('Benimaclet')
    benimamet = types.KeyboardButton('Benimàmet')
    benimodo = types.KeyboardButton('Benimodo')
    burjassot = types.KeyboardButton('Burjassot')
    godella = types.KeyboardButton('Burjassot - Godella')
    campament = types.KeyboardButton('Campament')
    campanar = types.KeyboardButton('Campanar')
    campus = types.KeyboardButton('Campus')
    cantereria = types.KeyboardButton('Canterería')
    carlet = types.KeyboardButton('Carlet')
    colon = types.KeyboardButton('Colón')
    vedat = types.KeyboardButton('Col·legi El Vedat')
    lluch = types.KeyboardButton('Dr. Lluch')
    clot = types.KeyboardButton('El Clot')
    empalme = types.KeyboardButton('Empalme')
    entrepins = types.KeyboardButton('Entrepins')
    espioca = types.KeyboardButton('Espioca')
    llevant = types.KeyboardButton('Estadi del Llevant')
    eugenia = types.KeyboardButton('Eugenia Viñes')
    facultats = types.KeyboardButton('Facultats')
    faitanar = types.KeyboardButton('Faitanar')
    fira = types.KeyboardButton('Fira València')
    florista = types.KeyboardButton('Florista')
    foios = types.KeyboardButton('Foios')
    font = types.KeyboardButton('Font Almaguer')
    francesc = types.KeyboardButton('Francesc Cubells')
    fuente = types.KeyboardButton('Fuente del Jarro')
    garbi = types.KeyboardButton('Garbí')
    godella = types.KeyboardButton('Godella')
    grau = types.KeyboardButton('Grau - Canyamelar')
    horta = types.KeyboardButton('Horta Vella')
    jesus = types.KeyboardButton('Jesús')
    alcudia = types.KeyboardButton('L\'Alcúdia')
    eliana = types.KeyboardButton('L\'Eliana')
    cadena = types.KeyboardButton('La Cadena')
    cayada = types.KeyboardButton('La Canyada')
    carrasca = types.KeyboardButton('La Carrasca')
    coma = types.KeyboardButton('La Coma')
    cova = types.KeyboardButton('La Cova')
    granja = types.KeyboardButton('La Granja')
    marina = types.KeyboardButton('La Marina')
    farnals = types.KeyboardButton('La Pobla de Farnals')
    vallbona = types.KeyboardButton('La Pobla de Vallbona')
    presa = types.KeyboardButton('La Presa')
    vallesa = types.KeyboardButton('La Vallesa')
    arenes = types.KeyboardButton('Les Arenes')
    carolines = types.KeyboardButton('Les Carolines/Fira')
    llarga = types.KeyboardButton('Ll. Llarga - Terramelar')
    lliria = types.KeyboardButton('Llíria')
    machado = types.KeyboardButton('Machado')
    manises = types.KeyboardButton('Manises')
    maritim = types.KeyboardButton('Marítim - Serrería')
    marina = types.KeyboardButton('Marina Reial Joan Carles I')
    marxalenes = types.KeyboardButton('Marxalenes')
    mas = types.KeyboardButton('Mas del Rosari')
    masia = types.KeyboardButton('Masia de Traver')
    masies = types.KeyboardButton('Masies')
    massalaves = types.KeyboardButton('Massalavés')
    massamagrell = types.KeyboardButton('Massamagrell')
    massarrojos = types.KeyboardButton('Massarrojos')
    mediterrani = types.KeyboardButton('Mediterrani')
    meliana = types.KeyboardButton('Meliana')
    mislata = types.KeyboardButton('Mislata')
    almassil = types.KeyboardButton('Mislata - Almassil')
    moncada = types.KeyboardButton('Moncada - Alfara')
    montesol = types.KeyboardButton('Montesol')
    montortal = types.KeyboardButton('Montortal')
    museros = types.KeyboardButton('Museros')
    octubre = types.KeyboardButton('Nou d\'Octubre')
    omet = types.KeyboardButton('Omet')
    orriols = types.KeyboardButton('Orriols')
    paiporta = types.KeyboardButton('Paiporta')
    congresos = types.KeyboardButton('Palau de Congressos')
    paterna = types.KeyboardButton('Paterna')
    patraix = types.KeyboardButton('Patraix')
    picanya = types.KeyboardButton('Picanya')
    picassent = types.KeyboardButton('Picassent')
    espanya = types.KeyboardButton('Pl. Espanya')
    fusta = types.KeyboardButton('Pont de Fusta')
    primat = types.KeyboardButton('Primat Reig')
    quart = types.KeyboardButton('Quart de Poblet')
    rafel = types.KeyboardButton('Rafelbunyol')
    realon = types.KeyboardButton('Realón')
    reus = types.KeyboardButton('Reus')
    riba = types.KeyboardButton('Riba-roja de Túria')
    rocafort = types.KeyboardButton('Rocafort')
    rosas = types.KeyboardButton('Rosas')
    safranar = types.KeyboardButton('Safranar')
    sagunt = types.KeyboardButton('Sagunt')
    salt = types.KeyboardButton('Salt de l\'Aigua')
    sant_i = types.KeyboardButton('Sant Isidre')
    sant_j = types.KeyboardButton('Sant Joan')
    sant_m = types.KeyboardButton('Sant Miquel dels Reis')
    sant_r = types.KeyboardButton('Sant Ramon')
    sant_g = types.KeyboardButton('Santa Gemma - Parc Científic UV')
    sant_ri = types.KeyboardButton('Santa Rita')
    seminari = types.KeyboardButton('Seminari - CEU')
    serreria = types.KeyboardButton('Serrería')
    tarongers = types.KeyboardButton('Tarongers')
    turia = types.KeyboardButton('Túria')
    tomas = types.KeyboardButton('Tomás y Valiente')
    torre = types.KeyboardButton('Torre del Virrei')
    torrent = types.KeyboardButton('Torrent')
    torrent_av = types.KeyboardButton('Torrent Avinguda')
    tossal = types.KeyboardButton('Tossal del Rei')
    transits = types.KeyboardButton('Trànsits')
    tvv = types.KeyboardButton('TVV')
    upv = types.KeyboardButton('Universitat Politècnica')
    sud = types.KeyboardButton('València Sud')
    estelles = types.KeyboardButton('Vicent Andrés Estellés')
    zaragossa = types.KeyboardButton('Vicente Zaragozá')
    villanova = types.KeyboardButton('Villanueva de Castellón')
    xativa = types.KeyboardButton('Xàtiva')
    markup.add(alameda,albalat,alberic,alboraya,alboraya_1,alfauir,alginet,almassera,amistat,guimera,aragon,ausias,cid,ayora,bailen,betera,benaguasil_1,benaguasil_2,benicalap,beniferri,benimaclet,benimamet,benimodo,burjassot,godella,campament,campanar,campus,cantereria,carlet,colon,vedat,lluch,clot,empalme,entrepins,espioca,llevant,eugenia,facultats,faitanar,fira,florista,foios,font,francesc,fuente,garbi,godella,grau,horta,jesus,alcudia,eliana,cadena,cayada,carrasca,coma,cova,granja,marina,farnals,vallbona,presa,vallesa,arenes,carolines,llarga,lliria,machado,manises,maritim,marina,marxalenes,mas,masia,masies,massalaves,massamagrell,massarrojos,mediterrani,meliana,mislata,almassil,moncada,montesol,montortal,museros,octubre,omet,orriols,paiporta,congresos,paterna,patraix,picanya,picassent,espanya,fusta,primat,quart,rafel,realon,reus,riba,rocafort,rosas,safranar,sagunt,salt,sant_i,sant_j,sant_m,sant_r,sant_g,sant_ri,seminari,serreria,tarongers,turia,tomas,torre,torrent,torrent_av,tossal,transits,tvv,upv,sud,estelles,zaragossa,villanova,xativa)
    bot.send_message(message.chat.id, "Elige estación de salida:", reply_markup=markup)

    bot.register_next_step_handler(message, step_salida)

def step_salida(message):
    code = ""
    try:
        salida = str(message.text)
        if salida == 'Alameda':
            code = '14'
        elif salida == 'Albalat dels Sorells':
            code = '5'
        elif salida == 'Alberic':
            code = '36'
        elif salida == 'Alboraya-Palmaret':
            code = '10'
        elif salida == 'Alboraya-Peris Aragó':
            code = '9'
        elif salida == 'Alfauir':
            code = '128'
        elif salida == 'Alginet':
            code = '43'
        elif salida == 'Almàssera':
            code = '8'
        elif salida == 'Amistat-Casa de Salud':
            code = '23'
        elif salida == 'Àngel Guimerà':
            code = '17'
        elif salida == 'Aragón':
            code = '24'
        elif salida == 'Ausiàs March':
            code = '42'
        elif salida == 'Av. del Cid':
            code = '18'
        elif salida == 'Ayora':
            code = '22'
        elif salida == 'Bailén':
            code = '109'
        elif salida == 'Bétera':
            code = '107'
        elif salida == 'Benaguasil 1r':
            code = '69'
        elif salida == 'Benaguasil 2n':
            code = '70'
        elif salida == 'Benicalap':
            code = '97'
        elif salida == 'Beniferri':
            code = '54'
        elif salida == 'Benimaclet':
            code = '12'
        elif salida == 'Benimàmet':
            code = '57'
        elif salida == 'Benimodo':
            code = '40'
        elif salida == 'Burjassot':
            code = '72'
        elif salida == 'Burjassot - Godella':
            code = '73'
        elif salida == 'Campament':
            code = '59'
        elif salida == 'Campanar':
            code = '53'
        elif salida == 'Campus':
            code = '103'
        elif salida == 'Canterería':
            code = '56'
        elif salida == 'Carlet':
            code = '41'
        elif salida == 'Colón':
            code = '15'
        elif salida == 'Col·legi El Vedat':
            code = '50'
        elif salida == 'Dr. Lluch':
            code = '83'
        elif salida == 'El Clot':
            code = '108'
        elif salida == 'Empalme':
            code = '55'
        elif salida == 'Entrepins':
            code = '65'
        elif salida == 'Espioca':
            code = '45'
        elif salida == 'Estadi del Llevant':
            code = '130'
        elif salida == 'Eugenia Viñes':
            code = '81'
        elif salida == 'Facultats':
            code = '13'
        elif salida == 'Faitanar':
            code = '200'
        elif salida == 'Fira València':
            code = '106'
        elif salida == 'Florista':
            code = '99'
        elif salida == 'Foios':
            code = '6'
        elif salida == 'Font Almaguer':
            code = '44'
        elif salida == 'Francesc Cubells':
            code = '122'
        elif salida == 'Fuente del Jarro':
            code = '62'
        elif salida == 'Garbí':
            code = '98'
        elif salida == 'Godella':
            code = '74'
        elif salida == 'Grau - Canyamelar':
            code = '123'
        elif salida == 'Horta Vella':
            code = '80'
        elif salida == 'Jesús':
            code = '25'
        elif salida == 'L\'Alcúdia':
            code = '39'
        elif salida == 'L\'Eliana':
            code = '67'
        elif salida == 'La Cadena':
            code = '85'
        elif salida == 'La Canyada':
            code = '63'
        elif salida == 'La Carrasca':
            code = '88'
        elif salida == 'La Coma':
            code = '111'
        elif salida == 'La Cova':
            code = '183'
        elif salida == 'La Granja':
            code = '101'
        elif salida == 'La Marina':
            code = '84'
        elif salida == 'La Pobla de Farnals':
            code = '2'
        elif salida == 'La Pobla de Vallbona':
            code = '68'
        elif salida == 'La Presa':
            code = '184'
        elif salida == 'La Vallesa':
            code = '64'
        elif salida == 'Les Arenes':
            code = '82'
        elif salida == 'Les Carolines/Fira':
            code = '58'
        elif salida == 'Ll. Llarga - Terramelar':
            code = '114'
        elif salida == 'Llíria':
            code = '71'
        elif salida == 'Machado':
            code = '11'
        elif salida == 'Manises':
            code = '119'
        elif salida == 'Marítim - Serrería':
            code = '115'
        elif salida == 'Marina Reial Joan Carles I':
            code = '126'
        elif salida == 'Marxalenes':
            code = '95'
        elif salida == 'Mas del Rosari':
            code = '110'
        elif salida == 'Masia de Traver':
            code = '185'
        elif salida == 'Masies':
            code = '79'
        elif salida == 'Massalavés':
            code = '37'
        elif salida == 'Massamagrell':
            code = '3'
        elif salida == 'Massarrojos':
            code = '76'
        elif salida == 'Mediterrani':
            code = '127'
        elif salida == 'Meliana':
            code = '7'
        elif salida == 'Mislata':
            code = '20'
        elif salida == 'Mislata - Almassil':
            code = '21'
        elif salida == 'Moncada - Alfara':
            code = '77'
        elif salida == 'Montesol':
            code = '66'
        elif salida == 'Montortal':
            code = '38'
        elif salida == 'Museros':
            code = '4'
        elif salida == 'Nou d\'Octubre':
            code = '19'
        elif salida == 'Omet\'Orriols':
            code = '46'
        elif salida == 'Paiporta':
            code = '129'
        elif salida == 'Palau de Congressos':
            code = '100'
        elif salida == 'Paterna':
            code = '60'
        elif salida == 'Patraix':
            code = '26'
        elif salida == 'Picanya':
            code = '32'
        elif salida == 'Picassent':
            code = '47'
        elif salida == 'Pl. Espanya':
            code = '51'
        elif salida == 'Pont de Fusta':
            code = '92'
        elif salida == 'Primat Reig':
            code = '91'
        elif salida == 'Quart de Poblet':
            code = '117'
        elif salida == 'Rafelbunyol':
            code = '1'
        elif salida == 'Realón':
            code = '49'
        elif salida == 'Reus':
            code = '94'
        elif salida == 'Riba-roja de Túria':
            code = '186'
        elif salida == 'Rocafort':
            code = '75'
        elif salida == 'Rosas':
            code = '120'
        elif salida == 'Safranar':
            code = '27'
        elif salida == 'Sagunt':
            code = '93'
        elif salida == 'Salt de l\'Aigua':
            code = '118'
        elif salida == 'Sant Isidre':
            code = '28'
        elif salida == 'Sant Joan':
            code = '102'
        elif salida == 'Sant Miquel dels Reis':
            code = '131'
        elif salida == 'Sant Ramon':
            code = '48'
        elif salida == 'Santa Gemma - Parc Científic UV':
            code = '113'
        elif salida == 'Santa Rita':
            code = '61'
        elif salida == 'Seminari - CEU':
            code = '78'
        elif salida == 'Serrería':
            code = '86'
        elif salida == 'Tarongers':
            code = '87'
        elif salida == 'Túria':
            code = '52'
        elif salida == 'Tomás y Valiente':
            code = '112'
        elif salida == 'Torre del Virrei':
            code = '201'
        elif salida == 'Torrent':
            code = '33'
        elif salida == 'Torrent Avinguda':
            code = '34'
        elif salida == 'Tossal del Rei':
            code = '132'
        elif salida == 'Trànsits':
            code = '96'
        elif salida == 'TVV':
            code = '105'
        elif salida == 'Universitat Politècnica':
            code = '89'
        elif salida == 'València Sud':
            code = '30'
        elif salida == 'Vicent Andrés Estellés':
            code = '104'
        elif salida == 'Vicente Zaragozá':
            code = '90'
        elif salida == 'Villanueva de Castellón':
            code = '35'
        elif salida == 'Xàtiva':
            code = '16'
        else:
            bot.reply_to(message, 'Fallo al seleccionar la estación')

        global code_salida
        code_salida = code

        markup = types.ReplyKeyboardMarkup(row_width=4)
        alameda = types.KeyboardButton('Alameda')
        albalat = types.KeyboardButton('Albalat dels Sorells')
        alberic = types.KeyboardButton('Alberic')
        alboraya = types.KeyboardButton('Alboraya-Palmaret')
        alboraya_1 = types.KeyboardButton('Alboraya-Peris Aragó')
        alfauir = types.KeyboardButton('Alfauir')
        alginet = types.KeyboardButton('Alginet')
        almassera = types.KeyboardButton('Almàssera')
        amistat = types.KeyboardButton('Amistat-Casa de Salud')
        guimera = types.KeyboardButton('Àngel Guimerà')
        aragon = types.KeyboardButton('Aragón')
        ausias = types.KeyboardButton('Ausiàs March')
        cid = types.KeyboardButton('Av. del Cid')
        ayora = types.KeyboardButton('Ayora')
        bailen = types.KeyboardButton('Bailén')
        betera = types.KeyboardButton('Bétera')
        benaguasil_1 = types.KeyboardButton('Benaguasil 1r')
        benaguasil_2 = types.KeyboardButton('Benaguasil 2n')
        benicalap = types.KeyboardButton('Benicalap')
        beniferri = types.KeyboardButton('Beniferri')
        benimaclet = types.KeyboardButton('Benimaclet')
        benimamet = types.KeyboardButton('Benimàmet')
        benimodo = types.KeyboardButton('Benimodo')
        burjassot = types.KeyboardButton('Burjassot')
        godella = types.KeyboardButton('Burjassot - Godella')
        campament = types.KeyboardButton('Campament')
        campanar = types.KeyboardButton('Campanar')
        campus = types.KeyboardButton('Campus')
        cantereria = types.KeyboardButton('Canterería')
        carlet = types.KeyboardButton('Carlet')
        colon = types.KeyboardButton('Colón')
        vedat = types.KeyboardButton('Col·legi El Vedat')
        lluch = types.KeyboardButton('Dr. Lluch')
        clot = types.KeyboardButton('El Clot')
        empalme = types.KeyboardButton('Empalme')
        entrepins = types.KeyboardButton('Entrepins')
        espioca = types.KeyboardButton('Espioca')
        llevant = types.KeyboardButton('Estadi del Llevant')
        eugenia = types.KeyboardButton('Eugenia Viñes')
        facultats = types.KeyboardButton('Facultats')
        faitanar = types.KeyboardButton('Faitanar')
        fira = types.KeyboardButton('Fira València')
        florista = types.KeyboardButton('Florista')
        foios = types.KeyboardButton('Foios')
        font = types.KeyboardButton('Font Almaguer')
        francesc = types.KeyboardButton('Francesc Cubells')
        fuente = types.KeyboardButton('Fuente del Jarro')
        garbi = types.KeyboardButton('Garbí')
        godella = types.KeyboardButton('Godella')
        grau = types.KeyboardButton('Grau - Canyamelar')
        horta = types.KeyboardButton('Horta Vella')
        jesus = types.KeyboardButton('Jesús')
        alcudia = types.KeyboardButton('L\'Alcúdia')
        eliana = types.KeyboardButton('L\'Eliana')
        cadena = types.KeyboardButton('La Cadena')
        cayada = types.KeyboardButton('La Canyada')
        carrasca = types.KeyboardButton('La Carrasca')
        coma = types.KeyboardButton('La Coma')
        cova = types.KeyboardButton('La Cova')
        granja = types.KeyboardButton('La Granja')
        marina = types.KeyboardButton('La Marina')
        farnals = types.KeyboardButton('La Pobla de Farnals')
        vallbona = types.KeyboardButton('La Pobla de Vallbona')
        presa = types.KeyboardButton('La Presa')
        vallesa = types.KeyboardButton('La Vallesa')
        arenes = types.KeyboardButton('Les Arenes')
        carolines = types.KeyboardButton('Les Carolines/Fira')
        llarga = types.KeyboardButton('Ll. Llarga - Terramelar')
        lliria = types.KeyboardButton('Llíria')
        machado = types.KeyboardButton('Machado')
        manises = types.KeyboardButton('Manises')
        maritim = types.KeyboardButton('Marítim - Serrería')
        marina = types.KeyboardButton('Marina Reial Joan Carles I')
        marxalenes = types.KeyboardButton('Marxalenes')
        mas = types.KeyboardButton('Mas del Rosari')
        masia = types.KeyboardButton('Masia de Traver')
        masies = types.KeyboardButton('Masies')
        massalaves = types.KeyboardButton('Massalavés')
        massamagrell = types.KeyboardButton('Massamagrell')
        massarrojos = types.KeyboardButton('Massarrojos')
        mediterrani = types.KeyboardButton('Mediterrani')
        meliana = types.KeyboardButton('Meliana')
        mislata = types.KeyboardButton('Mislata')
        almassil = types.KeyboardButton('Mislata - Almassil')
        moncada = types.KeyboardButton('Moncada - Alfara')
        montesol = types.KeyboardButton('Montesol')
        montortal = types.KeyboardButton('Montortal')
        museros = types.KeyboardButton('Museros')
        octubre = types.KeyboardButton('Nou d\'Octubre')
        omet = types.KeyboardButton('Omet')
        orriols = types.KeyboardButton('Orriols')
        paiporta = types.KeyboardButton('Paiporta')
        congresos = types.KeyboardButton('Palau de Congressos')
        paterna = types.KeyboardButton('Paterna')
        patraix = types.KeyboardButton('Patraix')
        picanya = types.KeyboardButton('Picanya')
        picassent = types.KeyboardButton('Picassent')
        espanya = types.KeyboardButton('Pl. Espanya')
        fusta = types.KeyboardButton('Pont de Fusta')
        primat = types.KeyboardButton('Primat Reig')
        quart = types.KeyboardButton('Quart de Poblet')
        rafel = types.KeyboardButton('Rafelbunyol')
        realon = types.KeyboardButton('Realón')
        reus = types.KeyboardButton('Reus')
        riba = types.KeyboardButton('Riba-roja de Túria')
        rocafort = types.KeyboardButton('Rocafort')
        rosas = types.KeyboardButton('Rosas')
        safranar = types.KeyboardButton('Safranar')
        sagunt = types.KeyboardButton('Sagunt')
        salt = types.KeyboardButton('Salt de l\'Aigua')
        sant_i = types.KeyboardButton('Sant Isidre')
        sant_j = types.KeyboardButton('Sant Joan')
        sant_m = types.KeyboardButton('Sant Miquel dels Reis')
        sant_r = types.KeyboardButton('Sant Ramon')
        sant_g = types.KeyboardButton('Santa Gemma - Parc Científic UV')
        sant_ri = types.KeyboardButton('Santa Rita')
        seminari = types.KeyboardButton('Seminari - CEU')
        serreria = types.KeyboardButton('Serrería')
        tarongers = types.KeyboardButton('Tarongers')
        turia = types.KeyboardButton('Túria')
        tomas = types.KeyboardButton('Tomás y Valiente')
        torre = types.KeyboardButton('Torre del Virrei')
        torrent = types.KeyboardButton('Torrent')
        torrent_av = types.KeyboardButton('Torrent Avinguda')
        tossal = types.KeyboardButton('Tossal del Rei')
        transits = types.KeyboardButton('Trànsits')
        tvv = types.KeyboardButton('TVV')
        upv = types.KeyboardButton('Universitat Politècnica')
        sud = types.KeyboardButton('València Sud')
        estelles = types.KeyboardButton('Vicent Andrés Estellés')
        zaragossa = types.KeyboardButton('Vicente Zaragozá')
        villanova = types.KeyboardButton('Villanueva de Castellón')
        xativa = types.KeyboardButton('Xàtiva')
        markup.add(alameda,albalat,alberic,alboraya,alboraya_1,alfauir,alginet,almassera,amistat,guimera,aragon,ausias,cid,ayora,bailen,betera,benaguasil_1,benaguasil_2,benicalap,beniferri,benimaclet,benimamet,benimodo,burjassot,godella,campament,campanar,campus,cantereria,carlet,colon,vedat,lluch,clot,empalme,entrepins,espioca,llevant,eugenia,facultats,faitanar,fira,florista,foios,font,francesc,fuente,garbi,godella,grau,horta,jesus,alcudia,eliana,cadena,cayada,carrasca,coma,cova,granja,marina,farnals,vallbona,presa,vallesa,arenes,carolines,llarga,lliria,machado,manises,maritim,marina,marxalenes,mas,masia,masies,massalaves,massamagrell,massarrojos,mediterrani,meliana,mislata,almassil,moncada,montesol,montortal,museros,octubre,omet,orriols,paiporta,congresos,paterna,patraix,picanya,picassent,espanya,fusta,primat,quart,rafel,realon,reus,riba,rocafort,rosas,safranar,sagunt,salt,sant_i,sant_j,sant_m,sant_r,sant_g,sant_ri,seminari,serreria,tarongers,turia,tomas,torre,torrent,torrent_av,tossal,transits,tvv,upv,sud,estelles,zaragossa,villanova,xativa)
        bot.send_message(message.chat.id, "Elige estación de destino:", reply_markup=markup)

        bot.register_next_step_handler(message, step_destino)
    except Exception as e:
        bot.reply_to(message, 'Fallo al empoderar')

def step_destino(message):
    code = ""
    salida = str(message.text)
    if salida == 'Alameda':
        code = '14'
    elif salida == 'Albalat dels Sorells':
        code = '5'
    elif salida == 'Alberic':
        code = '36'
    elif salida == 'Alboraya-Palmaret':
        code = '10'
    elif salida == 'Alboraya-Peris Aragó':
        code = '9'
    elif salida == 'Alfauir':
        code = '128'
    elif salida == 'Alginet':
        code = '43'
    elif salida == 'Almàssera':
        code = '8'
    elif salida == 'Amistat-Casa de Salud':
        code = '23'
    elif salida == 'Àngel Guimerà':
        code = '17'
    elif salida == 'Aragón':
        code = '24'
    elif salida == 'Ausiàs March':
        code = '42'
    elif salida == 'Av. del Cid':
        code = '18'
    elif salida == 'Ayora':
        code = '22'
    elif salida == 'Bailén':
        code = '109'
    elif salida == 'Bétera':
        code = '107'
    elif salida == 'Benaguasil 1r':
        code = '69'
    elif salida == 'Benaguasil 2n':
        code = '70'
    elif salida == 'Benicalap':
        code = '97'
    elif salida == 'Beniferri':
        code = '54'
    elif salida == 'Benimaclet':
        code = '12'
    elif salida == 'Benimàmet':
        code = '57'
    elif salida == 'Benimodo':
        code = '40'
    elif salida == 'Burjassot':
        code = '72'
    elif salida == 'Burjassot - Godella':
        code = '73'
    elif salida == 'Campament':
        code = '59'
    elif salida == 'Campanar':
        code = '53'
    elif salida == 'Campus':
        code = '103'
    elif salida == 'Canterería':
        code = '56'
    elif salida == 'Carlet':
        code = '41'
    elif salida == 'Colón':
        code = '15'
    elif salida == 'Col·legi El Vedat':
        code = '50'
    elif salida == 'Dr. Lluch':
        code = '83'
    elif salida == 'El Clot':
        code = '108'
    elif salida == 'Empalme':
        code = '55'
    elif salida == 'Entrepins':
        code = '65'
    elif salida == 'Espioca':
        code = '45'
    elif salida == 'Estadi del Llevant':
        code = '130'
    elif salida == 'Eugenia Viñes':
        code = '81'
    elif salida == 'Facultats':
        code = '13'
    elif salida == 'Faitanar':
        code = '200'
    elif salida == 'Fira València':
        code = '106'
    elif salida == 'Florista':
        code = '99'
    elif salida == 'Foios':
        code = '6'
    elif salida == 'Font Almaguer':
        code = '44'
    elif salida == 'Francesc Cubells':
        code = '122'
    elif salida == 'Fuente del Jarro':
        code = '62'
    elif salida == 'Garbí':
        code = '98'
    elif salida == 'Godella':
        code = '74'
    elif salida == 'Grau - Canyamelar':
        code = '123'
    elif salida == 'Horta Vella':
        code = '80'
    elif salida == 'Jesús':
        code = '25'
    elif salida == 'L\'Alcúdia':
        code = '39'
    elif salida == 'L\'Eliana':
        code = '67'
    elif salida == 'La Cadena':
        code = '85'
    elif salida == 'La Canyada':
        code = '63'
    elif salida == 'La Carrasca':
        code = '88'
    elif salida == 'La Coma':
        code = '111'
    elif salida == 'La Cova':
        code = '183'
    elif salida == 'La Granja':
        code = '101'
    elif salida == 'La Marina':
        code = '84'
    elif salida == 'La Pobla de Farnals':
        code = '2'
    elif salida == 'La Pobla de Vallbona':
        code = '68'
    elif salida == 'La Presa':
        code = '184'
    elif salida == 'La Vallesa':
        code = '64'
    elif salida == 'Les Arenes':
        code = '82'
    elif salida == 'Les Carolines/Fira':
        code = '58'
    elif salida == 'Ll. Llarga - Terramelar':
        code = '114'
    elif salida == 'Llíria':
        code = '71'
    elif salida == 'Machado':
        code = '11'
    elif salida == 'Manises':
        code = '119'
    elif salida == 'Marítim - Serrería':
        code = '115'
    elif salida == 'Marina Reial Joan Carles I':
        code = '126'
    elif salida == 'Marxalenes':
        code = '95'
    elif salida == 'Mas del Rosari':
        code = '110'
    elif salida == 'Masia de Traver':
        code = '185'
    elif salida == 'Masies':
        code = '79'
    elif salida == 'Massalavés':
        code = '37'
    elif salida == 'Massamagrell':
        code = '3'
    elif salida == 'Massarrojos':
        code = '76'
    elif salida == 'Mediterrani':
        code = '127'
    elif salida == 'Meliana':
        code = '7'
    elif salida == 'Mislata':
        code = '20'
    elif salida == 'Mislata - Almassil':
        code = '21'
    elif salida == 'Moncada - Alfara':
        code = '77'
    elif salida == 'Montesol':
        code = '66'
    elif salida == 'Montortal':
        code = '38'
    elif salida == 'Museros':
        code = '4'
    elif salida == 'Nou d\'Octubre':
        code = '19'
    elif salida == 'Omet\'Orriols':
        code = '46'
    elif salida == 'Paiporta':
        code = '129'
    elif salida == 'Palau de Congressos':
        code = '100'
    elif salida == 'Paterna':
        code = '60'
    elif salida == 'Patraix':
        code = '26'
    elif salida == 'Picanya':
        code = '32'
    elif salida == 'Picassent':
        code = '47'
    elif salida == 'Pl. Espanya':
        code = '51'
    elif salida == 'Pont de Fusta':
        code = '92'
    elif salida == 'Primat Reig':
        code = '91'
    elif salida == 'Quart de Poblet':
        code = '117'
    elif salida == 'Rafelbunyol':
        code = '1'
    elif salida == 'Realón':
        code = '49'
    elif salida == 'Reus':
        code = '94'
    elif salida == 'Riba-roja de Túria':
        code = '186'
    elif salida == 'Rocafort':
        code = '75'
    elif salida == 'Rosas':
        code = '120'
    elif salida == 'Safranar':
        code = '27'
    elif salida == 'Sagunt':
        code = '93'
    elif salida == 'Salt de l\'Aigua':
        code = '118'
    elif salida == 'Sant Isidre':
        code = '28'
    elif salida == 'Sant Joan':
        code = '102'
    elif salida == 'Sant Miquel dels Reis':
        code = '131'
    elif salida == 'Sant Ramon':
        code = '48'
    elif salida == 'Santa Gemma - Parc Científic UV':
        code = '113'
    elif salida == 'Santa Rita':
        code = '61'
    elif salida == 'Seminari - CEU':
        code = '78'
    elif salida == 'Serrería':
        code = '86'
    elif salida == 'Tarongers':
        code = '87'
    elif salida == 'Túria':
        code = '52'
    elif salida == 'Tomás y Valiente':
        code = '112'
    elif salida == 'Torre del Virrei':
        code = '201'
    elif salida == 'Torrent':
        code = '33'
    elif salida == 'Torrent Avinguda':
        code = '34'
    elif salida == 'Tossal del Rei':
        code = '132'
    elif salida == 'Trànsits':
        code = '96'
    elif salida == 'TVV':
        code = '105'
    elif salida == 'Universitat Politècnica':
        code = '89'
    elif salida == 'València Sud':
        code = '30'
    elif salida == 'Vicent Andrés Estellés':
        code = '104'
    elif salida == 'Vicente Zaragozá':
        code = '90'
    elif salida == 'Villanueva de Castellón':
        code = '35'
    elif salida == 'Xàtiva':
        code = '16'
    else:
        bot.reply_to(message, 'Fallo al seleccionar la estación')

    code_destino = code

    time_format = get_time().split(" ")
    fecha = time_format[0]
    hora = time_format[1]
    html = get_html(code_salida,fecha,code_destino,hora)
    response = parse_html(html)
    reply = ""
    for r in range(len(response)):
        reply += str(response[r]['description']) +"\n\n"
        if response[r]['duracion'] is not '':
            reply += "Duración del trayecto " + str(response[r]['duracion'] + "\n\n")
    bot.send_message(message.chat.id,reply)
    global rutas
    rutas.append(reply)
    bot.register_next_step_handler(message, step_guardar)

def step_guardar(message):
    global rutas
    rutas.append(message.text)

bot.polling()
