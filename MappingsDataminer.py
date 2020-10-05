import json
import requests
import re
import sys, traceback
import time

#request = input("Please enter request: ")

token = "033eb3d1a6a71d22fc591b772cf59d6e89e6b5de"

headersRaw = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'accept': 'application/vnd.github.VERSION.raw',
    'Authorization': 'token ' + token
}
headersJson = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Authorization': 'token ' + token
}

flatten = lambda l: [item for sublist in l for item in sublist]

requestsRemaining = 4800
startTime = time.time()
def loadPage(url, header):
    global requestsRemaining
    global startTime
    if requestsRemaining <= 0:
        sleepTime = 3600-(time.time()-startTime)
        print("requestsRemaining is empty, sleeping for"+str(sleepTime)+" seconds")
        time.sleep(sleepTime)
        startTime=time.time()
        requestsRemaining=5000
    requestsRemaining=requestsRemaining-1
    return requests.get(url, headers=header).text

loadPageJson = lambda url: loadPage(url, headersJson)
loadPageRaw = lambda url: loadPage(url, headersRaw)

loadJson = lambda url: json.loads(loadPageJson(url))

loadPageJson("https://api.github.com")

branchesUrl = lambda repo: "https://api.github.com/repos/"+repo+"/branches"

def find1_12Mappings(branches):
    for br in branches:
        branch = loadJson(loadJson(br['commit']['url'])['commit']['tree']['url'])['tree']            
        
        properties = list(map(lambda f: loadPageRaw(f['url']).splitlines(), filter(lambda f: f['path']=="gradle.properties" or f['path']=="build.properties", branch)))
        
        def resolve(value):
            #print("resolve "+str(value))
            v1 = re.match(r' *\'([.\-A-z_0-9]+)\'',value)
            v2 = re.match(r' *\"([.\-A-z_0-9]+)\"',value)
            v3 = re.match(r' *(config.)?([A-z_]+[A-z_0-9]*)',value)
            v4 = re.match(r' *\'\$\{(config.)?([A-z_]+[A-z_0-9]*)',value)
            v5 = re.match(r' *\"\$\{(config.)?([A-z_]+[A-z_0-9]*)',value)
            if v1:
                return v1.group(1)
            elif v2:
                return v2.group(1)
            elif v3 or v4 or v5:
                propertyName = v3.group(2) if v3 else (v4.group(2) if v4 else v5.group(2))
                #print("propertyName "+propertyName)
                for flines in properties:
                    for line in flines:
                        #print("   "+line)
                        found = re.match(r' *'+propertyName+' *= *([.\-A-z_0-9]+)',line)
                        if found:
                            return found.group(1)
                return "miss"
            else:
                print("strange... "+str(value))
                return "miss"
                
            
        for f in branch:
            if f['path']=="build.gradle":
                fj = loadPageRaw(f['url'])
                flines = fj.splitlines()
                for i in range(len(flines)):
                    line = flines[i]
                    if re.search(r'minecraft[ ]*\{', line):
                        for j in range(i,len(flines)):
                            maybeVersion = re.search(r'version[ ]*\=[ ]*(.+)',flines[j])
                            if maybeVersion:
                                mcversion = resolve(maybeVersion.group(1))
                                #print("chech "+str(mcversion))
                                if re.match(r'1.12', mcversion): #or 1.12.2?
                                    for k in range(i,len(flines)):
                                        maybeMappings = re.search(r'mappings[ ]*\=[ ]*(.+)',flines[k])
                                        if maybeMappings:
                                            return [resolve(maybeMappings.group(1))]
                #print(fj)
                #print(" ")
    return []

#print(find1_12Mappings(loadJson(branchesUrl(request))))

file1 = open('./github-pages.txt', 'r') 
lines = file1.readlines() 

projects = list(map(lambda i: i.replace('https://github.com/', '').rstrip('\n'), filter(lambda url: "github.com" in url, lines)))

project_count=50

frequency = {}
for project_start in range(0,len(projects),project_count):
    print("processing "+str(len(projects))+" mods, from "+str(project_start)+" count "+str(project_count))

    def projectToMappings(p):
        try:
            j = loadJson(branchesUrl(p))
            if isinstance(j,dict) and "API rate limit" in j.get("message",""):
                print("        Unexpected API rate limit!")
            return find1_12Mappings(j)
        except:
            print("Unexpected error for project: "+str(p))
            print("-"*60)
            traceback.print_exc(file=sys.stdout)
            print("-"*60)
            return []

    usesMappings = flatten(map(projectToMappings, [projects[i] for i in range(project_start, min(len(projects), project_start+project_count))]))

    for mappings in usesMappings:
        frequency[mappings]=frequency.get(mappings, 0)+1
        
    for mappings,count in frequency.items():
        print(mappings+" > "+str(count))

print("final frequency!")
for mappings,count in frequency.items():
    print(mappings+" > "+str(count))