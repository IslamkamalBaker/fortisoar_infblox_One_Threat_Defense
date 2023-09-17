import json
import requests

from connectors.core.connector import ConnectorError, get_logger

logger = get_logger('infoblox-bloxone-threat-defense')

error_msgs = {
    400: 'Bad/Invalid Request',
    401: 'Unauthorized: Invalid credentials or token provided failed to authorize',
    403: 'Access Denied',
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable'
}


class BloxOneThreatDefense:
    def __init__(self, config):
        if config.get('server_url'):
            self.server_url = config.get('server_url').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://{0}'.format(self.server_url)
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')
        self.headers = {'Authorization': 'Token {}'.format(self.api_key), 'Content-Type': 'application/json'}

    def make_rest_call(self, method, endpoint, data=None, params=None, headers=None):
        try:
            service_endpoint = '{0}{1}'.format(self.server_url, endpoint)
            logger.debug("Service URL: {0}".format(service_endpoint))
            logger.debug("API Request Payload: {0}".format(data))
            response = requests.request(method, service_endpoint, data=data, params=params, headers=self.headers,
                                        verify=self.verify_ssl)
            logger.debug("API Status Code: {}".format(response.status_code))
            logger.debug("API Response: {}".format(response.text))

            if response.ok:
                return response.json()
            else:
                logger.error("{0}".format(response.text))
                if error_msgs.get(response.status_code, response.text):
                    raise ConnectorError('{}'.format(error_msgs.get(response.status_code, response.text)))
                else:
                    raise ConnectorError("{0}".format(response.text))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def build_payload(params):
    items = params.get('items')
    if isinstance(items, str):
        items = items.split(',')
    payload = {
        'items': []
    }
    description_type = params.get('description_type')

    description = params.get('description')
    if description:
        payload.update({'items_described':[]})
    if description_type == 'Common':
        description = [{'item': item, 'description': params.get('description')} for item in items]
        payload.get('items_described').append(description)
    else:
        if description and isinstance(description, list):
            payload.get('items_described').extend(description)

    if items and isinstance(items, list):
        payload.update({'items': items})

    return payload


def add_item_into_named_list(config, params):
    try:
        params = {k: v for k, v in params.items() if v is not None and v != ''}
        bloxone = BloxOneThreatDefense(config)
        endpoint = "/api/atcfw/v1/named_lists/{id}/items".format(id=params.get('id'))
        paths = params.pop('path', '')
        if paths and isinstance(paths, str):
            paths = paths.split(',')
        payload = build_payload(params)
        if paths and isinstance(paths, list):
            payload.update({'fields': {'paths': paths}})
        return bloxone.make_rest_call('POST', endpoint, data=json.dumps(payload))
    except Exception as err:
        logger.error("{0}".format(err))
        raise Exception(err)


def remove_item_from_named_list(config, params):
    try:
        bloxone = BloxOneThreatDefense(config)
        endpoint = "/api/atcfw/v1/named_lists/{id}/items".format(id=params.get('id'))
        payload = build_payload(params)
        return bloxone.make_rest_call('DELETE', endpoint, data=json.dumps(payload))
    except Exception as err:
        logger.error("{0}".format(err))
        raise Exception(err)


def get_named_lists(config, params):
    try:
        bloxone = BloxOneThreatDefense(config)
        return bloxone.make_rest_call('GET', '/api/atcfw/v1/named_lists', params=params)
    except Exception as err:
        logger.error("{0}".format(err))
        raise Exception(err)


def get_specific_named_list(config, params):
    try:
        bloxone = BloxOneThreatDefense(config)
        endpoint = '/api/atcfw/v1/named_lists/{id}'.format(id=params.pop('id', ''))
        return bloxone.make_rest_call('GET', endpoint, params=params)
    except Exception as err:
        logger.error("{0}".format(err))
        raise Exception(err)

def dossier_source_lookup_by_target_type(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    endpoint = '/tide/api/services/intel/lookup/indicator/{0}'.format(params.get('type'))
    return bloxone.make_rest_call('GET', endpoint, params=params)
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err)

    
def dossier_lookup_job_status(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    endpoint = '/tide/api/services/intel/lookup/jobs/{0}'.format(params.get('jobid'))
    return bloxone.make_rest_call('GET', endpoint, params=params)
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err)
    
def dossier_lookup_job_returns(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    endpoint = '/tide/api/services/intel/lookup/jobs/{0}/{1}'.format(params.get('jobid'),"results")
    return bloxone.make_rest_call('GET', endpoint, params=params)
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err)    

    
def dossier_indicator_source(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    endpoint = '/tide/api/services/intel/lookup/sources'
    return bloxone.make_rest_call('GET', endpoint )
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err) 
    
def dossier_source_lookup_by_indicator_type(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    endpoint = '/tide/api/services/intel/lookup/sources/target/{0}'.format(params.get('target_type'))
    return bloxone.make_rest_call('GET', endpoint ,params=params)
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err) 
    

    
def dossier_indicator_type_lookup_based_on_source(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    endpoint = '/tide/api/services/intel/lookup/source/{0}/targets'.format(params.get('target_type'))
    return bloxone.make_rest_call('GET', endpoint , params=params)
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err) 
    
    
def dossier_lookup_job_status_by_specific_task(config, params):
  try:
    bloxone = BloxOneThreatDefense(config)
    endpoint = '/tide/api/services/intel/lookup/jobs/{0}/{1}/{2}'.format(params.get('job_id'),"tasks",params.get('task_id'))
    return bloxone.make_rest_call('GET', endpoint , params=params)
  except Exception as err:
    logger.error("{0}".format(err))
    raise Exception(err) 
    
    
def _check_health(config):
    try:
        bloxone = BloxOneThreatDefense(config)
        resp = get_named_lists(config, {})
        if resp:
            logger.info('connector available')
            return True
    except Exception as err:
        logger.error("{0}".format(err))
        raise Exception(err)



operations = {
  	'dossier_source_lookup_by_target_type': dossier_source_lookup_by_target_type,
  	'dossier_lookup_job_status': dossier_lookup_job_status,
  	'dossier_lookup_job_returns':dossier_lookup_job_returns,
  	'dossier_indicator_source' : dossier_indicator_source,
  	'dossier_source_lookup_by_indicator_type':dossier_source_lookup_by_indicator_type,
  	'dossier_indicator_type_lookup_based_on_source':dossier_indicator_type_lookup_based_on_source,
  	'dossier_lookup_job_status_by_specific_task':dossier_lookup_job_status_by_specific_task,
    'remove_item_from_named_list': remove_item_from_named_list,
    'add_item_into_named_list': add_item_into_named_list,
    'get_named_lists': get_named_lists,
    'get_specific_named_list': get_specific_named_list
}
