import sys
print(sys.path)
#sys.path.append(rootPath)
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.tsf.v20180326 import tsf_client, models 
try:
    def deploycontainer():
        cred = credential.Credential("AKIDqYN3JQCCvTmuortUyd3JNFICsIXXQyJx", "bzkGWaljpkV3SccNwMZaLtDUZRDj37ye")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tsf.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tsf_client.TsfClient(cred, "ap-beijing", clientProfile)
        req = models.DeployContainerGroupRequest()
        params = '{"GroupId":'+'"'+GRP_ID+'"'+',"Version":"2018-03-26","Server":"ccr.ccs.tencentyun.com","Reponame":'+'"'+REP_NAME+'"'+',"TagName":'+'"'+TAG_NAME+'"'+',"InstanceNum":2,"CpuRequest":"0.54","MemRequest":"1024"}'
        print(params)
        #params = '{"GroupId":"group-9yngk44a","Version":"2018-03-26","Server":"ccr.ccs.tencentyun.com","Reponame":"tsf_100011309346/ibm-devops-demo","TagName":"v34","InstanceNum":2,"CpuRequest":"0.54","MemRequest":"1024"}'
        req.from_json_string(params)
        resp = client.DeployContainerGroup(req)
        print(resp.to_json_string())
except TencentCloudSDKException as err: 
        print(err)

if __name__ == "__main__":
    GRP_ID = sys.argv[1]
    print(GRP_ID)
    REP_NAME=sys.argv[2]
    print(REP_NAME)
    TAG_NAME=sys.argv[3]
    print(TAG_NAME)
    deploycontainer()