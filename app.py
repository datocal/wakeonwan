from flask import Flask, render_template, request
import socket, struct

macs = {
    'david_f09ba4b3-8363-46e1-9fb8-10feaeb27f8c': '2a:2a:2a:2a:2a:2a',
}

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/wake_on_wan')
def wake_on_wan():
    passcode = request.args['passcode']
    if passcode in macs:
        send_magic_packet(macs[passcode])
        return render_template('wake_ok.html')
    else:
        return render_template('wake_ko.html', code=passcode)


def send_magic_packet(mac):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(get_packet(mac), ("255.255.255.255", 9))
    s.close()


def get_packet(address):
    split_mac = str.split(address, ':')
    # Pack together the sections of the MAC address as binary hex
    hex_mac = struct.pack('BBBBBB', int(split_mac[0], 16),
                          int(split_mac[1], 16),
                          int(split_mac[2], 16),
                          int(split_mac[3], 16),
                          int(split_mac[4], 16),
                          int(split_mac[5], 16))
    return b'\xff' * 6 + hex_mac * 16


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
