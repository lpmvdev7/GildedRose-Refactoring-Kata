# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose


class TestItemNormal:
    def test_quality_decreases_by_1_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 19
        assert items[0].sell_in == 9

    def test_quality_decreases_by_2_after_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 18

    def test_quality_never_goes_below_zero(self):
        items = [Item("Normal Item", 5, 0)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    def test_quality_never_goes_below_zero_after_sell_date(self):
        items = [Item("Normal Item", 0, 1)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0


class TestAgedBrie:
    def test_quality_increases_before_sell_date(self):
        items = [Item("Aged Brie", 5, 10)]
        GildedRose(items).update_quality()
        assert items[0].quality == 11

    def test_quality_increases_twice_after_sell_date(self):
        items = [Item("Aged Brie", 0, 10)]
        GildedRose(items).update_quality()
        assert items[0].quality == 12

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 5, 50)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50

    def test_quality_caps_at_50_after_sell_date(self):
        items = [Item("Aged Brie", 0, 49)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50


class TestSulfuras:
    def test_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        assert items[0].quality == 80

    def test_sell_in_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        GildedRose(items).update_quality()
        assert items[0].sell_in == 5


class TestBackstagePasses:
    ITEM = "Backstage passes to a TAFKAL80ETC concert"

    def test_quality_increases_by_1_more_than_10_days(self):
        items = [Item(self.ITEM, 15, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 21

    def test_quality_increases_by_2_at_10_days(self):
        items = [Item(self.ITEM, 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 22

    def test_quality_increases_by_2_between_6_and_10_days(self):
        items = [Item(self.ITEM, 7, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 22

    def test_quality_increases_by_3_at_5_days(self):
        items = [Item(self.ITEM, 5, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 23

    def test_quality_increases_by_3_between_1_and_5_days(self):
        items = [Item(self.ITEM, 3, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 23

    def test_quality_drops_to_zero_after_concert(self):
        items = [Item(self.ITEM, 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    def test_quality_never_exceeds_50(self):
        items = [Item(self.ITEM, 5, 49)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50
