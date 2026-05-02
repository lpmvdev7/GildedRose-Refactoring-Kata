# -*- coding: utf-8 -*-

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        if self.is_sulfuras():
            return

        self.update_quality()
        self.decrease_sell_in()

        if self.is_expired():
            self.update_expired()

    # --- Template methods (hooks) ---

    def update_quality(self):
        self.decrease_quality()

    def update_expired(self):
        self.decrease_quality()

    # --- Helpers comunes ---

    def decrease_sell_in(self):
        self.item.sell_in -= 1

    def is_expired(self):
        return self.item.sell_in < 0

    def is_sulfuras(self):
        return self.item.name == "Sulfuras, Hand of Ragnaros"

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1


# --- Implementaciones específicas ---

class AgedBrieUpdater(ItemUpdater):

    def update_quality(self):
        self.increase_quality()

    def update_expired(self):
        self.increase_quality()


class BackstagePassUpdater(ItemUpdater):

    def update_quality(self):
        self.increase_quality()

        if self.item.sell_in < 11:
            self.increase_quality()

        if self.item.sell_in < 6:
            self.increase_quality()

    def update_expired(self):
        self.item.quality = 0


class NormalItemUpdater(ItemUpdater):
    pass


class SulfurasUpdater(ItemUpdater):
    def update(self):
        # No cambia nada
        return


# --- Factory simple ---

class ItemUpdaterFactory:
    @staticmethod
    def get_updater(item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater(item)
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater(item)
        if item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater(item)
        return NormalItemUpdater(item)


# --- Clase principal ---

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = ItemUpdaterFactory.get_updater(item)
            updater.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)