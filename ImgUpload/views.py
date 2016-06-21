import json
import subprocess
from django.shortcuts import render
import urllib


def index(request):
    print "No active session"
    return render(request, 'index.html')


def photos(request):
    client_id = "xxx" #Your app id here, you can get it after creating an application on developers.facebook.com
    client_secret = "xxx" #Client secret here
    redirect_url = "xxx" #Your redirect url, configure in your facebook app also
    code=request.GET.get('code', False)
    # print code
    oauth_args= dict(
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_url,
        code = code,
    )
    print "code "+code

    oauth_curl_cmd = ['curl','https://graph.facebook.com/v2.6/oauth/access_token?' + urllib.urlencode(oauth_args)]
    oauth_response = subprocess.Popen(oauth_curl_cmd,stdout = subprocess.PIPE,stderr = subprocess.PIPE).communicate()[0]
    oauth_response=json.loads(oauth_response)
    oauth_access_token = oauth_response['access_token']
    print "Token: " +oauth_access_token
    print "Response"
    print oauth_response

    oauth_curl_cmd = ['curl','https://graph.facebook.com/v2.6/me/photos?fields=images&type=uploaded&access_token={0}'.format(oauth_access_token)]
    oauth_response = subprocess.Popen(oauth_curl_cmd,stdout = subprocess.PIPE,stderr = subprocess.PIPE).communicate()[0]
    oauth_response=json.loads(oauth_response)
    print "Response : "
    print oauth_response

    return render(request, 'index.html',{'response': oauth_response})