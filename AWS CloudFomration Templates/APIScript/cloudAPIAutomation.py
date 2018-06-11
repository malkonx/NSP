import httplib
import os
import sys
import base64
import json
import time
import sys
import requests

os.environ['SCRIPTFILES_PATH'] = os.path.dirname(os.path.abspath(__file__))
os.environ['NSM_PATH'] = "C://Program Files//McAfee//Network Security Manager//App"

Accept = "application/vnd.nsm.v2.0+json"
Content_Type = "application/json"
BOUNDARY = '--Boundary_1_12424925_1353496814940'
ContentType_multipart = 'multipart/form-data; boundary=%s' %BOUNDARY
env_file_path = os.environ['SCRIPTFILES_PATH']+"/cloudData.txt"
license_file_name = "license.zip"
license_file_path = os.environ['SCRIPTFILES_PATH'] + "/" + license_file_name

def write_log(msg):
    logfile = open(os.environ['NSM_PATH']+"/clouddeployment.log","a")
    logfile.write(time.strftime("%d/%m/%Y %H:%M:%S"))
    logfile.write("\t")
    logfile.write(str(msg))
    logfile.write("\n")
    logfile.write("\n")
    logfile.close()

def silentremove(filename):
    try:
        os.remove(filename)
        write_log("Removed %s\n"%(filename))
    except OSError as e:
        pass

def read_user_data():
	r = requests.get("http://169.254.169.254/latest/user-data")
	user_data = r.text
	user_data = user_data[:user_data.find("<script>")]
	user_data = json.loads(user_data)
	for key, value in user_data.items():
		if key == "username":
			key = 'API_ISM_USERNAME'
		elif key == "userpassword":
			key = 'API_ISM_PASSWD'
		write_log("Setting " + str(key) + " to " + str(value))
		os.environ[key.strip()] = value.strip()
	if os.getenv("CONTROLLER_NAME","None") == "None":
		write_log("No CONTROLLER_NAME in the user data hence exiting.")
		os.system("cfn-signal -s false -r \"Configuration Failed: Valid user data not provided for controller launch. Exiting.\" "+ os.environ["CONTROLLER_WAIT_HANDLE"])
		clean_up_and_exit()

def check_env_file():
    while not os.path.exists(env_file_path):
        write_log("Waiting for the creation of the file " + env_file_path)
        time.sleep(1)

    if os.path.isfile(env_file_path):
        env_file = open(env_file_path)
        for line in env_file.readlines():
            line = line.strip()
            if line and not line.startswith("#"):
                key = line.split("=")[0]
                value = line.replace(str(key) + "=","")
                write_log("Setting " + str(key) + " to " + str(value))
                os.environ[key] = value
        env_file.close()
    else:
        write_log(env_file_path + " does not exist")

def get_Connection():
    Connection = None
    Ip= os.getenv('ISM_IP','localhost')
    Port='443'
    Url = Ip + ':' + Port
    write_log("NSM address : " + Url)
    try:
        import ssl
        context = ssl._create_unverified_context()
        if Port == '443':
            Connection = httplib.HTTPSConnection(Url, context=context)
        else:
            Connection = httplib.HTTPConnection(Url)
    except:
        Connection = httplib.HTTPSConnection(Url)
    return Connection

def get_auth_session(Connection):
    """ login and set auth """
    AuthSession = None
    api_username = os.getenv('API_ISM_USERNAME', 'No Username Provided')
    User = api_username
    Pass = os.getenv('API_ISM_PASSWD', 'No Password Provided')
    user_pass = User + ":" + Pass
    authString = base64.encodestring(user_pass.encode('utf-8'))
    authString = authString.decode('utf-8').replace('\n','')
    Headers = {'Accept' : "%s" % Accept, "NSM-SDK-API" : "%s" % authString}
    try:
        write_log("Logging in to the manager")
        Connection.request("GET", "/sdkapi/session", None, Headers)                 
        logResponse = Connection.getresponse()
        loginData = logResponse.read()
        write_log(loginData)
        if "session" not in loginData:
            msg = "Failure in logging in to the manager, credentials used : username - %s, password - %s"%(User,Pass)
            write_log(msg)
            os.system("cfn-signal -s false -r \"Configuration Failed: " + msg + ". Exiting.\" "+ os.environ["CONTROLLER_WAIT_HANDLE"])
            clean_up_and_exit()
        loginObj = json.loads(loginData)
        sessionData = loginObj['session']
        userData = loginObj['userId']
        seesion_user = sessionData + ":" + userData
        AuthSession = base64.encodestring(seesion_user.encode('utf-8')).decode('utf-8').replace('\n','')
        write_log(AuthSession)
        Connection.close()
    except Exception as e:
        write_log(str(e))
        os.system("cfn-signal -s false -r \"Configuration Failed: Login to the NSM failed - " + str(e) + ". Exiting.\" "+ os.environ["CONTROLLER_WAIT_HANDLE"])
        clean_up_and_exit()
    return AuthSession
    """ login and set auth over """

def download_import_license(Connection, AuthSession):
    """ download and upload license file to manager """
    if os.getenv("TEST_DRIVE", "FALSE") == "FALSE":
        write_log("Downloading user entered license file: "+os.getenv('LICENSE_FILE','None provided')+" to " + license_file_path)
        try:
            import boto3
            s3 = boto3.resource('s3')
            s3.Bucket(os.getenv('S3_BUCKET_NAME', 'No s3 provided')).download_file(os.getenv('LICENSE_FILE','None provided'),license_file_path)
            time.sleep(10)
        except Exception as e:
            write_log(str(e))
       
        if(os.path.isfile(license_file_path)):
            write_log("Downloaded license file to " + license_file_path)
            write_log("Now starting the import of " + license_file_path+" into NSM")
            Headers = {'Accept': "%s" % Accept, 'NSM-SDK-API': "%s" % AuthSession, 'Content-Type': "%s" % ContentType_multipart}
            CRLF = '\r\n'
            msg = []
            msg.append('--' + BOUNDARY)
            msg.append('Content-Type: application/json')
            msg.append('')
            data = {}
            data["fileName"] = license_file_name
            jsonData = json.dumps(data)
            msg.append(jsonData)
            msg.append('--'+BOUNDARY)
            fp = open(license_file_path, 'rb')
            file_data = fp.read()
            fp.close()
            msg.append('Content-Type: application/octet-stream')
            msg.append('')
            msg.append(file_data)
            msg.append('--' + BOUNDARY )
            msg[-1] += '--'
            msg.append('')
            payload = CRLF.join(msg)
            write_log("Payload generation for License import over")
            license_url = "/sdkapi/license"
            Connection.request("PUT", license_url,  payload, Headers)
            response = Connection.getresponse()
            resultData = response.read()
            write_log(resultData)
            Connection.close()
            resultObj = json.loads(resultData)
            if resultObj.get('status') == 1:
                write_log("License imported to NSM")
            else:
                write_log("license import failed, exiting")
                os.system("cfn-signal -s false -r \"Configuration Failed: License import to NSM failed. Exiting.\" "+ os.environ["CONTROLLER_WAIT_HANDLE"])
                clean_up_and_exit()
        else:
            write_log("Downloading license file from S3 bucket to NSM has failed")
            os.system("cfn-signal -s false -r \"Configuration Failed: License could not be downloaded to the manager. Exiting.\" "+ os.environ["CONTROLLER_WAIT_HANDLE"])
            clean_up_and_exit()
    """ license part done """

def create_controller(Connection, AuthSession):
    """ create controller and send the signal """
    if os.getenv("TEST_DRIVE", "FALSE") != "FALSE":
        return 102
    connector_url = "/sdkapi/cloud/0/connector"
    Headers = {'Accept': "%s" % Accept, 'NSM-SDK-API': "%s" % AuthSession, 'Content-Type': "%s" % Content_Type}
    isHA = False
    if os.getenv("CONTROLLER_HA","") == "TRUE":
        isHA = True
    data = {"name" : os.environ['CONTROLLER_NAME'], "description":"Controller from automation", "sharedSecret" : os.environ["CONTROLLER_SECRET"], "privateCommunicationSubnet" : os.environ['CONTROLLER_SUBNET'], "isHA" : isHA}
    if os.getenv("CONTROLLER_CUSTOM_SERVICE_IP","").strip():
        data["serviceIp"] = os.getenv("CONTROLLER_CUSTOM_SERVICE_IP","")
    if isHA:
        data["haTimeout"] = os.getenv("CONTROLLER_HA_TIMEOUT",5)
    cloudDetails = {}
    if os.environ['CLOUD_PLATFORM'] == "AZURE":
        cloudDetails["type"] = "AZURE"
        azureDetails = {}
        azureDetails["directoryId"] = os.environ["AZURE_DIRECTORY_ID"]
        azureDetails['applicationKey'] = os.environ["AZURE_APP_KEY"]
        azureDetails['applicationId'] = os.environ['AZURE_APP_ID']
        azureDetails['subscription'] = os.environ["AZURE_CONTROLLER_SUBSCRIPTION"]
        cloudDetails["azureDetails"] = azureDetails
    else:
        cloudDetails["type"] = "AMAZON"
        awsDetails = {}
        awsDetails["region"] = os.environ["CONTROLLER_CLOUD_REGION"].upper().replace("-","_")
        awsDetails["useIAMRole"] = os.environ["USE_IAM_ROLE"] == "TRUE"
        if os.environ["USE_IAM_ROLE"] == "FALSE":
            awsDetails["accessKey"] = os.environ["CONTROLLER_CLOUD_ACCESSKEY"]
            awsDetails["secretKey"] = os.environ["CONTROLLER_CLOUD_SECRET"]
        cloudDetails['awsDetails'] = awsDetails
    data['cloud'] = cloudDetails
    payload = json.dumps(data)
    Connection.request("POST", connector_url,  payload, Headers)
    response = Connection.getresponse()
    resultData = response.read()
    if os.getenv('DEBUG', 'FALSE') == 'FALSE':
        del data['sharedSecret']
        if data.get('cloud',{}).get('awsDetails', {}).get('secretKey'):
            del data['cloud']['awsDetails']['secretKey']
        if data.get('cloud',{}).get('azureDetails', {}).get('applicationKey'):
            del data['cloud']['azureDetails']['applicationKey']
    write_log(str(data))
    write_log(resultData)
    Connection.close()
    resultObj = json.loads(resultData)
    added_controller_id = -1
    if resultObj.get('createdResourceId'):
        added_controller_id = resultObj['createdResourceId']
        write_log("Controller Created with resource id " + str(added_controller_id))
        write_log("Sending the signal for controller instance launch")
        os.system("cfn-signal -s true " + os.environ["CONTROLLER_WAIT_HANDLE"])
    else:
        write_log("Error while creating the controller. Sending the failure signal to the stack")
        os.system("cfn-signal -s false -r \"Configuration Failed: Controller creation failed in NSM. Exiting.\" "+ os.environ["CONTROLLER_WAIT_HANDLE"])
        clean_up_and_exit()
    return added_controller_id

def create_cluster(Connection, AuthSession, retry_count = 1):
    cluster_url = "/sdkapi/cloud/0/cluster"
    Headers = {'Accept': "%s" % Accept, 'NSM-SDK-API': "%s" % AuthSession, 'Content-Type': "%s" % Content_Type}
    data = {"name" : os.environ['CLUSTER_NAME'], "description":"Cluster from automation", "cloudConnector": os.environ['CONTROLLER_NAME'], "sharedSecret" : os.environ["CLUSTER_SECRET"]}
    if os.environ['CLOUD_PLATFORM'] == "AZURE":
        data["subscription"] = os.environ["AZURE_CLUSTER_SUBSCRIPTION"]
    payload = json.dumps(data)
    Connection.request("POST", cluster_url,  payload, Headers)
    response = Connection.getresponse()
    resultData = response.read().decode("utf-8")
    if os.getenv('DEBUG', 'FALSE') == 'FALSE':
        del data['sharedSecret']
    write_log(str(data))
    Connection.close()
    if resultData.find("errorMessage") != -1:
        if resultData.find("unacceptable: cloudDomainId") != -1 and retry_count < 16:
            write_log("Error while creating the cluster. Fabric server pool creation failed so retrying after 20 seconds")
            time.sleep(20)
            write_log("Have tried cluster creation for %s time"%(retry_count))
            return create_cluster(Connection, AuthSession, retry_count + 1)
        write_log(resultData)
    else:
        write_log(resultData)
        resultObj = json.loads(resultData)
        if resultObj.get('createdResourceId'):
            added_cluster_id = resultObj['createdResourceId']
            write_log("Cluster Created with resource id " + str(added_cluster_id))
            return added_cluster_id
    write_log("Error while creating the cluster.")
    os.system("cfn-signal -s false -r \"Configuration Failed: Cluster creation failed in manager. Exiting.\" "+ os.environ["CLUSTER_WAIT_HANDLE"])
    clean_up_and_exit()
    return -1

def get_controller_satus(added_controller_id, Connection, AuthSession):
    controller_url = "/sdkapi/cloud/connector/%s"%(added_controller_id)
    Headers = {'Accept': "%s" % Accept, 'NSM-SDK-API': "%s" % AuthSession, 'Content-Type': "%s" % Content_Type}
    Connection.request("GET", controller_url,  None, Headers)
    response = Connection.getresponse()
    resultData = response.read().decode("utf-8")
    write_log(resultData)
    if resultData.find("errorMessage") != -1:
        time.sleep(10)
        return get_controller_satus(added_controller_id, Connection, AuthSession)
    Connection.close()
    resultObj = json.loads(resultData)
    controller_status = []
    for member in resultObj['members']:
        controller_status.append(member['status'].lower())
    return controller_status

def check_controller_status_create_cluster(Connection, AuthSession, added_controller_id):
    """ create controller and send signal end """
    added_cluster_id = -1
    if added_controller_id > 0:
        """ wait for the controller to be online """
        controller_status = get_controller_satus(added_controller_id, Connection, AuthSession)
        write_log("Controller status is %s."%(controller_status))
        waitCount = 0
        loopCount = 180
        """ controller status will be checked till 1800 seconds with 10 second interval in each loop"""
        while "online" not in controller_status and waitCount < loopCount:
            time.sleep(10)
            controller_status = get_controller_satus(added_controller_id, Connection, AuthSession)
            waitCount += 1
            write_log("Controller status is %s after %s seconds"%(controller_status,waitCount * 10))
           
        """ wait for the controller to be online end """

        if "online" in controller_status:
            """ create cluster and send the signal """
            added_cluster_id = create_cluster(Connection, AuthSession)
            """ create cluster and send signal end """
            if added_cluster_id > 0:
                write_log("Sending the signal for sensor creation")
                os.system("cfn-signal -s true " + os.environ["CLUSTER_WAIT_HANDLE"])
        else:
            write_log("Controller did not come up online. Sending Failure signal to stack. Exiting.")
            os.system("cfn-signal -s false -r \"Configuration Failed: Controller instance did not come up online in Manager. Exiting.\" "+ os.environ["CLUSTER_WAIT_HANDLE"])
            clean_up_and_exit()
    return added_cluster_id          

def create_vm_group(Connection, AuthSession, added_cluster_id):
    if os.getenv("CREATE_VMGROUP", "FALSE") == "TRUE" and added_cluster_id > 0:
        write_log("Creating the VM Group.")
        vmgroup_url = "/sdkapi/cloud/cluster/%s/vmgroup"%(added_cluster_id)
        Headers = {'Accept': "%s" % Accept, 'NSM-SDK-API': "%s" % AuthSession, 'Content-Type': "%s" % Content_Type}
        data = {"name" : "Protected Group", "description" : "VM Group created at the time of Automation", "advancedAgentSettings" : { "inspectionMode" : "IPS" , "trafficProcessing" : "Ingress & Egress"}}
        if os.environ["CLOUD_PLATFORM"] == "AZURE":
            data["resourceGroup"] = os.environ["VMGROUP_RESOURCE_GROUP"].split(",")
            data["protectedObjects"] = os.environ["PROTECTED_OBJECTS"].split(",")
        else:
            data["vpc"] = os.environ["PROTECTED_VPC"].split(",")
            data["protectedObjects"] = os.environ["PROTECTED_OBJECTS"].split(",")
        write_log(str(data))
        payload = json.dumps(data)
        Connection.request("POST", vmgroup_url,  payload, Headers)
        response = Connection.getresponse()
        resultData = response.read()
        write_log(resultData)
        Connection.close()
        resultObj = json.loads(resultData)
        if resultObj.get('createdResourceId'):
            write_log("VM Group Created with resource id " + str(resultObj['createdResourceId']))
        else:
            write_log("Error while creating the VM Group.")

def clean_up_and_exit():
    silentremove(env_file_path)
    silentremove(license_file_path)
    write_log("Over\n")
    sys.exit()

if __name__ == '__main__':
    write_log("Started\n")
    read_user_data()
    # check_env_file()
    Connection = get_Connection()
    AuthSession = get_auth_session(Connection)
    download_import_license(Connection, AuthSession)
    added_controller_id = create_controller(Connection, AuthSession)
    added_cluster_id = check_controller_status_create_cluster(Connection,AuthSession, added_controller_id)
    create_vm_group(Connection, AuthSession, added_cluster_id)
    clean_up_and_exit()
