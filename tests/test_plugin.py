pytest_plugins = "pytester"  # to get testdir fixture


def test_myplugin(testdir):
    test_example_1 = """
    from random import randint

    import pytest

    pytest_plugins = "pytester"

    @pytest.mark.xray(test_key="PRDS-12277", test_exec_key="PRDS-12276")
    def test_pass_1():
        pass

    @pytest.mark.xray(test_key="PRDS-12280", test_exec_key="PRDS-12276")
    def test_pass_2():
        pass
    """
    testdir.makepyfile(test_example_1)
    result = testdir.runpytest("--jira-xray")
    # result = testdir.runpytest("")
    assert len(result.errlines) == 1
    assert result.errlines[0] == ""
    result.fnmatch_lines(
        """
        test_example*
    """
    )

