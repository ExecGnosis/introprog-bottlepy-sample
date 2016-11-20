<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <link href="https://fonts.googleapis.com/css?family=Pacifico" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

    <link rel="stylesheet" href="http://code.jquery.com/ui/1.9.0/themes/base/jquery-ui.css" />
    <script src="http://code.jquery.com/jquery-1.8.2.js"></script>
    <script src="http://code.jquery.com/ui/1.9.0/jquery-ui.js"></script>
    <script>
      $(function() {
        $( "#datepicker" ).datepicker({
          dateFormat: "d-m-yy",
          showOn: "button",
          buttonImage: "/image/calendar.gif",
          buttonImageOnly: true,
          buttonText: "Escolha uma data",
          minDate: 0,
          maxDate: +7
        });
      });
    </script>

    <link rel="stylesheet" type="text/css" href="/style/theme.css">
    <title>Horoscópia - Painel de Controle</title>
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
        <span id="topBarText"><span id="welcomeMessage">Bem-vindo, <b>{{username}}</b></span><a href="/logout/">Sair</a></span>
      </div>

      <div id="cpanel">
        <h1 align="center">Painel de Controle</h1>
        <div id="cpanelContent" align="center">
          <form action="/atualizar/" method="post">
            % if error==1:
            <div class="alert alert-danger" role="alert">Nenhuma data selecionada!</div>
            % elif error==2:
            <div class="alert alert-danger" role="alert">Nenhum texto escrito para o horóscopo do dia!</div>
            % elif error==-1:
            <div class="alert alert-success" role="alert">Dados atualizados com sucesso!</div>
            % end
            <h3>Hor&oacute;scopo do dia:</h3>

            <input name="datepicker" type="hidden" id="datepicker" size="30" style="cursor:pointer;">
            <span id="clearDate" alt="Limpar data" class="glyphicon glyphicon-remove" aria-hidden="true" style="cursor:pointer;" onclick="document.getElementById('datepicker').value = '';"></span>
            <select name="signSelect" class="form-control" id="signSelect">
              <option value="aquarius">Aquário</option>
              <option value="aries">Áries</option>
              <option value="cancer">Câncer</option>
              <option value="capricorn">Capricórnio</option>
              <option value="gemini">Gêmeos</option>
              <option value="leo">Leão</option>
              <option value="libra">Libra</option>
              <option value="pisces">Peixes</option>
              <option value="sagittarius">Sagitário</option>
              <option value="scorpio">Escorpião</option>
              <option value="taurus">Touro</option>
              <option value="virgo">Virgem</option>
            </select>
            <textarea name="dayText" class="form-control" rows="5" id="dayText" placeholder="Texto do horóscopo do dia..."></textarea>
            <h3>V&iacute;deo Patrocinado:</h3>
            URL do V&iacute;deo: <input name="videoURL" type="text" class="form-control" id="videoURL" placeholder="Exemplo: https://www.youtube.com/watch?v=d_HlPboLRL8" />
            <input id="sendAttForm" type="submit" class="btn" value="Atualizar Dados" />
          </form>
        </div>
      </div>
  </body>
</html>
