# Copyright (c) 2026, ErpGenEx
from frappe.tests.utils import FrappeTestCase
from omnexa_core.omnexa_core.infra_parity import preview_infra

class TestSapParityInfraApp(FrappeTestCase):
	def test_infra_kpi(self):
		out = preview_infra("eng_workflow_engine")
		self.assertEqual(out["vertical"], "eng_workflow_engine")
