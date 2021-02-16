import json

import requests

nexus_oss_url = 'http://192.168.2.123:8081'


def get_status():
    url = f'{nexus_oss_url}/service/rest/v1/status'
    response = requests.get(url)
    print(f'nexus_oss_status: {response.status_code}')


def get_system_status():
    url = f'{nexus_oss_url}/service/rest/v1/status/check'
    response = requests.get(url, auth=('admin', 'password'))
    json_response = response.json()
    # json pretty print using json dumps
    print(json.dumps(json_response, indent=4, sort_keys=True))


# Health check endpoint that validates server can respond to read and write requests
def is_writable():
    url = f'{nexus_oss_url}/service/rest/v1/status/writable'
    response = requests.get(url, auth=('admin', 'password'))
    if response.status_code == 200:
        print('Nexus OSS is Available to service requests')


def main():
    get_status()
    get_system_status()
    is_writable()


if __name__ == '__main__':
    main()
