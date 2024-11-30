from django.shortcuts import render,HttpResponse
#y3DFatULGVHCCjUb3yZ2bg==yKeRweS1ky4JKSdN
# Create your views here.
def home(request):
    import json
    import requests
    if request.method=="POST":
        query=request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request=requests.get(api_url + query,headers={'X-Api-Key':'y3DFatULGVHCCjUb3yZ2bg==yKeRweS1ky4JKSdN'})
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
            # context={}
            # context['data']=api
            # print(context)
        except Exception as e:
            api="Oops! There is an error"
            print(e)
        return render(request,'index.html',{'api':api})
        #return render(request,'index.html',context)
    else:
        return render(request,'index.html',{'query':'Enter a valid query'})

