from robyn import Robyn

app = Robyn(_file__)

@app.get("/hey bro")
def h(request):
    return "Hello, "

app.start(port=5080, host="0.0.0.0") # host is optional, defaults to 127.0.0.1

