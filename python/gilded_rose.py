# -*- coding: utf-8 -*-

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        raise NotImplementedError()


# --- Estrategias ---

class NormalItemUpdater(ItemUpdater):

    def update(self):
        self._decrease_quality(1)
        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self._decrease_quality(1)

    def _decrease_quality(self, amount):
        self.item.quality = max(0, self.item.quality - amount)


class AgedBrieUpdater(ItemUpdater):

    def update(self):
        self._increase_quality(1)
        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self._increase_quality(1)

    def _increase_quality(self, amount):
        self.item.quality = min(50, self.item.quality + amount)


class SulfurasUpdater(ItemUpdater):

    def update(self):
        pass


class BackstagePassUpdater(ItemUpdater):

    def update(self):
        if self.item.sell_in > 10:
            self._increase_quality(1)
        elif self.item.sell_in > 5:
            self._increase_quality(2)
        elif self.item.sell_in > 0:
            self._increase_quality(3)
        else:
            self.item.quality = 0

        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self.item.quality = 0

    def _increase_quality(self, amount):
        self.item.quality = min(50, self.item.quality + amount)


# --- Factory sin ifs ---

class UpdaterFactory:

    _strategies = {
        "Aged Brie": AgedBrieUpdater,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater,
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
    }

    @classmethod
    def get_updater(cls, item):
        updater_class = cls._strategies.get(item.name, NormalItemUpdater)
        return updater_class(item)


# --- GildedRose simplificado ---

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            UpdaterFactory.get_updater(item).update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
