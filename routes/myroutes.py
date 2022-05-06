from config import app

@app.get('/home')
def greetnow():
    return "This is home page...Hi How arey you?"

@app.get('/sample')
def fun():
    return " This is a sample page"