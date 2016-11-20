<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="/style/theme.css">
    <title>Horoscópia - {{formalName}}</title>
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

      <div id="signContent" align="center">
        <h1>{{formalName}}</h1>
        <img src="/image/{{signName}}.png" />
        <h3>Descrição:</h3><span>{{signText}}</span>
        <h3>Sorte do dia:</h3><span>{{dayText}}</span>
        <img alt="{{formalName}}" src="/image/back-arrow.png" alt="Voltar" onclick="window.history.back();" style="cursor:pointer;" width="64" height="64" />
      </div>
  </body>
</html>
