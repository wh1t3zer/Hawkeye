from logging import Filter

from middleware.response import request_id_context


class TraceIDFilter(Filter):
    def filter(self, record):
        print(record)
        record.traceid = request_id_context.get("TRACE_ID")
        return True
