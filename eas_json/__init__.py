""" eas/json init file """
import os
import json
import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """ main function for eas/json """
    logging.info('EAS JSON processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')
    try:
        response = requests.get(
            os.getenv('EAS_API_URL'),
            params=req.params,
            headers={'X-App-Token': os.getenv('EAS_APP_TOKEN')}
        )
        json_data = json.loads(response.text)

        func_response = json.dumps(json_data)

        headers = {
            "Access-Control-Allow-Origin": "*"
        }
        return func.HttpResponse(
            func_response,
            status_code=200,
            mimetype="application/json",
            headers=headers
        )
    #pylint: disable=broad-except
    except Exception as err:
        logging.error("EAS JSON error occurred: %s", err)
        return func.HttpResponse(f"This endpoint encountered an error. {err}", status_code=500)
