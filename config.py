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
    "casting_assistant" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..fAjF2uQ3GyyBaWcr.hKQ2bzrOY7EYbzzE-6tnG17-alrClSQqJxccebFibMXaEYc1geBiJFt8OFTg8R85IJJjsH6235CaoyOmADgy3MGMkYr7Q2TqxX2EM9t-oBGPA27LJ4qvG3elyiaEZ8dimrJ962gJFn1jRodOMmxF_nTJRehGu4f6c7vAkSLGDo_mTjNxufSKFb1QGLhxAlHuRN0XjFCvwozepwGgA6kmgxFacLkEBIgBjga9smYIQwtLi1a52df0ne2K8UzTELIM_g-EP7efCtkJhlXXSSdH8B_Q3lqQRs-nkMYwFhwW3S87wM0fjnZ61_SGO7g.Lf_iiswHqx2HH4NmkDOzmw",
    "executive_producer" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..NEZcQ0G9k_cLy6IL.m9vMfWrDYRc_pEHPUzV5WgoHFk94pBOL7cgkzDujvH-KFB9IMjQ02oiDzSGvag2fOc7vZa8VH6TLSHCubIr6CbFlide3vU0dUMdvA6hdwCUqLt-4FMresoyjtts3biNygulSZ1HZE6w0I51SkMZTdZ5UZhx7PA5m4X6l06Q2co4aQyKcAy4KRhAVMySAQu9-8CKvUjvPEk4RyH9rn4ASWOhJ-0z0tSpvbzFFAEvoGxiT-bh6xeTTBe4nlPJcaWwt6nP9o547JB0jrOs8oQtB1fmRsEarwTiAKtrSX4AZ6A9SdGAd9vugYnxxM-4.bwigRH4hrGuxoHBQENbS3g",
    "casting_director" : "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtNGs0dnRjcDc0MHhnaHcwdy51cy5hdXRoMC5jb20vIn0..-VzWyJOX2chZPk_o.-IYIusztQiLMNJimov2yu1XG7SmEsKA7680Ufh9pzbdgHBnwO4SkPRs44SimVZeIHIWCRrWXyP-sn9jRg-dI7UUAgn3yYfANGuiKp0Yk3KZgFXgFMabqBjDE3MCML_4V1FPJYUh8Nornrg6GTCdEIktfBN4kYK8K_9C6t5cWMLU_urkrPWSORs47OagvyYw7VNR0vxPNBPbYoi3b6rWa9MPprH-6WmsHNTcTvUOOVeURaIePquYQEFx502yregItEU7_huAbJgsTcapzTR0R9NQvtDStstT7OZUn7YR13i1LPGGOeZjG_6IKnqQ.EcjXPRg2rarA9k7z8TL3UA"
}