"""
Provides access to Revit Journals

"""

import os.path as op
from pyrevit import HOST_APP


def get_journals_folder():
    return op.dirname(HOST_APP.app.RecordingJournalFilename)


def get_current_journal_file():
    return HOST_APP.app.RecordingJournalFilename
