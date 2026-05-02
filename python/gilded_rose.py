# -*- coding: utf-8 -*-

class GildedRose(object):

    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if self._is_sulfuras(item):
                continue

            if item.name == self.AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == self.BACKSTAGE_PASSES:
                self._update_backstage_pass(item)
            else:
                self._update_normal_item(item)

            item.sell_in -= 1

            if item.sell_in < 0:
                self._handle_expired(item)

    # --- Métodos por tipo ---

    def _update_aged_brie(self, item):
        self._increase_quality(item)

    def _update_backstage_pass(self, item):
        self._increase_quality(item)

        if item.sell_in < 11:
            self._increase_quality(item)

        if item.sell_in < 6:
            self._increase_quality(item)

    def _update_normal_item(self, item):
        self._decrease_quality(item)

    # --- Guard clauses aplicadas aquí ---

    def _handle_expired(self, item):
        if item.name == self.BACKSTAGE_PASSES:
            item.quality = 0
            return

        if item.name == self.AGED_BRIE:
            self._increase_quality(item)
            return

        self._decrease_quality(item)

    def _is_sulfuras(self, item):
        return item.name == self.SULFURAS

    # --- Helpers ---

    def _increase_quality(self, item):
        if item.quality >= 50:
            return
        item.quality += 1

    def _decrease_quality(self, item):
        if item.quality <= 0:
            return
        item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)