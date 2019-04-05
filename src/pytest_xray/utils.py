import json
import logging

import pytest
import requests

from .constants import XRAY_MARKER_NAME

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_test_keys = {}


def _get_xray_marker(item):
    return item.get_closest_marker(XRAY_MARKER_NAME)


def associate_marker_metadata_for(item):
    marker = _get_xray_marker(item)
    if not marker:
        return

    test_key = marker.kwargs["test_key"]
    test_exec_key = marker.kwargs["test_exec_key"]
    _test_keys[item.nodeid] = test_key, test_exec_key


def get_test_key_for(item):
    results = _test_keys.get(item.nodeid)
    if results:
        return results
    return None, None


class PublishXrayResults:
    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret

    def __call__(self, *report_objs):
        bearer_token = self.authenticate()
        for a_dict in self._test_execution_summaries(*report_objs):
            self._post(a_dict, bearer_token)

        logger.info("Successfully posted all test execution results to Xray!")

    def _post(self, a_dict, bearer_token):
        payload = json.dumps(a_dict)
        logger.debug(f"Payload => {payload}")
        url = self.results_url()
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {bearer_token}"}
        resp = requests.post(self.results_url(), data=payload, headers=headers)

        if not resp.ok:
            logger.error("There was an error from Xray API!")
            logger.error(resp.text)
            logger.info(f"Payload => {payload}")
        else:
            logger.info("Post test execution success!")

    def results_url(self):
        return f"{self.base_url}/api/v1/import/execution"

    def authenticate(self):
        url = f"{self.base_url}/api/v1/authenticate"
        payload = {"client_id": self.client_id, "client_secret": self.client_secret}
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url, payload, headers)
        token = resp.json()
        return token

    def _test_execution_summaries(self, *report_objs):
        summaries = {}

        for each in report_objs:
            if not each.test_exec_key in summaries:
                summaries[each.test_exec_key] = self._create_header(each.test_exec_key)
            summaries[each.test_exec_key]["tests"].append(each.as_dict())

        return summaries.values()

    def _create_header(self, test_exec_key):
        return {
            "testExecutionKey": test_exec_key,
            "info": {
                "summary": "Execution of automated tests",
                "description": "",
                "version": "",
                "testEnvironments": ["UAT"],
            },
            "tests": [],
        }
