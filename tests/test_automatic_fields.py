"""Test that with no fields selected for a stream automatic fields are still
replicated."""
from base import WorkdayAdaptivePlanningBaseTest
from tap_tester.base_suite_tests.automatic_fields_test import MinimumSelectionTest


class WorkdayAdaptivePlanningAutomaticFields(MinimumSelectionTest, WorkdayAdaptivePlanningBaseTest):
    """Test that with no fields selected for a stream automatic fields are
    still replicated."""

    @staticmethod
    def name():
        return "tap_tester_workday_adaptive_planning_automatic_fields_test"

    def streams_to_test(self):
        streams_to_exclude = {}
        return self.expected_stream_names().difference(streams_to_exclude)

