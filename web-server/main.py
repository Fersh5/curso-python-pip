import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return '''
    <h1>Hola bienvenido a esta pagina</h1>
    <p>Este es un parrafo</p>
    '''


def run():
    store.get_categories()


if __name__=='__main__':
    run()
    