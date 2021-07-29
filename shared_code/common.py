""" Common shared functions """
import json
import jsend
import azure.functions as func

def func_json_response(response, headers=None):
    """ json func_json_response """
    json_data = json.loads(response.text)

    if response.status_code == 200:
        func_response = json.dumps(jsend.success({"items": json_data}))
    else:
        func_response = json.dumps(json_data)

    func_status_code = response.status_code

    return func.HttpResponse(
        func_response,
        status_code=func_status_code,
        mimetype="application/json",
        headers=headers
    )
