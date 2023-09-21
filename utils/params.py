from fastapi import Request
from pydantic import validators
def DefaultGetValidParams(params):
    return 1


def GetValidator(request: Request, validator: validators, exception: Exception):
    # val =
