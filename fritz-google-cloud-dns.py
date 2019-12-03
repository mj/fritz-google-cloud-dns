#!/usr/bin/python3

import fritzconnection
from google.cloud import dns
import argparse
import logging

def update(zone, rr, ip):
    changes = zone.changes()
    changes.delete_record_set(rr)

    new_rr = zone.resource_record_set(
        rr.name,
        rr.record_type,
        rr.ttl,
        [ip],
    )
    changes.add_record_set(new_rr)
    changes.create()

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO, format= '[%(asctime)s] %(message)s')

    parser = argparse.ArgumentParser(description = 'Update zone entry with FRITZ!Box public address.')
    parser.add_argument('zone')
    parser.add_argument('name')

    args = parser.parse_args()

    fc = fritzconnection.FritzConnection(
        address = 'fritz.box',
    )
    ip = fc.call_action('WANIPConn', 'GetExternalIPAddress')['NewExternalIPAddress']

    name = args.name if args.name.endswith('.') else args.name + '.'
    client = dns.Client()

    zone = client.zone(args.zone)

    for rr in zone.list_resource_record_sets():
        if rr.name == name and rr.rrdatas != [ip]:
            logging.info('Updating ' + name + ' to ' + ip)
            update(zone, rr, ip)
