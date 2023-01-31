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
    "casting_assistant" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..GTm1gz-Z8Pfik8l5.j3GHE3smudOBS7saVzx4ZfrExSP0K_Vw6Fxbq5zH3itnVYjqJ6U5sPFQXjK3j0-6VTKyrOOAlknhcPEnWhaf-EoitSTyAm5LZYU6mtSL-aHPzT2DSmv7K0R3DntuRU-v1yiTWIxNTka4HIfjFIZ2zPtM_Ewll9XHAkDHRmtbWu1qDvMLyATHtvPNLl5Y31Okh2xdYn5zIoY1hPfzUP1XJ6SkoXAvSWb9tbtcxLJQbzTfZcozTGYcLgDokmiCs0aKksXNmaIUsNDBNXBr1Lw-9V3FKQw0XmqOeUDeXFwxJKtcOjYNCO_cvkO6leI.SXv4oBB-3Sjgw3hJ6wTHJQ",
    "executive_producer" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..cizMokOOuq5Q7DHp.99q4vEwtmUvXTy1-sNCKUfWGCryekwT3kNZ6bQvO5kazzrnBhw3dNMvm0w3FF34-yP8h5q07o26LeGPjGhuH--BtopSh1piGWIudJRPELAVFcq9sv7Q5h9hgi4xI4ELarI4ILiiveItGjBuyk6l-J66IGbmGeeYCQ-3M8VnLNRHX1bxPvMddHgHPe9H58MQYHSKG9e5qCoAwFKX8QPSoAs0lzzBjdlWcGhyT6n5EJvGCRyR5Jx6xtROKX2IRTQNKudiI0Q7Q7KWNI8sF6tBprEMb0U5G2ybGfW14_pnQR-lYPROVPKTaMp3UHgQ.vbFQZ0DSu_ApXsAaRCvG7w",
    "casting_director" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..8nNbVp_3qVsJ-sBr.souKyamf9q5MYuMbDrKFYnAraxsZH4qLflsPcOApy7LoIhEAUfJgy0XNrMr1Z3f3FSgaGpOBiJIwC4Tkw-GFJHzr3DEL9wW6C2NVsIlwaTTjW75Xsjz8oLwFXeCeGmOx_iOoyI8KI2NKsTk3QNecmUUQrVyClupmTMlBbfhg0BM1YSBg6jMympgiwfX7hqZBkS2c-E0jJB2FbpVtLuncbqI3EFBsJSHypbvopAtNLipCnYlKiRq-iaX-c0seXO0erBBGyAr426NkBRtd4GTFKkgJRYdYmp8jWYZim8P-wHYpLXCmgQRESfDup_4.z-t-xoupu8zum663Ye4DRg"
}