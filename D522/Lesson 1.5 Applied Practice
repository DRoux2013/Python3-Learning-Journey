""" Server Status Check Program """
servers = [
    {"hostname":"web01","status":"up"},
    {"hostname":"db01","status":"down"},
    {"hostname":"app01","status":"up"},
    {"hostname":"dns01","status":"down"}
    ]
def check_servers():
   for server in servers:
        hostname = server["hostname"]
        status = server["status"]
        if status == "down":
            print(f"{hostname} is down")
        else:
            print(f"{hostname} is operational")

if __name__ == "__main__": check_servers()