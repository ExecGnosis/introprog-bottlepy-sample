<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="/style/theme.css">
    <title>Horoscópia - Erro 404</title>
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

      <div id="error404">
        <h1 align="center">Erro 404!</h1>
        <h3 align="center">A p&aacute;gina requisitada n&atilde;o p&ocirc;de ser encontrada!</h3>
        <img src="/image/back-arrow.png" alt="Voltar" onclick="window.history.back();" />
      </div>
  </body>
</html>
