from flask import Flask, render_template, redirect, url_for, request, flash
import requests


app =  Flask (__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

profiles = 12312



@app.route ('/desativar')
def desativar ():
    return render_template ('desativar.html')

@app.route ('/ativar')
def ativar():
    return render_template ('ativar.html')


@app.route ('/desativar_usuario', methods = ["GET", "POST"])
def desativar_usuario():
    usuario = request.form.get ('usuario')

    if request.method == "POST":
        user = str(usuario)
        bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGkuaW50ZWdyYWNhbyIsInZuU2VjcmV0IjoiNGZkOTYxNjNhOThhYzgxY2MxZDUxNjAxNzU4MjMxODAiLCJ1c2VyIjoiYXBpLmludGVncmFjYW8iLCJ1c2VySWQiOjUwMjIxNTg3LCJleHAiOjE3MTc0NTgwMzN9.JIrlJ7puPRoHUI8_ZZH5vq242kZCrF55OuL6cxtZjzo"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.delete("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/%s/byLogin" % user, headers=headers)
        if response.status_code == 200:
            flash ("Usuário desativado com sucesso!")
            
        else:
            flash ("Erro: Não foi possivel desativar!")

    return render_template ("desativar.html")

@app.route ('/ativar_usuario', methods = ["GET", "POST"])
def ativar_usuario():
    usuario = request.form.get ('usuario')

    if request.method == "POST":
        user = str(usuario)
        bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGkuaW50ZWdyYWNhbyIsInZuU2VjcmV0IjoiNGZkOTYxNjNhOThhYzgxY2MxZDUxNjAxNzU4MjMxODAiLCJ1c2VyIjoiYXBpLmludGVncmFjYW8iLCJ1c2VySWQiOjUwMjIxNTg3LCJleHAiOjE3MTc0NTgwMzN9.JIrlJ7puPRoHUI8_ZZH5vq242kZCrF55OuL6cxtZjzo"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.put("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/%s/byLogin" % user, headers=headers)
        if response.status_code == 200:
            flash ("Usuário ativo com sucesso!")

        else:
            flash ("Erro: Não foi possivel ativar")
            print(response.status_code)

    return render_template ("ativar.html")


@app.route ('/criar', methods = ["GET", "POST"])
def criar ():
    
    if request.method == "POST":
        
        bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGkuaW50ZWdyYWNhbyIsInZuU2VjcmV0IjoiNGZkOTYxNjNhOThhYzgxY2MxZDUxNjAxNzU4MjMxODAiLCJ1c2VyIjoiYXBpLmludGVncmFjYW8iLCJ1c2VySWQiOjUwMjIxNTg3LCJleHAiOjE3MTc0NTgwMzN9.JIrlJ7puPRoHUI8_ZZH5vq242kZCrF55OuL6cxtZjzo"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.post("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/create", headers=headers)
        
    return render_template ("criarusuario.html")

@app.route('/criar_usuario', methods = ["GET","POST"])
def criar_usuario ():
    
    if request.method == "POST":
        nome= request.form.get('nome')
        apelido = request.form.get('apelido')
        cpf= request.form.get('cpf')
        telefone = request.form.get('telefone')
        usuario = request.form.get('usuario')
        senha= request.form.get('senha')
        genero = request.form.get('genero')
        cidade=request.form.get('cidade')
        estado = request.form.get('estado')
        nacionalidade= request.form.get('nacionalidade')
        aniversario = request.form.get('aniversario')
        cnpj= request.form.get('cnpj')
        lista = [nome, apelido,cpf,telefone,usuario,senha,genero,cidade,estado,nacionalidade,aniversario,cnpj]
        print(lista)
    return render_template ('criarusuario.html')
    
    
    

        





app.run(host='0.0.0.0' , port=80, debug=True)