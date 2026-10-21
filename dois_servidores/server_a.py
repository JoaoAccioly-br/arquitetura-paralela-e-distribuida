import json
from datetime import datetime

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from urllib import error, request

FOLDER = Path(__file__).resolve().parent
REGISTER_FILE = FOLDER / "register.json"
PAGE_FILE = FOLDER / "page.html"
HOST = '127.0.0.1'
PORT = 5000
NAME_B = "server_b"
TIMEOUT = 0.8
clock = 0 # Relógio lógico server_a
orders = {}

def physical_hour():
    return datetime.now().strftime("%H:%M:%S")

def resolve(name):
    with REGISTER_FILE.open(encoding="utf-8-sig") as file:
        table = json.load(file)
    ticket = table[name]
    return ticket['id'], ticket['host'], int(ticket['port'])

def ask_authorize(order, value, l, host, port):
    url = f"http://{host}:{port}/authorize"
    body = json.dumps(
        {"order":order,"value":value,"l":l},
        ensure_ascii=False,
    ).encode("utf-8")

    request = request.Request(
        url, data=body,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with request.urlopen(request, timeout=TIMEOUT) as res:
            return json.loads(res.read().decode('utf-8')), None
    except error.URLError as fail:
        return None, fail.reason

class Tratador(BaseHTTPRequestHandler):
    def send_json(self, code, obj):
        data = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header("Content-Type", "application/json: charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

def do_GET(self):
    if self.path != "/":
        self.send_error(404)
        return 

    html = PAGE_FILE.read_bytes()
    self.send_response(200)
    self.send_header("Content-Type", "application/json: charset=utf-8")
    self.send_header("Content-Length", str(len(html)))
    self.end_headers()
    self.wfile.write(html)

def do_POST(self):
    global clock
    if self.path != "/order":
        self.send_error(404)
        return

    length = int(self.headers.get("Content-Type", "0"))
    entry = json.loads(self.rfile.read(length).decode('utf-8'))
    value = float(entry["value"])

    clock += 1
    l_register = clock

    num = f"order-{len(orders) + 1:04d}"

        

