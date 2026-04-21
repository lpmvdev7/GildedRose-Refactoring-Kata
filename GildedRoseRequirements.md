# Gilded Rose Requirements Specification

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in `Quality` as they approach their sell by date.

We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that
we can begin selling a new category of items. First an introduction to our system:

- All `items` have a `SellIn` value which denotes the number of days we have to sell the `items`
- All `items` have a `Quality` value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

Pretty simple, right? Well this is where it gets interesting:

- Once the sell by date has passed, `Quality` degrades twice as fast
- The `Quality` of an item is never negative
- __"Aged Brie"__ actually increases in `Quality` the older it gets
- The `Quality` of an item is never more than `50`
- __"Sulfuras"__, being a legendary item, never has to be sold or decreases in `Quality`
- __"Backstage passes"__, like aged brie, increases in `Quality` as its `SellIn` value approaches;
	- `Quality` increases by `2` when there are `10` days or less and by `3` when there are `5` days or less but
	- `Quality` drops to `0` after the concert

We have recently signed a supplier of conjured items. This requires an update to our system:

- __"Conjured"__ items degrade in `Quality` twice as fast as normal items

Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything
still works correctly. However, do not alter the `Item` class or `Items` property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the `UpdateQuality` method and `Items` property static if you like, we'll cover
for you).

Just for clarification, an item can never have its `Quality` increase above `50`, however __"Sulfuras"__ is a
legendary item and as such its `Quality` is `80` and it never alters.




¿Cuantos tipos de items diferentes se mencionan? 
- items normales
- Aged Brie
- Sulfuras
- Backstages passes
- Conjured


¿Cual es el comportamiento de cada uno?
Items normales:
Quality disminuye en 1 cada día
Después de la fecha (SellIn < 0), disminuye el doble (2)
Aged Brie:
Quality aumenta con el tiempo
También respeta el límite máximo de 50
Sulfuras:
No cambia nunca
No disminuye SellIn ni Quality
Su Quality es siempre 80
Backstage passes:
Aumenta su Quality conforme se acerca el concierto:
+1 si faltan más de 10 días
+2 si faltan 10 días o menos
+3 si faltan 5 días o menos
Después del concierto (SellIn < 0), Quality = 0
Conjured:
Degradan el doble de rápido que los normales
(-2 por día, o -4 si ya pasó la fecha)




¿Que signigica sellIn?
Es el numero de dias que quedan para vender el item

¿Que significa quality?
Valor numerico que denota que tan valioso es el producto

¿Cuales son sus limites?
Quality nunca puede ser menor a 0
Quality nunca puede ser mayor a 50
Excepción:
Sulfuras siempre tiene Quality = 80

¿Cual es la restriccion mas importante sobre la clase Item?
No se puede modificar la clase Item ni la propiedad Items


¿Que nuevo item hay que implementar al final del kata?
Conjured

