from tastypie.authentication import ApiKeyAuthentication


class MethodAuthentication(ApiKeyAuthentication):
    """ Always allow GET requests; require ApiKeyAuthentication for others """

    def is_authenticated(self, request, **kwargs):
        if request.method == "GET":
            return True

        return super(MethodAuthentication, self).is_authenticated(
            request, **kwargs)
