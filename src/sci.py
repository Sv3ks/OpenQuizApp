# Socket Communication Interface

# SCI[0-3]  Server -> Client, sent during handshake

SCI = {
    0: b'ACCEPTED',                     #? Server accepts client
    1: b'DECLINED_CLOSED',              #? Server declines client, server is not open.
    2: b'DECLINED_FULL',                #? Server declines client, server's client limit is reached.
    3: b'DECLINED_BANNED_USERNAME',     #? Server declines client, client's username is banned.
    4: b'DECLINED_NAME_TAKEN',          #? Server declines client, client with equal username is connected to server.

    8: b'QUIZ_STARTING',                #? Sent to all clients when quiz is starting so SCI[9/10] can be sent.
    9: b'CLIENT_STAYING',               #? Sent when quiz starts to end the thread checking for SCI[10].
    10: b'CLIENT_LEAVING',              #? Client is leaving, sends message so server knows. Only sent before quiz starts.
}
