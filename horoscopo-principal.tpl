<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="/style/theme.css">
    <title>Horoscópia - Horóscopo do Dia</title>
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

      <div id="horoscopeContent" align="center">
        <h1>Horóscopo do Dia</h1>
        <h3>Selecione seu signo para ver o seu horóscopo de hoje!</h3>
        <a href="/horoscopo/aquarius/"><img src="/image/aquarius.png" alt="Aquário" /></a>
        <a href="/horoscopo/aries/"><img src="/image/aries.png" alt="Áries" /></a>
        <a href="/horoscopo/cancer/"><img src="/image/cancer.png" alt="Câncer" /></a>
        <a href="/horoscopo/capricorn/"><img src="/image/capricorn.png" alt="Capricórnio" /></a>
        <a href="/horoscopo/gemini/"><img src="/image/gemini.png" alt="Gêmeos" /></a>
        <a href="/horoscopo/leo/"><img src="/image/leo.png" alt="Leão" /></a>
        <a href="/horoscopo/libra/"><img src="/image/libra.png" alt="Libra" /></a>
        <a href="/horoscopo/pisces/"><img src="/image/pisces.png" alt="Peixes" /></a>
        <a href="/horoscopo/sagittarius/"><img src="/image/sagittarius.png" alt="Sagitário" /></a>
        <a href="/horoscopo/scorpio/"><img src="/image/scorpio.png" alt="Escorpião" /></a>
        <a href="/horoscopo/taurus/"><img src="/image/taurus.png" alt="Touro" /></a>
        <a href="/horoscopo/virgo/"><img src="/image/virgo.png" alt="Virgem" /></a>
      </div>
  </body>
</html>
