from . import indovina_numero
from . indovina_la_parola import IndovinaParola
import os


from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


__app_name = 'gamelibs'
__indovina_numero_cfg_path = os.path.join(settings.BASE_DIR,
                                          __app_name,
                                         'indovina_numero.cfg')
__html_template_head = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
</head>
'''

__html_template_body = '''
<body>

<h3>Indovina il Numero</h3>

<div class="container">
  <form action="/gioco/indovina_numero" method=GET>
    <label for="fname">|MESSAGGIO|</label>
    <input type="text" id="numero" name="numero" placeholder="Fai un tentativo ...">

    <input type="submit" value="Submit">
  </form>
</div>

</body>
'''


def indovina_numero_web(request):
    """
    Semplice vista per interfacciare il gioco di indovina il numero
    """
    try:
        with open(__indovina_numero_cfg_path, 'r') as f:
            numero = int(f.read())
    except:
        numero = indovina_numero.seleziona_numero_casuale()
        with open(__indovina_numero_cfg_path, 'w') as f:
            f.write('{}'.format(numero))

    if request.GET.get('numero'):
        tentativo = int(request.GET['numero'])
        _msg = '<span style="color:green;">{} è {} rispetto al numero da indovinare. </span>'
        if tentativo == numero:
            os.remove(__indovina_numero_cfg_path)
            return HttpResponse('<body><div class="container"><h3>Complimenti Hai indovinato</h3><p>Il numero era: {}</p></div></body>'.format(tentativo))
        if tentativo < numero:
            msg = _msg.format(tentativo, 'minore')
        elif tentativo > numero:
            msg = _msg.format(tentativo, 'maggiore')

        return HttpResponse(__html_template_head+__html_template_body.replace('|MESSAGGIO|', msg))
    else:
        return HttpResponse(__html_template_head+__html_template_body.replace('|MESSAGGIO|', ''))


def indovina_la_parola(request):
    try:
        with open(__indovina_parola_cfg_path, 'r') as f:
            parola = f.read()
    except:
        parola = IndovinaParola.get_parola_casuale()
        with open(__indovina_parola_cfg_path, 'w') as f:
            f.write('{}'.format(parola))

    '''... completare qui ....

    Considerazioni utili:
        piuttosto che print sarebbe utile che i metodi tornassero il messaggio con return
    '''
