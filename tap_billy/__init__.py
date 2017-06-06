#!/usr/bin/env python3

from decimal import Decimal

import argparse
import base64
import copy
import datetime
import json
import os
import sys
import time
import dateutil.parser

import backoff
import requests
import singer

import schemas

LOGGER = singer.get_logger()
SESSION = requests.Session()


BASE_URL = "https://api.billysbilling.com/v2"
CONFIG = {}

DEFAULT_STATE = {
    'invoice': {}
}

DEFAULT_START_DATE = '2016-08-01'

def giveup(error):
    LOGGER.error(error.response.text)
    response = error.response
    return not (response.status_code == 429 or
                response.status_code >= 500)

@backoff.on_exception(backoff.constant,
                      (requests.exceptions.RequestException),
                      jitter=backoff.random_jitter,
                      max_tries=5,
                      giveup=giveup,
                      interval=30)


def request(url, access_token, params):
    LOGGER.info("Making request: GET {} {}".format(url, params))
    headers = {'X-ACCESS-TOKEN': access_token}
    if 'user_agent' in CONFIG:
        headers['User-Agent'] = CONFIG['user_agent']

    req = requests.Request('GET', url, headers=headers, params=params).prepare()
    LOGGER.info("GET {}".format(req.url))
    resp = SESSION.send(req)

    if resp.status_code >= 400:
        LOGGER.error("GET {} [{} - {}]".format(req.url, resp.status_code, resp.content))
        resp.raise_for_status()

    return resp

def parse_datetime(date_time):
    parsed_datetime = dateutil.parser.parse(date_time)

    # the assumption is that the timestamp comes in in UTC
    return parsed_datetime.isoformat('T') + 'Z'



def sync_invoices(access_token):
    LOGGER.info('Syncing accounts.')

    start = time.time()
    response = request('{}/invoices'.format(BASE_URL), access_token, {})

    invoices = response.json().get('invoices', [])

    singer.write_records('invoices', invoices)


def do_sync(args):
     #pylint: disable=global-statement
    global DEFAULT_START_DATE
    state = DEFAULT_STATE

    with open(args.config) as config_file:
        config = json.load(config_file)
        CONFIG.update(config)

    missing_keys = []

    if 'access_token' not in config:
        missing_keys.append('access_token')
    else:
        access_token = config['access_token']

    if 'organization_id' not in config:
        missing_keys.append('organization_id')
    else:
        organization_id = config['organization_id']

    if len(missing_keys) > 0:
        LOGGER.fatal("Missing {}.".format(", ".join(missing_keys)))
        raise RuntimeError

    singer.write_schema('invoices',
                        schemas.invoice,
                        key_properties=["id"])

    sync_invoices(access_token)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--config', help='Config file', required=True)
    parser.add_argument(
        '-s', '--state', help='State file')

    args = parser.parse_args()

    do_sync(args)


if __name__ == '__main__':
    main()
