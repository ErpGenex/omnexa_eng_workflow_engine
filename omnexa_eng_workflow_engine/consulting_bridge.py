# Copyright (c) 2026, Omnexa and contributors
# License: MIT. See license.txt

"""Lazy import from **omnexa_engineering_consulting** until logic is moved into this app."""


def get_workflow_facade():
	from omnexa_engineering_consulting.integrations import workflow_facade

	return workflow_facade
