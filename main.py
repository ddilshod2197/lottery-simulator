import random

class LottoSimulyator:
    def __init__(self, sonlar_soni, oyna_soni):
        self.sonlar_soni = sonlar_soni
        self.oyna_soni = oyna_soni
        self.tayyor_sonlar = set(range(1, sonlar_soni + 1))

    def oyna(self):
        oyna_sonlar = random.sample(list(self.tayyor_sonlar), self.oyna_soni)
        return oyna_sonlar

    def o'yinlash(self):
        oyna_sonlar = self.oyna()
        print(f"O'yin natijasi: {oyna_sonlar}")

    def o'yinlash_ko'p_marta(self, marta):
        for i in range(marta):
            self.o'yinlash()

simulyator = LottoSimulyator(50, 6)
simulyator.o'yinlash_ko'p_marta(10)
```

Kodda quyidagilar mavjud:

- `LottoSimulyator` classi yaratildi, u loto o'yini simulyatsiyasini amalga oshiradi.
- `sonlar_soni` va `oyna_soni` atributlari mavjud, ular loto o'yini uchun sonlar soni va har bir o'yin uchun oyna sonini belgilaydi.
- `tayyor_sonlar` atributi mavjud, u 1 dan `sonlar_soni` gacha bo'lgan sonlar to'plamini o'z ichiga oladi.
- `oyna` metodi mavjud, u random moduli yordamida oyna sonlarini yaratadi.
- `o'yinlash` metodi mavjud, u oyna natijasini konsolga chiqaradi.
- `o'yinlash_ko'p_marta` metodi mavjud, u o'yinlash metodi ni ko'p marta takrorlaydi.
- `simulyator` obyekti yaratildi, u `LottoSimulyator` classidan meros oladi.
- `o'yinlash_ko'p_marta` metodi 10 marta takrorlanadi.
