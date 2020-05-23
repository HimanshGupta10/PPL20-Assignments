host_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "www.google.com", "www.coep.org"]
with open(host_path, 'r+') as file :
    content = file.read()
    for site in website_list :
        if site in content :
            pass
        else :
            file.write(redirect + " " + site + "\n")
