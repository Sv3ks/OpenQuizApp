# Socket Communication Interface

# SCI[0-3]  Server -> Client, sent during handshake

SCI = {
    0: b'ACCEPTED',                     #? Server accepts client
    1: b'DECLINED_CLOSED',              #? Server declines client, server is not open.
    #2: b'DECLINED_FULL'                #? Preserved for the future.
    #3: b'DECLINED_USERNAME'            #? Preserved for the future.

    9: b'CLIENT_STAYING',                #? Sent when quiz starts to end the thread checking for SCI[10].
    10: b'CLIENT_LEAVING',              #? Client is leaving, sends message so server knows. Only sent before quiz starts.
}
