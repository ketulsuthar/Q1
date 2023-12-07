from models import User

USERS = {
    'admin': User(
        id=1,
        username='admin',
        password='scrypt:32768:8:1$5RR8uLQnuTGAAVJc$38258e3d6f3141980dcd771544bea2daef2ad3c880f95a542f49a47bcee05ec010f87054650e85f5b9f80866a971973dabfed2226987288451e794b66cc17f22'
    )
}