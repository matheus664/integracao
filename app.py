from flask import Flask, render_template, redirect, url_for, request, flash
import requests


app =  Flask (__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'





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
        bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGkuaW50ZWdyYWNhbyIsInZuU2VjcmV0IjoiZWY4YzM2MWM2ZTg1NjQ5YWQ5NWYwNTJjNTJlZmVmMjUiLCJ1c2VyIjoiYXBpLmludGVncmFjYW8iLCJ1c2VySWQiOjUwMjIxNTg3LCJleHAiOjE3MTc0MDE2ODl9.ha1K8RtVqa9uaSy-MQjSwWupLpCJekffWlcbV01Eb7Y"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.delete("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/%s/byLogin" % user, headers=headers)
        print (response.status_code)

        return (response.json())
    

@app.route ('/ativar_usuario', methods = ["GET", "POST"])
def ativar_usuario():
    usuario = request.form.get ('usuario')

    if request.method == "POST":
        user = str(usuario)
        bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYXRoZXVzLmxvIiwidm5TZWNyZXQiOiIzNzYyMTFjMzVhMGM5MmRiOWUxNzgwMDkxYTJiZGY2MyIsInVzZXIiOiJtYXRoZXVzLmxvIiwidXNlcklkIjo1MDE0NjYxMCwiZXhwIjoxNzE3MzkwMjIzfQ.-BV07LvUtnlFWeGdftspTY4ZuJTxtNiSAK66UPAuuHA"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.put("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/%s/byLogin" % user, headers=headers)
        if response.status_code == 200:
            flash ("Usuário ativo com sucesso!")

        else:
            flash ("Erro %s: Não foi possivel ativar" % response.status_code)

    return render_template ("ativar.html")
        





app.run(host='0.0.0.0' , port=80)