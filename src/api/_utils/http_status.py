class HttpStatus:
    """ RFC-7231 (reference: https://datatracker.ietf.org/doc/html/rfc7231#section-6.3.1)"""

    ## 2XX ##
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204

    ## 4XX ##
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONTENT_TOO_LARGE = 413

    ## 5XX ##
    INTERNAL_SERVER_ERROR = 500
