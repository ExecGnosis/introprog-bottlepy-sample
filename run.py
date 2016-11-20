# -*- coding: cp1252 -*-.

from bottle import route, run, response, request, template, static_file, error
from datetime import date
import hashlib

#Static Files Routing
@route('/image/<filename>')
def server_static(filename):
    return static_file(filename, root='./img/', mimetype="image/png")

@route('/style/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')

#General Routing
@route('/')
def index():
    videoFile = open("data/video.txt","r")
    videoCode = videoFile.readline()
    videoCode = 'https://www.youtube.com/embed/' + videoCode[videoCode.index("?v=")+3:]
    videoFile.close()

    if permissionCheck() == True:
        return template('index',username="Administrador",videoCode=videoCode)
    else:
        return template('index',username=None,videoCode=videoCode)

#Theme
@route('/materia/<num:int>')
def materia(num):
    if permissionCheck() == True:
        if num==1:
            tmpText = '''
            Confira no vídeo acima tudo sobre o signo mais incrível do zodíaco! Dizem que os taurinos costumam ser ótimos professores e programadores melhores ainda.
            '''
            return template('materia',username="Administrador",title="Papo Astral - Touro e sua Essência",type=1,themeText=tmpText,videoURL="0YqGRGxJ_mQ",imgName=0)
        elif num==2:
            tmpText = '''
            No mundo da tecnologia aqueles que correm atrás das novidades são os que se destacam.
            Nessa descrição se enquadram os taurinos e arianos.
            Ainda na casa da excelência, aqueles que tem uma tendência maior de conhecimento acerca de diversas áreas, como os virginianos se sobressaem em vista dos outros signos do zodíaco.
            '''
            return template('materia',username="Administrador",title="Tecnologia e o Zodíaco",type=2,themeText=tmpText,videoURL=0,imgName="tech.jpg")
    else:
        if num==1:
            tmpText = '''
            Confira no vídeo acima tudo sobre o signo mais incrível do zodíaco! Dizem que os taurinos costumam ser ótimos professores e programadores melhores ainda.
            '''
            return template('materia',username=None,title="Papo Astral - Touro e sua Essência",type=1,themeText=tmpText,videoURL="0YqGRGxJ_mQ",imgName=0)
        elif num==2:
            tmpText = '''
            No mundo da tecnologia aqueles que correm atrás das novidades são os que se destacam.
            Nessa descrição se enquadram os taurinos e arianos.
            Ainda na casa da excelência, aqueles que tem uma tendência maior de conhecimento acerca de diversas áreas, como os virginianos se sobressaem em vista dos outros signos do zodíaco.
            Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum justo ex, interdum eget tincidunt vitae, ullamcorper sodales nisi. Aliquam finibus, felis vitae cursus faucibus, felis felis cursus purus, eu laoreet nisi quam non elit. In sed tempor turpis. Sed id ultrices dolor, a varius turpis. Donec mauris sapien, molestie eu rutrum vitae, maximus vel enim. Morbi mi nunc, facilisis vel elementum non, lacinia et dui. Proin consequat vestibulum imperdiet. Etiam faucibus risus id condimentum dapibus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce varius elit vel turpis tincidunt, id consectetur libero sollicitudin. Aliquam erat volutpat. Duis eleifend nisl quis dolor scelerisque, mollis fermentum justo porta. Nulla rutrum mollis nibh, in auctor erat maximus sit amet. Integer sed nunc quis velit dapibus maximus nec eu tellus. Integer id sapien vel nisi fringilla congue.
            Sed feugiat varius ultrices. Curabitur ac enim vestibulum, faucibus justo sed, lobortis odio. Donec neque lacus, pharetra nec convallis in, accumsan et risus. Fusce turpis nisi, bibendum eget diam et, sodales fermentum augue. Nulla lobortis dui ac tellus ultrices, in pellentesque magna porttitor. In nec purus ut purus lobortis sollicitudin. Suspendisse aliquet vehicula elit et imperdiet. Ut eget metus iaculis, maximus arcu in, euismod magna. Curabitur at sem pulvinar, suscipit purus ac, imperdiet dui. In egestas mauris dolor, sit amet elementum lacus volutpat a.
            Fusce eget maximus dolor. Aenean sagittis, ante congue elementum venenatis, turpis enim bibendum odio, quis ornare lorem magna at urna. Fusce malesuada augue in consectetur elementum. Phasellus malesuada purus orci, nec gravida sem fringilla non. Nulla et auctor lectus. Mauris ante lacus, commodo eget bibendum vel, lobortis nec nunc. Sed convallis faucibus massa id lacinia. Suspendisse convallis egestas lacinia. Nunc venenatis elit vitae malesuada semper. Sed tincidunt purus vitae lorem elementum accumsan.
            Nullam id nunc nisi. Maecenas malesuada feugiat accumsan. Sed tincidunt magna et justo ultricies pharetra. Curabitur a felis arcu. Sed vel facilisis eros. Nulla sit amet finibus tellus. Nulla facilisi. Pellentesque lacinia consectetur massa eget viverra. Mauris aliquet erat vitae ullamcorper interdum. Donec eget convallis mauris, in aliquam metus. Aenean sollicitudin non tellus vel tristique. In vitae arcu eu sapien lobortis porta. Proin metus ipsum, placerat eget enim non, fermentum tempor sem. Aliquam accumsan sem semper, tincidunt metus at, tempus ex. Integer ut massa porta, imperdiet leo eget, sodales nisi.
            Nullam tempor ornare tellus, at lacinia enim rutrum vitae. Sed quis ante egestas, placerat purus a, molestie est. Aliquam vestibulum est ipsum, eu pellentesque dui tincidunt nec. Sed ut lacus id velit faucibus maximus eu eu leo. Quisque nec pharetra lorem, ut dictum dolor. Donec ornare ex nec tellus congue, quis vestibulum augue bibendum. Vivamus felis purus, pellentesque sed tristique id, eleifend id ligula. In egestas nulla non quam placerat condimentum. Praesent et placerat urna. Aenean blandit ornare nisl sed accumsan. Ut sit amet tempus elit. Nulla finibus accumsan neque vitae aliquam. Proin lorem urna, congue non dolor a, scelerisque semper metus.
            Cras vel felis magna. Vivamus efficitur urna vitae lorem tristique, at feugiat mi consequat. Etiam laoreet pharetra sem, quis posuere orci rhoncus et. Sed cursus condimentum ullamcorper. Mauris in volutpat mi. Aliquam egestas, ex vitae cursus gravida, dolor ipsum congue velit, sit amet consectetur odio ante vel dolor. Aliquam at felis a tortor placerat vestibulum ut ac ipsum. Vivamus eleifend lobortis egestas. Etiam eu fermentum tortor. Mauris dui ligula, pulvinar quis vulputate ut, congue at augue. Morbi blandit libero a dolor sollicitudin eleifend quis eget risus. Integer sed eros fermentum, tristique nisi sed, aliquam mi. Morbi hendrerit iaculis eleifend. Nunc rutrum posuere nisi cursus sagittis. Nam sodales cursus massa, et ornare diam pretium et.
            Nulla blandit interdum blandit. Phasellus sollicitudin eu massa ut semper. Nullam eu gravida nibh. Morbi in elit lacus. Curabitur vel iaculis quam. Duis ac orci quam. Nullam cursus sollicitudin vulputate. Quisque tempus scelerisque sem, et malesuada est viverra vel.
            Nunc commodo magna at venenatis ornare. Pellentesque sit amet urna egestas, porta quam in, faucibus sem. In non arcu orci. Mauris euismod neque orci, eu pharetra tellus venenatis ut. Pellentesque egestas id quam nec scelerisque. In volutpat venenatis nunc, vel tempus velit pulvinar in. Maecenas elementum, tortor et vehicula vestibulum, orci velit porttitor justo, molestie imperdiet sem nisl a tortor. Cras eget magna sit amet justo posuere egestas. Suspendisse libero sem, suscipit eget odio ac, efficitur feugiat odio. Etiam dignissim egestas lectus eu egestas. Vivamus a sapien eu dui lacinia aliquet.
            Vivamus porta eget ligula quis convallis. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc rhoncus risus leo, in venenatis odio aliquet eu. Nulla placerat massa eu purus commodo, sed malesuada massa venenatis. Duis mattis justo in posuere sagittis. Sed in consequat arcu, sed rutrum sem. Cras ut consectetur tortor. Etiam quis eleifend augue. Vestibulum porttitor sodales felis, at faucibus orci porttitor at. Nulla in tellus consectetur enim ultricies sagittis vel eleifend orci.
            Sed id ipsum at felis eleifend ultrices ut ac lorem. Nullam quis semper lorem. Nam maximus nibh ante, vitae mattis nisl ultricies porttitor. Morbi auctor, lorem vel feugiat varius, libero eros auctor nisi, a laoreet mi quam vehicula quam. Nunc porta, lectus sit amet facilisis bibendum, sem erat ultrices urna, ac aliquet neque neque non neque. Cras iaculis orci a est hendrerit euismod. Nullam tristique pretium mauris sed aliquam. Pellentesque semper sem nec enim semper, vel maximus libero placerat. Sed tortor lorem, varius ut risus et, imperdiet maximus lorem. Pellentesque vitae risus lacinia, euismod ipsum at, fermentum leo. Nullam mollis tempor augue in varius. Nam aliquam turpis at dui elementum, id vehicula odio gravida. Etiam vitae nibh feugiat, sagittis nisl finibus, venenatis augue. Aenean gravida, leo eget pulvinar tempor, leo orci commodo leo, a mollis nibh enim vitae libero. Praesent tincidunt, orci at volutpat dictum, leo nulla suscipit tortor, id condimentum erat est quis ligula.
            Suspendisse sit amet massa egestas, porta quam sed, eleifend sapien. Integer id vestibulum justo. Sed vitae suscipit dolor, sit amet consequat dui. Fusce facilisis venenatis felis. Aliquam erat volutpat. Aliquam consequat elementum tortor, vel semper ipsum mattis quis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent luctus ultrices lectus, eget maximus urna aliquet at. Nunc et neque porttitor, malesuada felis ut, consectetur est. Morbi eget dapibus arcu.
            Vestibulum ac tincidunt nisi, eu posuere arcu. Pellentesque erat justo, aliquet eget vulputate et, bibendum et orci. Ut dignissim tellus id justo mattis, non egestas est varius. Quisque ultrices ante erat, a aliquam risus imperdiet sagittis. Sed vulputate mauris at ligula hendrerit ultrices. Sed imperdiet ligula et quam pretium faucibus. Etiam blandit, justo sed maximus malesuada, leo eros convallis enim, blandit vestibulum justo ex a ligula. Quisque porta aliquam neque at maximus.
            Nunc pulvinar ex nec nunc rhoncus, vel congue lorem semper. Nulla eget arcu at magna aliquet rhoncus a ut eros. Cras ac diam tincidunt, accumsan libero non, aliquet odio. Pellentesque rutrum commodo massa. Mauris euismod faucibus pretium. Nam dignissim nisi et tortor lacinia, quis interdum velit mollis. Proin eget consectetur neque. Nam mi diam, volutpat a nisi a, venenatis vehicula lectus. Pellentesque consectetur mollis enim ac consequat. Donec maximus hendrerit sapien, nec consequat augue semper quis. Nullam in orci ultricies lectus sodales auctor a sed massa. Curabitur dapibus hendrerit tincidunt. Interdum et malesuada fames ac ante ipsum primis in faucibus. Maecenas non velit efficitur metus tincidunt tempus. Phasellus dapibus molestie nunc suscipit pellentesque. Nullam tincidunt ligula id sem pellentesque auctor.
            Morbi nisl tortor, aliquet sit amet nibh in, ultricies ornare mauris. Mauris sed faucibus risus, eu semper nisl. Vivamus commodo felis quis rutrum dictum. Proin mattis sed ligula sit amet auctor. Aliquam sed nunc facilisis, consectetur neque sed, iaculis velit. Aenean bibendum elementum est, ut vestibulum enim commodo id. Etiam iaculis convallis viverra. Proin efficitur posuere massa ac dapibus. Vestibulum auctor ac mi eu consectetur. Aliquam erat volutpat. Nam bibendum tellus et leo auctor interdum. Sed non faucibus ante.
            Suspendisse semper congue sem, at ultrices nisi porttitor ut. Integer enim arcu, sagittis sed laoreet in, venenatis sed ante. Quisque feugiat hendrerit hendrerit. Fusce posuere in lacus id convallis. Fusce rhoncus nisi ipsum, sed ultricies urna pulvinar sed. Maecenas pulvinar aliquet diam sit amet convallis. Donec ut feugiat augue.
            Donec efficitur ipsum a libero accumsan, nec eleifend mauris vulputate. Maecenas ullamcorper, mi sit amet auctor congue, lorem arcu lacinia erat, posuere sollicitudin tortor elit in erat. Donec molestie ipsum magna, vitae semper risus gravida eu. Sed ac felis id sem pellentesque gravida. Proin sit amet nunc finibus, euismod odio sit amet, rutrum metus. Quisque at vehicula massa, eu venenatis neque. Fusce bibendum dui in nunc efficitur, et semper nulla lacinia. Vestibulum vitae turpis in neque venenatis porta eu vel metus. Nunc nec accumsan massa.
            Aenean eu sagittis nunc, eu lacinia eros. Suspendisse nec vulputate sem. Morbi quis velit ac purus blandit pretium. Suspendisse potenti. Pellentesque tincidunt leo vitae neque mollis, a lobortis velit semper. Cras tincidunt ipsum sapien, a feugiat urna vestibulum nec. Nulla feugiat leo ut feugiat sagittis. Fusce non commodo urna. Nullam laoreet mauris et varius tincidunt. Duis tincidunt ex lobortis nunc dictum, id scelerisque dolor pellentesque. Quisque eu justo viverra diam convallis fringilla.
            Donec venenatis pulvinar arcu in tempor. Maecenas at orci ligula. Nullam tincidunt sem dolor, vel suscipit tellus interdum elementum. Aenean pretium hendrerit sapien, nec mollis libero gravida vitae. Vivamus vel libero neque. Interdum et malesuada fames ac ante ipsum primis in faucibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas malesuada nisi lorem. Nunc a dui mauris. In vestibulum gravida erat, eu vestibulum est consectetur eget. Sed et nisl quis sem varius lacinia. Proin tempor bibendum nibh eu elementum.
            Aenean rutrum vulputate felis et ultrices. Maecenas eleifend, diam vitae congue cursus, sapien magna convallis massa, vel luctus quam mauris et quam. Praesent ut sem lobortis, viverra massa at, egestas nisi. Phasellus nec eros sem. Fusce facilisis dui quis placerat lobortis. Cras mattis nec magna id elementum. Nulla eu ex ac eros convallis lobortis. Etiam congue tortor eget gravida sollicitudin. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce lobortis nibh lacinia neque placerat imperdiet. Nulla ut tellus vitae leo vestibulum molestie. Curabitur ac erat semper, ultrices dolor a, fringilla mauris. Praesent vel enim quis justo sollicitudin vulputate a eget mauris. Nunc a ornare lorem.
            Integer pulvinar, libero vitae luctus aliquet, sapien enim tempor enim, sed dapibus leo arcu ac ligula. Donec non ultricies magna, vel dictum ante. Duis dictum odio a lacus tincidunt maximus. Duis ultricies, nisi sed malesuada blandit, est purus dapibus nibh, sit amet eleifend odio sapien sed lorem. Integer sed risus laoreet lacus tincidunt dictum a quis nisi. Pellentesque auctor dictum ex sed pellentesque. Sed nec dignissim lectus. Morbi consequat volutpat nunc, vitae imperdiet nisi consequat ut. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Suspendisse ac ligula tellus. 
            '''
            return template('materia',username=None,title="Tecnologia e o Zodíaco",type=2,themeText=tmpText,videoURL=0,imgName="tech.jpg")

#Horoscope
@route('/horoscopo/')
def horoscopo():
    if permissionCheck() == True:
        return template('horoscopo-principal',username="Administrador")
    else:
        return template('horoscopo-principal',username=None)

@route('/horoscopo/<sign>/')
def horoscopo(sign):
    today = str(date.today().day) + '-' + str(date.today().month) + '-' + str(date.today().year) + '.txt'
    try:
        signFile = open('data/resumo.txt', 'r')
        pass
    except Exception as e:
        signFile = None

    try:
        todayFile = open('data/' + sign + '/' + today, 'r')
        pass
    except Exception as e:
        todayFile = None

    if signFile!=None:
        descriptionFile = signFile.readlines()

        if sign=='aquarius':
            descriptionText = descriptionFile[1] + descriptionFile[2] + descriptionFile[3] + descriptionFile[4]
            formalName = "Aquário"
        elif sign=='aries':
            descriptionText = descriptionFile[7] + descriptionFile[8] + descriptionFile[9] + descriptionFile[10]
            formalName = "Áries"
        elif sign=='cancer':
            descriptionText = descriptionFile[13] + descriptionFile[14] + descriptionFile[15] + descriptionFile[16]
            formalName = "Câncer"
        elif sign=='capricorn':
            descriptionText = descriptionFile[19] + descriptionFile[20] + descriptionFile[21] + descriptionFile[22]
            formalName = "Capricórnio"
        elif sign=='gemini':
            descriptionText = descriptionFile[25] + descriptionFile[26] + descriptionFile[27] + descriptionFile[28]
            formalName = "Gêmeos"
        elif sign=='leo':
            descriptionText = descriptionFile[31] + descriptionFile[32] + descriptionFile[33] + descriptionFile[34]
            formalName = "Leão"
        elif sign=='libra':
            descriptionText = descriptionFile[37] + descriptionFile[38] + descriptionFile[39] + descriptionFile[40]
            formalName = "Libra"
        elif sign=='pisces':
            descriptionText = descriptionFile[43] + descriptionFile[44] + descriptionFile[45] + descriptionFile[46]
            formalName = "Peixes"
        elif sign=='sagittarius':
            descriptionText = descriptionFile[49] + descriptionFile[50] + descriptionFile[51] + descriptionFile[52]
            formalName = "Sagitário"
        elif sign=='scorpio':
            descriptionText = descriptionFile[55] + descriptionFile[56] + descriptionFile[57] + descriptionFile[58]
            formalName = "Escorpião"
        elif sign=='taurus':
            descriptionText = descriptionFile[61] + descriptionFile[62] + descriptionFile[63] + descriptionFile[64]
            formalName = "Touro"
        elif sign=='virgo':
            descriptionText = descriptionFile[67] + descriptionFile[68] + descriptionFile[69] + descriptionFile[70]
            formalName = "Virgem"

        if todayFile!=None:
            textDay = ''.join(todayFile.readlines()).encode('1252')
        else:
            textDay = "Seu Vênus está em Marte. Isso não influencia em nada na sua vida."

        if permissionCheck() == True:
            return template('horoscopo-specific',username="Administrador",signName=sign,signText=descriptionText,dayText=textDay,formalName=formalName)
        else:
            return template('horoscopo-specific',username=None,signName=sign,signText=descriptionText,dayText=textDay,formalName=formalName)
    else:
        return 'Procedimento n&atilde;o permitido, voc&ecirc; n&atilde;o deveria estar aqui.'

#Admin
@route('/admin/')
def admin():

    if permissionCheck() == True:
        return template('cpanel',username="Administrador",error=0)
    else:
        return template('admin',login_error=0)

@route('/admin/', method='POST')
def intranet():
    username = request.forms.get('user')
    password = request.forms.get('pass')

    if username=="Administrador" and password=="senha1234":
        m = hashlib.md5()
        m.update("Administrador".encode('utf-8'))
        m.update("senha1234".encode('utf-8'))

        response.set_cookie("session", m.hexdigest(), secret='1337', path='/')
        return template('cpanel',username=username,error=0)
    else:
        return template('admin',login_error=1)

#Operations
@route('/atualizar/',method='POST')
def atualizar():

    fullDate = request.forms.get('datepicker')
    signName = request.forms.get('signSelect')
    text = request.forms.get('dayText')
    video = request.forms.get('videoURL')

    if permissionCheck()==True:
        if fullDate!='' and text!='':
            signFile = open('data/' + signName + '/' + fullDate + '.txt', "w")
            signFile.write(text)
            signFile.close()
        elif fullDate=='' and video=='':
            return template('cpanel',username="Administrador",error=1)
        elif text=='' and video=='':
            return template('cpanel',username="Administrador",error=2)
        if video!='':
            videoFile = open("data/video.txt","w")
            videoFile.write(video)
            videoFile.close()
        return template('cpanel',username="Administrador",error=-1)
    else:
        return "Voc&ecirc; n&atilde;o deveria estar aqui."

@route('/logout/')
def logout():
    response.delete_cookie(key='session', secret='1337', path='/')
    return '<script>window.location="/";</script>'

#Error 404/405
@error(405)
@error(404)
def error404(error):
    if permissionCheck() == True:
        return template('error',username="Administrador")
    else:
        return template('error',username=None)

#Internal Functions
def permissionCheck():
    m = hashlib.md5()
    m.update("Administrador".encode('utf-8'))
    m.update("senha1234".encode('utf-8'))

    session = request.get_cookie("session", secret='1337')

    if session == m.hexdigest():
        return True
    else:
        return False

#Run Server
run(host='localhost', port=8081)
