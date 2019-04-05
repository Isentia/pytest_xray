from datetime import datetime, timedelta


class XrayTestReport:
    def __init__(self, test_key, test_exec_key, duration, exception_log=None):
        self.test_key = test_key
        self.test_exec_key = test_exec_key
        self._set_execution_range(duration)
        self.exception_log = exception_log

    def _set_execution_range(self, duration):
        self.start_ts = datetime.utcnow()
        self.end_ts = self.start_ts + timedelta(microseconds=duration * 1000 ** 2)

    def __repr__(self):
        if self.exception_log:
            return f"<XrayTestReport (FAIL) test_key={self.test_key}>"
        else:
            return f"<XrayTestReport (PASS) test_key={self.test_key}>"

    def as_dict(self):
        entry = {"testKey": self.test_key, "status": "FAILED" if self.exception_log else "PASSED"}
        # "start": self.start_ts.isoformat()[:-7],
        # "finish": self.end_ts.isoformat()[:-7],
        if self.exception_log:
            entry["comment"] = self.exception_log
        return entry

    @classmethod
    def as_passed(cls, test_key, test_exec_key, duration):
        return XrayTestReport(test_key, test_exec_key, duration)

    @classmethod
    def as_failed(cls, test_key, test_exec_key, duration, exception_log):
        return XrayTestReport(test_key, test_exec_key, duration, exception_log)
