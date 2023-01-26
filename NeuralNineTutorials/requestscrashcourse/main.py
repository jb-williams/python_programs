#import requests

#params = {
    #"name": "Mike",
    #"age": 25,
#}
#res_get = requests.get("https://httpbin.org/get", params=params)
#print(res_get.url) # what api recieves when sent

#payload = {
    #"name": "Mike",
    #"age": 25,
#}
#res_post = requests.post("https://httpbin.org/post", data=payload)
#print(res_post.url) # what api recieves when sent

# response status code

#print(response.status_code)
# full response
#print(response.text)

# to remove your ip if showing someone and want to be safe
# give a dictionary

#res_json = res_get.json()
#del res_json['origin']
#print(res_json)

## Status codes stuff

#res_status = requests.get("https://httpbin.org/status/200")
#print(res_status.status_code)

# can specify specific codes to check if they are returned or not

#res_status1 = requests.get("https://httpbin.org/status/404")
#print(res_status1.status_code)

# can either specify names of codes, or ref the num directly. ex: not_found vs 404

#if res_status1.status_code == requests.codes.not_found:
    #print("Not Found")
#else:
    #print(res_status1.status_code)

## user-agents stuff

#res_user_agent = requests.get("https://httpbin.org/user-agent")
#print(res_user_agent.text)

# specify user-agent
# set to custom user-agent found of search engine

#headers = {
    #"User-Agent": "HelloWorld/1.1"
#}
#res_user_agent1 = requests.get("https://httpbin.org/user-agent", headers=headers)
#print(res_user_agent1.text)

# specific other fields
# example downloading images

#headers = {
    #"User-Agent": "HelloWorld/1.1",
    #"Accept": "image/png",
#}
#res_user_agent2 = requests.get("https://httpbin.org/image", headers=headers)
#print(res_user_agent2.text)
# would give bytes and we would want save this into a binaryfile, image
#with open("myimage.png", "wb") as f:
    #f.write(res_user_agent2.content)

# changing accept image to jpg, will give diff image if api is programed that way but would ahve to change myimage to .jpg
# may work with webp as well


## example use case
# if you have a list of free public proxies and want to see which work
# may have to wait for response

#response = requests.get("https://httpbin.org/get/delay/3")

# add a timeout, this basic would error out
#response = requests.get("https://httpbin.org/get/delay/5", timeout=3)

# doing something add a try haha
#for _ in [1,2,3]:
    #try:
        #response = requests.get("https://httpbin.org/get/delay/5", timeout=7)
    #except:
        #contintue

#res_json = response.json()
#del res_json['origin']
#print(res_json)

# using proxy servers paid or free
#proxies = {
    #"http": "some.ip.of.proxy:80",
    #"https": "some.ip.of.proxy:80", # wont work with https just to have something here, would ahve to target the https api
#}

#response = requests.get("https://httpbin.org/get", proxies=proxies)
# dont want to delete "origin" because want to see proxies ip
#print(response.text)