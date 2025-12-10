import math

print("SUPER kalkulyatorga xush kelibsiz, Begim! 💚")

tarix = []  # hisoblashlar tarixini saqlaymiz


def son_olish(savol):
    """Foydalanuvchidan son olish, xato bo'lsa qayta so'raydi"""
    while True:
        qiymat = input(savol)
        try:
            return float(qiymat)
        except ValueError:
            print("❌ Iltimos faqat son kiriting!")


def hisoblash(amal, a, b=None):
    """Turli amallarni bajarish"""
    if amal == "1":      # qo'shish
        return a + b, "+"
    elif amal == "2":    # ayirish
        return a - b, "-"
    elif amal == "3":    # ko'paytirish
        return a * b, "*"
    elif amal == "4":    # bo'lish
        if b == 0:
            return "0 ga bo'lish mumkin emas!", "/"
        return a / b, "/"
    elif amal == "5":    # daraja
        return a ** b, "^"
    elif amal == "6":    # foiz: a ning b foizi
        return (a * b) / 100, "%(foiz)"
    elif amal == "7":    # modulus (qoldiq)
        if b == 0:
            return "0 ga bo'lish mumkin emas!", "%(qoldiq)"
        return a % b, "%(qoldiq)"
    elif amal == "8":    # kvadrat ildiz
        if a < 0:
            return "Manfiy sondan haqiqiy ildiz yo'q!", "√"
        return math.sqrt(a), "√"
    elif amal == "9":    # faktorial
        if a < 0 or int(a) != a:
            return "Faktorial faqat 0 yoki musbat butun son uchun!", "!"
        return math.factorial(int(a)), "!"
    elif amal == "10":   # sin (gradusda)
        return math.sin(math.radians(a)), "sin"
    elif amal == "11":   # cos (gradusda)
        return math.cos(math.radians(a)), "cos"
    elif amal == "12":   # tan (gradusda)
        return math.tan(math.radians(a)), "tan"

    return "Noma'lum amal", "?"


while True:
    print("\n--- SUPER MENYU ---")
    print("1) Qo'shish          (a + b)")
    print("2) Ayirish           (a - b)")
    print("3) Ko'paytirish      (a * b)")
    print("4) Bo'lish           (a / b)")
    print("5) Daraja            (a ^ b)")
    print("6) Foiz              (a ning b foizi)")
    print("7) Modulus           (a % b, qoldiq)")
    print("8) Kvadrat ildiz     (√a)")
    print("9) Faktorial         (n!)")
    print("10) Sinus (gradusda)")
    print("11) Cosinus (gradusda)")
    print("12) Tangens (gradusda)")
    print("13) O'rtacha qiymat (bir nechta son)")
    print("14) BMI (vazn/bo'y)")
    print("15) Tarixni ko'rish")
    print("16) Chiqish")

    tanlov = input("Amalni tanlang (1-16): ")

    if tanlov == "16":
        print("Dastur tugadi. Xayr, Begim! 👋")
        break

    # Tarix
    if tanlov == "15":
        print("\n--- HISOBLASH TARIXI ---")
        if not tarix:
            print("Hozircha hech qanday hisob yo'q 😊")
        else:
            for item in tarix:
                print("•", item)
        continue

    # O'rtacha qiymat
    if tanlov == "13":
        satr = input("Sonlarni bo'sh joy bilan kiriting (mas: 1 2 3 4): ")
        try:
            sonlar = [float(x) for x in satr.split()]
            if not sonlar:
                print("Hech narsa kiritilmadi.")
                continue
            o_rta = sum(sonlar) / len(sonlar)
            print("✅ O'rtacha qiymat:", o_rta)
            tarix.append(f"avg({sonlar}) = {o_rta}")
        except ValueError:
            print("❌ Faqat sonlardan foydalaning.")
        continue

    # BMI
    if tanlov == "14":
        vazn = son_olish("Vazningizni kiriting (kg): ")
        boy = son_olish("Bo'yingizni kiriting (metrda, mas: 1.70): ")
        if boy <= 0:
            print("Bo'y 0 dan katta bo'lishi kerak.")
            continue
        bmi = vazn / (boy ** 2)
        print("✅ BMI:", round(bmi, 2))
        if bmi < 18.5:
            holat = "Ozginaroq"
        elif bmi < 25:
            holat = "Normal"
        elif bmi < 30:
            holat = "Ortacha semizlik"
        else:
            holat = "Semizlik"
        print("Holat:", holat)
        tarix.append(f"BMI (v={vazn}kg, h={boy}m) = {round(bmi,2)} ({holat})")
        continue

    # Kvadrat ildiz / faktorial / trig – bitta son
    if tanlov in ["8", "9", "10", "11", "12"]:
        a = son_olish("Sonni kiriting: ")
        natija, belgi = hisoblash(tanlov, a)
        print("✅ Natija:", natija)

        if isinstance(natija, (int, float)):
            if belgi in ["sin", "cos", "tan"]:
                tarix.append(f"{belgi}({a}°) = {natija}")
            elif belgi == "√":
                tarix.append(f"√{a} = {natija}")
            elif belgi == "!":
                tarix.append(f"{int(a)}! = {natija}")
        continue

    # Qolganlari – 2 ta sonli amallar
    if tanlov in ["1", "2", "3", "4", "5", "6", "7"]:
        a = son_olish("1-sonni kiriting: ")
        b = son_olish("2-sonni kiriting: ")
        natija, belgi = hisoblash(tanlov, a, b)
        print("✅ Natija:", natija)

        if isinstance(natija, (int, float)):
            if belgi.startswith("%(foiz"):
                s = f"{b}% of {a} = {natija}"
            elif belgi.startswith("%(qoldiq"):
                s = f"{a} % {b} = {natija}"
            else:
                s = f"{a} {belgi} {b} = {natija}"
            tarix.append(s)
        continue

    # Boshqa narsa yozilsa:
    print("❌ Noto'g'ri tanlov! 1 dan 16 gacha son kiriting.")
