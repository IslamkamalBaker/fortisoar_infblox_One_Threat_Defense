# fortisoar_infblox_One_Threat_Defense
Update Exist connector to include Multiple Actions
## About the connector
Infoblox BloxOne Threat Defense provides foundational security that improves the efficiency of security operations centers by streamlining and automating threat response, reducing complexity, and enhancing the capabilities and performance of existing security investments.
<p>This document provides information about the Infoblox BloxOne Threat Defense Connector, which facilitates automated interactions, with a Infoblox BloxOne Threat Defense server using FortiSOAR&trade; playbooks. Add the Infoblox BloxOne Threat Defense Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Infoblox BloxOne Threat Defense.</p>
### Version information

Connector Version: 1.0.2


Authored By: Fortinet SE

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-infoblox-bloxone-threat-v2`

## Prerequisites to configuring the connector
- You must have the URL of Infoblox BloxOne Threat Defense server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Infoblox BloxOne Threat Defense server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Infoblox BloxOne Threat Defense</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td><br>
<tr><td>API Key<br></td><td><br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Named Lists<br></td><td>Retrieves information on all Named List objects or specific Named List objects for the account based on the input parameters you have specified.<br></td><td>get_named_lists <br/>Investigation<br></td></tr>
<tr><td>Get Specific Named List<br></td><td>Retrieves information on the specified Named List object for the account based on the ID of the named list and other input parameters you have specified.<br></td><td>get_specific_named_list <br/>Investigation<br></td></tr>
<tr><td>Add Item into Named List<br></td><td>Adds FQDN or IPv4 addresses into specified whitelists and blacklists for additional protection.<br></td><td>add_item_into_custom_list <br/>Miscellaneous<br></td></tr>
<tr><td>Remove Item From Named List<br></td><td>Remove FQDN or IPv4 addresses into specified whitelists and blacklists for additional protection.<br></td><td>remove_item_from_named_list <br/>Miscellaneous<br></td></tr>
<tr><td>Dossier Source Lookup by Target Type<br></td><td>Start a new Dossier lookup job for a specified indicator and source(s)<br></td><td>dossier_source_lookup_by_target_type <br/><br></td></tr>
<tr><td>Dossier Lookup Job Status<br></td><td>Returns status of a Dossier lookup job<br></td><td>dossier_lookup_job_status <br/><br></td></tr>
<tr><td>Dossier Lookup Job Returns<br></td><td>Returns results of a Dossier lookup job.<br></td><td>dossier_lookup_job_return <br/><br></td></tr>
<tr><td>Dossier Indicator Source Lookup<br></td><td>Returns a list of Dossier sources<br></td><td>dossier_indicator_source <br/><br></td></tr>
<tr><td>Dossier Source Lookup by Indicator Type<br></td><td>Returns sources that support queries for an indicator type.<br></td><td>dossier_source_lookup_by_indicator_type <br/><br></td></tr>
<tr><td>Dossier Indicator Type Lookup Based on Source<br></td><td>Return a list of indicator types supported by a given source.<br></td><td>dossier_indicator_type_lookup_based_on_source <br/><br></td></tr>
<tr><td>Dossier Lookup Job Status by Specific Task<br></td><td>Returns status of a single task in a Dossier lookup job.<br></td><td>dossier_lookup_job_status_by_specific_task <br/><br></td></tr>
</tbody></table>
### operation: Get Named Lists
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Filter<br></td><td>A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null. Note literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null’ Grouping operators (and, or, not, ()) are not supported.<br>
</td></tr><tr><td>Fields<br></td><td>Specify a CSV list of JSON tag names using which you want to retrieve Named List objects from Infoblox BloxOne Threat Defense.<br>
</td></tr><tr><td>Offset<br></td><td>The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0’.<br>
</td></tr><tr><td>Limit<br></td><td>The integer number of the resources to be returned in the response. The service might impose maximum value. If omitted the service might impose a default value.<br>
</td></tr><tr><td>Page Token<br></td><td>The service-defined string used to identify a page of resources. A null value indicates the first page.<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "results": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "created_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "items": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "policy_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "updated_time": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ]
</code><code><br>}</code>
### operation: Get Specific Named List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ID<br></td><td>The ID of the named list whose objects you want to retrieve from Infoblox BloxOne Threat Defense.<br>
</td></tr><tr><td>Fields<br></td><td>Specify a CSV list of JSON tag names using which you want to retrieve Named List objects from Infoblox BloxOne Threat Defense.<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "results": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "confidence_level": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "created_time": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "item_count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "items": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "items_described": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "item": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "policies": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "threat_level": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "type": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "updated_time": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>
### operation: Add Item into Named List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ID<br></td><td>Provide the custom named list object identifier.<br>
</td></tr><tr><td>Item<br></td><td>Provide CSV list of the FQDN or IPv4 addresses to define whitelists and blacklists for additional protection.<br>
</td></tr><tr><td>Description Type<br></td><td>Select description type one of the following.<br>
</td></tr><tr><td>Path<br></td><td>Provide the set of field mask paths.<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "success": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "code": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "status": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>
### operation: Remove Item From Named List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>ID<br></td><td>Provide the named list object identifier.<br>
</td></tr><tr><td>Item<br></td><td>Provide CSV list of the FQDN or IPv4 addresses to define whitelists and blacklists for additional protection.<br>
</td></tr><tr><td>Description Type<br></td><td>Select description type one of the following.<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Dossier Source Lookup by Target Type
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Value<br></td><td><br>
</td></tr><tr><td>Source<br></td><td>dns or ptr<br>
</td></tr><tr><td>Wait<br></td><td>whether to wait for the lookup to complete – true or false [defaults to false]<br>
</td></tr><tr><td>Type<br></td><td>Select description type one of the following.<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": ""
</code><code><br>}</code>
### operation: Dossier Lookup Job Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Job ID<br></td><td>Please Enter Job ID to Return Job <br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": ""
</code><code><br>}</code>
### operation: Dossier Lookup Job Returns
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Job ID<br></td><td>Please Enter Job ID to Return Results<br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "state": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "job_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "results": []
</code><code><br>}</code>
### operation: Dossier Indicator Source Lookup
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "acs": ""
</code><code><br>}</code>
### operation: Dossier Source Lookup by Indicator Type
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Target Type<br></td><td>Select Target type one of the following.<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Dossier Indicator Type Lookup Based on Source
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Target Type<br></td><td>For Example atp , dns ..etc<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Dossier Lookup Job Status by Specific Task
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Task ID<br></td><td>Please Enter Task ID which related to Job ID <br>
</td></tr><tr><td>Job ID<br></td><td>Please Enter Job ID <br>
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "state": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - infoblox-bloxone-threat-v2 - 1.0.2` playbook collection comes bundled with the Infoblox BloxOne Threat Defense connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Infoblox BloxOne Threat Defense connector.

- Get Named Lists
- Get Specific Named List
- Add Item into Named List
- Remove Item From Named List
- Dossier Source Lookup by Target Type
- Dossier Lookup Job Status
- Dossier Lookup Job Returns
- Dossier Indicator Source Lookup
- Dossier Source Lookup by Indicator Type
- Dossier Indicator Type Lookup Based on Source
- Dossier Lookup Job Status by Specific Task

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
