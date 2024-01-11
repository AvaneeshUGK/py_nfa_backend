from flask import Flask, request
import json
import requests 
import module
# import json

from flask_cors import CORS
import cfenv

function_names = {
    "GetSourceEvents":{
        "GET": "SourceHeaderDetails"
    },
    # "GetSupplierBids":{
    #     "GET":"itemdetails"
    # },
    "GetSupplierBidsv1":{
        "GET":"itemdetailsv1",
        # "GET":"itemdetailsv2",
        "POST":"itemdetailsv1post",
        "DELETE":"itemdelete",
        "PATCH":"edititem"
        # "GET":"itemdetailsv1post"
    },
    "postQuestion":{
        "POST":"itemdetailsquesPost",
        "DELETE":"questiondelete",
        "PATCH":"questionedit"
    },
    # "userEmail":{
    #     "GET":"userdata"
    # },
    # "GetLatestBids" : {
    #     "GET":"itemdetailsv2"
    # },
    "getVersions":{
        "GET":"itemdetails_v1"
    },
    "getPreview":{
        "GET":"previewDet"
    },
    "postDocument":{
        "POST":"documentUpload"
    }
}

app_env = cfenv.AppEnv()
port = app_env.port

app = Flask(__name__)

CORS(app, origins="*")

@app.route("/dev/<resource_name>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def call_function(resource_name):
    try:
        function_name = ''
        function =''
        querystring = json.loads(json.dumps(request.args))
        body_json = ""
        if request.data.decode("utf-8") != "":
            body_json = json.loads(request.data.decode("utf-8"))
        header = json.loads(json.dumps(dict(request.headers)))

        event = {
            "body-json": {},
            "params": {"path": {}, "querystring": {}, "header": {}},
            "stage-variables": {
                "schema": "einvoice_db_portal",
                "lambda_alias": "dev",
                "secreat": "test/einvoice/secret",
                "notification_email": "elipotest@gmail.com",
                "ocr_bucket_folder": "old-dev/",
                "cred_bucket": "file-bucket-emp",
            },
            "context": {
                "account-id": "",
                "api-id": "5ud4f0kv53",
                "api-key": "",
                "authorizer-principal-id": "",
                "caller": "",
                "cognito-authentication-provider": "",
                "cognito-authentication-type": "",
                "cognito-identity-id": "",
                "cognito-identity-pool-id": "",
                "http-method": "GET",
                "stage": "einvoice-v1",
                "source-ip": "49.207.50.252",
                "user": "",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                "user-arn": "",
                "request-id": "0dd29bb0-bd12-4dab-85d9-582a9b9ffbee",
                "resource-id": "39vsp4",
                "resource-path": "/rules",
            },
        }

        event["body-json"] = body_json
        event["params"]["querystring"] = querystring
        event["params"]["header"] = header

        if resource_name in function_names:
            function_name = function_names[resource_name][request.method]
            print(function_name)

        if hasattr(module, function_name):
            function = getattr(module, function_name)
        result = function(event=event,context=None)

        return result

    except AttributeError:
        return "Function not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)