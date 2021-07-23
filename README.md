# address-microservice-fn-js
This microservice to transform address data for [form.io](https://form.io) components with [URL Data Source](https://help.form.io/userguide/form-components/#url)

## `api/eas/lookup`
Query EAS for list of addresses via partial address string. Example to be used for autocomplete.

### Query string parameters
* `search` search query to perform address lookup

* additional query parameters supported by [Socrata API](https://dev.socrata.com/docs/queries/)



## `api/eas/json`
Query and filter EAS data in JSON
### [Simple Filtering](https://dev.socrata.com/docs/filtering.html)

Example filter by `address`
```
$ curl https://<host>/api/eas/json?address=200%20MAIN%20ST
```
Example filter by `address`, `block`, and `lot`
```
$ curl https://<host>/api/eas/json?address=200%20MAIN%20ST&block=3739&lot=008
```

### [Queries](https://dev.socrata.com/docs/queries/)

Example query `address_number`, `address_number_suffix`, `street_name`, `street_type`, and `unit_number` with `address`, `block`, and `lot`
```
$ curl https://<host>/api/eas/json?$select=address,address_number,address_number_suffix,street_name,street_type,unit_number,block,lot,parcel_number&$where=address=%2777%20VAN%20NESS%20AVE%20%23100%27%20AND%20block%20=%270834%27%20AND%20lot=%27144%27
```


## Development notes
### Quickstart Guide
[Create a function in Azure with Python using Visual Studio Code](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python)
[Create a Python function in Azure from the command line](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python)

### Environment variables
[Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#environment-variables)
In Functions, `application settings`, such as service connection strings, are exposed as environment variables during execution. You can access these settings by declaring `import os` and then using, `setting = os.environ["setting-name"]`. See example of `local.settings.json` file at `local.settings.example.json`

### Generating requirements.txt
Currently Azure Python Functions [does not support pipenv](https://github.com/Azure/azure-functions-python-worker/issues/417). However we can run `pipenv lock --requirements` to produce a requirements file for the non-dev requirements and `pipenv lock --requirements --dev` to produce one for just the dev requirements.
sample usage:  
production
```
$ pipenv lock --requirements > requirements.txt
```
development
```
pipenv lock --requirements --dev > requirements-dev.txt
```

#### azure-functions-worker
DO NOT include azure-functions-worker in requirements.txt
The Python Worker is managed by Azure Functions platform
Manually managing azure-functions-worker may cause unexpected issues


