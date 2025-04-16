from robyn import Robyn

app = Robyn(_file__)

@app.get("")
def h(request):
    return "Helo, world"

app.start(port=500, host="0.0.0.0") # host is optional, defaults to 127.0.0.1