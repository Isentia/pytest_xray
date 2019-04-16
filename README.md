Plugin installation
====

To install this library for use please enter the following command:

    $ pip install pytest_xray

To use this plugin
====

To take advantage of the pytest xray plugin, use markers from pytest to associate a test function with a test key and test execution id:

    import pytest

    @pytest.mark.xray(test_key="PRDS-12345", test_exec_key="PRDS-12121")
    def test_my_function():
        assert True == True

Enable the plugin by passing the extra options to the command line when invoking the pytest runner:

    $ pytest . --jira-xray

It is important that the environment variables **XRAY_API_CLIENT_ID** and **XRAY_API_CLIENT_SECRET** are set for pytest_xray to sucessfully post results to the Xray API.

Maintenance notes
====
Please make sure that any new releases of the library use an incremented version number from the last. The following guidance is used to properly version bump this library {major}.{minor}.{patch}.

Major versions are increased for any new overall library features or general API breaking changes.

Minor versions are increased for any new features added or implementation changes to existing APIs.

Patch versions are increased for any bug fixes and non-breaking changes.

To automatically bump versions, best to install bump2version, then enter either of the following on the command line:

    $ bump2version major

or

    $ bump2version minor

or

    $ bump2version patch

These commands automatically commits and tags a new version. Make sure to push tags to the server with 

    $ git push && git push --tags