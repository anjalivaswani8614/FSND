import http.client

conn = http.client.HTTPSConnection("dev-4k4vtcp740xghw0w.us.auth0.com")

payload = "{\"client_id\":\"oRW1PrlT161eJMdzeOz12hRAkpUwdR3E\",\"client_secret\":\"SVhd4gq_uafzu0-ohC_FvJVPNH_cRyItsGaQfGiaWuzO2jnRK3ako6fI_FOrJMGs\",\"audience\":\"/movies\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))