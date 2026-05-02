# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_conjured_item_degrades_twice_as_fast_before_sell_date(self):
        items = [Item("Conjured Mana Cake", sellIn=5, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 18  # degrada 2 por día (doble que normal)

    def test_conjured_item_degrades_four_times_after_sell_date(self):
        items = [Item("Conjured Mana Cake", sellIn=0, quality=20)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 16  # degrada 4 por día tras sell date

    def test_conjured_quality_never_below_zero(self):
        items = [Item("Conjured Mana Cake", sellIn=5, quality=1)]
        gr = GildedRose(items)
        gr.update_quality()
        assert items[0].quality == 0

        
if __name__ == '__main__':
    unittest.main()
