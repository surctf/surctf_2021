В таске у нас есть `сайт` и `url`, пробуем зайти на этот очень большой `url`, вылазит ошибка и просят расшифровать самому. Заходим на сайт и пробуем удлинить любую ссылку. Понимаем, что скорее всего очень много букв `o` - шифр, который возможно расшифровать. Но как? Есть несколько путей, к примеру мы могли закинуть свой `url` в `hex-редактор` и увидеть, что у буквы `o` имеют разные юникоды. Понимем, что всего 4 разных буквы `o`, предполагаем, что это `base4` (четверичная СС), пробуем перевести из `base4 -> Hex` получаем код, переводим в `ascii` и нифига себе, получаем еще одну такую же ссылку. Как это работает?!?!?!? ЭТО ЖЕ НЕВОЗМОЖНО!!!!! ЧТО МНЕ ДЕЛАТЬ???? Наверное нужно еще пару раз проделать эти действия и получить ответ в ссылке на сайт:
> http://surctf_oooo_thiiiiiiiiiiiiiiis_iiiiiiiiiiiiiis_looooooooooooong/

Или же можно было на сайте посмотреть в `ooo.js`, как кодируется и декодируется `url` и запустить функцию в js, но зачем тебе это всё???? ТЫ же и ручками можешь приколденсы делать!

Вот пример дикриптора на питоне, который работает как швейцарские часы:
```python3
url = input()
for i in range(3):
        url_rep = url.replace('o','0').replace('ο','1').replace('о','2').replace('ᴏ','3')[26:]
        url = bytearray.fromhex(hex(int(url_rep,4))[2:]).decode()
print(url[7:-1]) 
```
Запуск: `python3 dec.py < url.txt`

[dec.py](dec.py)

`Флаг: surctf_oooo_thiiiiiiiiiiiiiiis_iiiiiiiiiiiiiis_looooooooooooong`
