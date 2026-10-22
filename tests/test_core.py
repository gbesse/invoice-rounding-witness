import unittest
from invoice_rounding_witness import run

def line(id,net,rate='0.20',code='s'):return dict(id=id,net=net,tax_rate=rate,tax_code=code)
class DomainTests(unittest.TestCase):
 def test_category_vs_line_difference(self):
  r=run({'currency':'EUR','lines':[line('a','0.03'),line('b','0.03')]});self.assertEqual(r['sum_line_tax'],'0.02');self.assertEqual(r['sum_category_tax'],'0.01');self.assertEqual(r['difference'],'0.01')
 def test_negative_credit_rounding(self):self.assertEqual(run({'currency':'EUR','lines':[line('a','-0.03')]})['sum_line_tax'],'-0.01')
 def test_rates_never_mixed_under_same_code(self):
  with self.assertRaises(ValueError):run({'currency':'EUR','lines':[line('a','1.00'),line('b','1.00','0.10')]})
 def test_fractional_cent_net_rejected(self):
  with self.assertRaises(ValueError):run({'currency':'EUR','lines':[line('a','1.005')]})
 def test_explicit_half_even(self):self.assertEqual(run({'currency':'EUR','rounding':'half_even','lines':[line('a','0.05','0.10')]})['sum_line_tax'],'0.00')
