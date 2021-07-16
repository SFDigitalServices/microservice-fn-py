""" eas/lookup init file """
import os
import json
import logging
import requests

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """ main function for eas/lookup """

    logging.info('EAS Lookup processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')
    try:
        params  = req.params.copy()
        if params['search'] :
            params['$where'] = \
                "address like upper('{}%') AND parcel_number IS NOT NULL"\
                .format(params['search'])
            del params['search']

        response = requests.get(
            os.getenv('EAS_API_URL'),
            params=params,
            headers={'X-App-Token': os.getenv('EAS_APP_TOKEN')}
        )
        json_data = json.loads(response.text)

        func_response = json.dumps(json_data)

        headers = {
            "Cache-Control": "s-maxage=1, stale-while-revalidate, max-age={}"\
                .format(os.getenv('EAS_CACHE_MAX_AGE'))
        }

        return func.HttpResponse(
            func_response,
            status_code=200,
            mimetype="application/json",
            headers=headers
        )
    #pylint: disable=broad-except
    except Exception as err:
        logging.error("EAS Lookup error occurred: %s", err)
        return func.HttpResponse(f"This endpoint encountered an error. {err}", status_code=500)
