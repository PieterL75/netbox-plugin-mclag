from utilities.choices import ChoiceSet

class LagTypeChoices(ChoiceSet):
    key = 'McLag.type'

    # a data channel part of the MC-LAG
    LAGTYPE_CHANNEL = 'channel'

    # control and management protocol channes of the MC-LAG
    LAGTYPE_ICCP = 'iccp'
    LAGTYPE_MCLAG = 'mclag'
    LAGTYPE_PEERLINK = 'peerlink'
    LAGTYPE_PEERKEEPALIVE = 'peerkeepalive'

    CHOICES = [
        (LAGTYPE_CHANNEL, 'Channel', 'green'),
        (LAGTYPE_ICCP, 'ICCP', 'blue'),
        (LAGTYPE_MCLAG, 'MC-LAG', 'blue'),
        (LAGTYPE_PEERLINK, 'Peer-Link', 'blue'),
        (LAGTYPE_PEERKEEPALIVE, 'Peer-Keepalive', 'blue'),
    ]