import unittest
from redhat_interview_interview.main import *
from unittest.mock import patch, MagicMock


@patch("redhat_interview_interview.main.dnf", MagicMock(), create=True)
class TestMain(unittest.TestCase):
    class GetHawkeyQueryObject:
        class _dotmap(dict):
            """
            This internal class aims to be a helper to convert an dictionary
            to an dot notation object mapping. This is intended to mock the behaviour of
            _hawkye.Query object that is returned from the `filter` function of the same class
            """

            __getattr__ = dict.get

        def __call__(self, *args, **kwds):
            pass

        def filter(self, **kwds):
            return [
                self._dotmap(
                    {
                        "version": "5.13.12",
                    }
                )
            ]

    def test_get_installed_dnf_packages(self):
        assert get_installed_dnf_packages() is not None

    def test_main_initialization(self):
        assert main() is None

    @patch(
        "redhat_interview_interview.main.get_installed_dnf_packages",
        GetHawkeyQueryObject,
    )
    def test_main_with_kernel_versions(self):
        assert main() is None
