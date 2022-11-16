import socket
import droid


def myip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ret = s.getsockname()[0]
    except BaseException as e:
        droid.toast(str(e))
        ret = "127.0.0.1"
    s.close()
    return ret
