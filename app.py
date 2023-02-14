from flask import  Flask
app = Flask(__name__)

    # POSTS MOCK - simulação da página antes de criar o banco de dados, algo de mentira que utiliza para fazer testes
posts = [
    {

    },
    {
        
    }
]


@app.route("/")
def hello():
    return "Hello World!!!!"

@app.route("/pudim")
def pudim():
    return "<h1>eu gosto de pudim</h1>"



    