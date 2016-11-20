<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="/style/theme.css">
    <title>Horoscópia - Seu Portal de Astrologia</title>
  </head>
  <body>
      <div id="background"></div>

      <div id="topBar">
          <div class="logo">
            <a href="/" style="text-decoration:none">
              <img src="/image/logo.png" alt="99% originais, de propósito"  />
              <span>Horoscópia<span>
            </a>
          </div>
          % if username==None:
          <a href="/admin/" class="btn">Login</a>
          % else:
          <span id="topBarText"><span id="welcomeMessage">Bem-vindo, <a href="/admin/" style="margin-left:0px"><b>{{username}}</b></a></span><a href="/logout/">Sair</a></span>
          % end
      </div>

      <div id="myCarousel" class="carousel slide" data-ride="carousel" align="center">

      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>

      <div class="carousel-inner" role="listbox">
        <div class="item active first">
          <img src="/image/horoscopo_dia.png" alt="Horóscopo Diário">
          <div class="carousel-caption">
            <a href="/horoscopo/">
              <h1>Hoje</h1>
              <p>Veja aqui como vai ser seu dia!</p>
            </a>
          </div>
        </div>

        <div class="item second">
            <img src="/image/not_claudio.png" alt="Totally not Cláudio">
            <div class="carousel-caption">
              <a href="/materia/1">
                <h1>Touro</h1>
                <p>Confira aqui o vídeo da youtuber Carol Vaz tudo sobre os taurinos, sua essência e seus encantos!</p>
              </a>
            </div>
        </div>

        <div class="item third">
            <img src="/image/tech.png" alt="Horóscopo Diário">
            <div class="carousel-caption">
              <a href="/materia/2">
                <h2>Tecnologia</h2>
                <p>Venha ver quais os signos mais "antenados"!</p>
              </a>
            </div>
        </div>
      </div>
    </div>

    <div id="mainForm">
      <span id="content-1">
        <h1>Sobre N&oacute;s</h1>
        <p>
          Esta &eacute; uma p&aacute;gina de exemplo de uso do bottlepy, feita para ser um modelo de site de astrologia, para a disciplina de Introdu&ccedil;&atilde;o a Programa&ccedil;&atilde;o
          da UFRJ, ministrada pelo professor Cl&aacute;udio Miceli. Esta p&aacute;gina foi desenvolvida pelos alunos Ana Carvalho e Matheus Correia, e tem como principal foco entretenimento, j&aacute;
          que nenhum dos dois possui forma&ccedil;&atilde;o em astrologia, grande parte dos textos e recursos gerais aqui contidos foram retirados de outros sites especializados ou escritos em forma
          de s&aacute;tira
        </p>
        <img id="picture-2" src="/image/correia.png" /><img id="picture-1" src="/image/ana.png" />
      </span>

      <span id="content-2">
        <h1>V&iacute;deo Patrocinado</h1>
        <p>
          Confira abaixo um v&iacute;deo sobre astrologia ou assuntos adjacentes. Os v&iacute;deos s&atilde;o constantemente atualizados pelo administrador
        </p>
        <iframe width="70%" height="360" src="{{videoCode}}" frameborder="0"></iframe>
      </span>

    </div>

    <div id="footer">
      <div class="copyright">
        &copy; Copyright 2016 - UFRJ, todos os direitos reservados.
        <img src="/image/ufrj.png" />
      </div>
    </div>
  </body>
</html>
