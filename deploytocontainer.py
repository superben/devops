import sys
import requests

PROJECT_ID = "project-4y4qlqvk"
#GRP_ID = "group-6yo87eal"
SVC_URL="10.7.116.236:31104"
#REP_NAME="tsf_100000013/nginx"
#TAG_NAME="20191010163213-v55"
def get_acs_token(url="http://10.7.115.20/accountDispatch/login"):
    data = dict(
        accountName="lihuawei_ibm",
        password="qazwsx1",
        opt="login"
    )
    r = requests.post(url, json=data)
    if r.status_code != 200:
        raise Exception("Login fail")
    acs_token = r.cookies['accessToken']
    print
    'acs_token is %s' % acs_token
    return acs_token

def deploy_grp( url="http://10.7.115.20/apiDispatch/v3?action=DeployContainerGroup"):
    headers = {
        "Cookie": "accessToken=" + acs_token,
        "Content-Type": "application/json"
    }

    deploy_data = dict(
        jvmOpts="-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m",
        Version="2018-03-26",
        groupId=GRP_ID,
        cpuRequest="0.5",
        memRequest= 384,
        server=SVC_URL,
        reponame= REP_NAME,
        tagName= TAG_NAME,
        doNotStart= "false",
        instanceNum= 1
        )

    data = dict(
        action="DeployContainerGroup",
        serviceType="tsf",
        regionId=1,
        data=deploy_data,
        projectId=PROJECT_ID
        )
    r = requests.post(url, json=data, headers=headers)
    if r.status_code != 200:
        raise Exception("Deploy fail")
        print
        r.content

if __name__ == "__main__":
    acs_token = get_acs_token()
    GRP_ID = sys.argv[1]
    print(GRP_ID)
    REP_NAME=sys.argv[2]
    print(REP_NAME)
    TAG_NAME=sys.argv[3]
    print(TAG_NAME)
    deploy_grp()