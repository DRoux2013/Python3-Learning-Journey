LINUX_DNS_SERVER_IP = "192.168.1.1"

dns_service_status = "failed"
if dns_service_status == "active":
    print(f"{LINUX_DNS_SERVER_IP} operating within normal parameters")
elif dns_service_status == "inactive":
    print(f"Warning: {LINUX_DNS_SERVER_IP} inactive")
else:
    print(f"Alert, {LINUX_DNS_SERVER_IP} has failed, immediate attention required")
