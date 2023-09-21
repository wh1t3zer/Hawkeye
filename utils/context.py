from fastapi import Request


class MyContext:
    def __init__(self, request: Request, request_id):
        self.request = request
        self.request_id = request_id
