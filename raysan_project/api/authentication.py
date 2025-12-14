from rest_framework.authentication import TokenAuthentication as TAuth


class TokenAuthentication(TAuth):
    keyword = 'raysanDevToken'