#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

template = """[connection]
id=%(vpn_type)s-%(name)s
uuid=%(uuid_string)s
type=vpn
permissions=user:dirlt:;
autoconnect=false
timestamp=%(create_ts)d

[vpn]
service-type=org.freedesktop.NetworkManager.%(vpn_type)s
gateway=%(domain)s
require-mppe=yes
user=dirtysalt
password-flags=0

[vpn-secrets]
password=%(password)s

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
method=auto
"""

password = 'youwillnevergetit'

domain_confs = (
    ('jp', 4),
    ('us', 6),
    ('tw', 1),
    ('hk', 3),
    ('sg', 2),
    ('uk', 1)
)

import uuid
import time

# then find NetworkManager and kill it
# ubuntu will restart NetworkManager and reload these generated configuration files

for (region, count) in domain_confs:
    for idx in range(count):
        index = idx + 1
        for vpn_type, vpn_index in (('pptp', 'p1'),('l2tp', 'p2')):
            file_prefix = '/etc/NetworkManager/system-connections/'
            file_path = file_prefix + 'vpncloud-%s-%s-%d' % (vpn_type, region, index)
            with open(file_path, 'w') as fh:
                uuid_string = str(uuid.uuid4())
                create_ts = int(time.time())
                name = '%s%d' % (region, index)
                domain = '%s.%s.jumpko.com' % (vpn_index, name)
                data = template % (locals())
                fh.write(data)
