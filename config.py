# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "dev-4k4vtcp740xghw0w.us.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "Music"
}

pagination_service = {
    "example" : 10 # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..WjvwLMSNWSRCygl_.V9w2VUpbcv53sEqWkl874rOl9N_D30pojYBVouDLcaoFNhqsFlT2ihmUJDbpc7UQPX-hxSdTDEtQIhaEVzvTPreOq9DY3hF_zuehJd-mK_ZKOasgljT7GIu79LxRRI866S_uthnMPgWZUGyrBnLj5HPHmYD4819vPNcaxWWtCI4tpvmhPGTc6gK5-c0qmLst8jISMCjlWi5lcoBjjAemkIo4VSpcz_obLEj3UPFelSf7VJ9GNQflpegBikjTbHIDMkVLa_bcF1VNWQ0CuB_8sXSxRgU3_oFxrE-rENf-vKgztOS0qiIrZGW-q6w.5xM0MZWHT1xGJAo4gZ4pEA",
    "executive_producer" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..Bzom36eOytzLpPWs.2XLGJR7EnIuclTMYtzcpYn2J53nyhMVacFmP4e9pqm1lRWd4_6ZFSyVE7IyBBOwuIpsM4D0HvQrkGxU9Iq7B2SCe8ksl235J_oawizevGadyOy8Cc1awp-ek9rquloOypHowKoxna4N5BWnfSzq43dgT0nNFZ74U4Jv-S2T3An1qKy8ML1xWp7Tky-DWbnsjhOGwvjjHDaDy3rq5DnA80sbkBeH3dSYvxR9e9py5dqve6dIPvk4bZstmRWvI3XMVbQULexNgwrarQFaTjbAbktS5ubJnWqRFx3eMMAlKm7OPNakoRA7sDVssAqE.wAiMCy6ImsnslAhGX8NeEQ",
    "casting_director" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..9sE3YzMZIyonxwZW.lOqc2FfclSKqDEgyK_FdNKkmzjhj5_Me0UmAv3Ra_jkVHXhTW1Iv57q8Zqa2xOKm0X8aEqRMydgTTg3nhQ9-mTkUkVXw4jDjscSGWNSKUBQoadKtw7uOb8GieTr7f2XtOV1Lcoz3oOzee4vo8QHWgzsmhT039REzOQByolgbVbuHB1gRaBMl4tH3H2Ruryr4mZI6rmb_D68VBUQFP2cRSnLsXqMCOk6Q-AO-3-CpaJhgCPzb0qfmY8MfKwVNIz1lm0Yr5IJ2cLhKpc47iPeEnSeZ6E5tVc7u0LYJFRO6Cqp5f9p3xg1jr_MpDi4.SuClS6r6GUU7Cwr4DdNXzA"