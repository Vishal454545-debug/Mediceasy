# IP PROJECT - MEDICEASY
# VISHAL KUMAR PRADHWANI

import pandas as p
import matplotlib.pyplot as plt
from datetime import datetime

u = 0

while u == 0:

    register = input("Signup\t / \t Already a Customer: Login\n")

    # ---------------- SIGNUP ----------------
    if register == 'Signup' or register == 'signup':

        usrname = input("username: ")
        password = str(input("Password: "))

        idc = {
            'Username': [usrname],
            'Password': [password]
        }

        a = p.DataFrame(idc)

        data = p.read_csv(
            r'C:\Users\Student\Documents\Project.csv'
        )

        list1 = []

        for i in range(len(data)):
            list1.append(data['Username'][i])

        if usrname in list1:

            print("This username has already been registered.")
            print("Choose a different username or sign-up again.")

            z = 'failure'

            b = input("Do you want to go back: y/n ")

            if b == 'Y' or b == 'y':
                u = 0

            elif b == 'N' or b == 'n':
                u += 1

        elif usrname not in list1:

            a.to_csv(
                r'C:\Users\Student\Documents\Project.csv',
                index=False,
                header=False,
                mode='a'
            )

            print("Registration successful.")
            z = 'success'


    # ---------------- LOGIN ----------------
    elif (register == 'Log-in' or
          register == 'log-in' or
          register == 'login' or
          register == 'Login'):

        usrname = input("username: ")
        password = str(input("Password: "))

        data = p.read_csv(
            r'C:\Users\Student\Documents\Project.csv'
        )

        list2 = []
        list3 = []

        for i in range(len(data)):
            list2.append(data['Username'][i])
            list3.append(data['Password'][i])

        if usrname not in list2:

            print("Kindly signup.")

            z = 'failure'

            b = input("Do you want to go back: y/n ")

            if b == 'Y' or b == 'y':
                u = 0

            elif b == 'N' or b == 'n':
                u += 1

        elif (usrname in list2 and
              password != list3[list2.index(usrname)]):

            print("Your password is wrong.")
            print("Log in again or Create a new account and Sign in.")

            z = 'failure'

            b = input("Do you want to go back: y/n ")

            if b == 'Y' or b == 'y':
                u = 0

            elif b == 'N' or b == 'n':
                u += 1

        elif (usrname in list2 and
              password == list3[list2.index(usrname)]):

            print("Enjoy your shopping. You have been logged in.")

            z = 'success'


        # ============================================================
        # SHOPPING SECTION
        # ============================================================

        while z == 'success':

            ag = 'yes'
            t = 0

            i = []
            r = []
            pr = []
            to = []

            med = p.read_csv(
                r'C:\Users\student\Documents\stock.csv',
                index_col=None
            )

            st = []
            qt = []

            for ab in range(len(med)):
                st.append(med['Item Name'][ab])
                qt.append(med['Quantity'][ab])

            print("\nTime to choose your healing power")

            while ag == 'yes':

                medic = input(
                    "Select Category:\n"
                    "Eye\n"
                    "Nose\n"
                    "Fracture\n"
                    "Skin\n"
                    "Scalp\n"
                    "Mouth\n"
                    "Digestive\n"
                    "Respiratory\n"
                    "Pain\n"
                )

                # ====================================================
                # EYE
                # ====================================================

                if medic.lower() == 'eye':

                    print("1. Napal act Eye drops 5ml")
                    print("2. Itral Eye Oint")

                    e = int(input("choose 1 or 2: "))

                    if e == 1:

                        e1 = 'Napal act Eye drops 5ml'
                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 160)

                                i.append('Napal act Eye drops 5ml')
                                pr.append(q)
                                r.append(160)
                                to.append(q * 160)

                                t += q * 160

                    elif e == 2:

                        e1 = 'Itral Eye Oint'
                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 169)

                                i.append('Itral Eye Oint')
                                pr.append(q)
                                r.append(169)
                                to.append(q * 169)

                                t += q * 169


                # ====================================================
                # NOSE
                # ====================================================

                elif medic.lower() == 'nose':

                    print("1. NASOCLEAR NASAL SPRAY 20ML")
                    print("2. Nocold Syrup 60ml")

                    ns = int(input("choose 1 or 2: "))

                    if ns == 1:

                        q = int(input("Select Quantity: "))

                        e1 = 'NASOCLEAR NASAL SPRAY 20Ml'

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 50)

                                i.append('NASOCLEAR NASAL SPRAY 20Ml')
                                pr.append(q)
                                r.append(50)
                                to.append(q * 50)

                                t += q * 50

                    elif ns == 2:

                        q = int(input("Select Quantity: "))

                        e1 = 'Nocold Syrup 60ml'

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 64)

                                pr.append(q)
                                i.append('Nocold Syrup 60ml')
                                r.append(64)
                                to.append(q * 64)

                                t += q * 64


                # ====================================================
                # FRACTURE
                # ====================================================

                elif medic.lower() == 'fracture':

                    print("1. Dynamic Top Cast Plaster of Paris Bandage 25cm")
                    print("2. Accusure Electric Heating Pad")

                    f = int(input("choose 1 or 2: "))

                    if f == 1:

                        q = int(input("Select Quantity: "))

                        e1 = 'Dynamic Top Cast Plaster of Paris Bandage 25cm '

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 144)

                                pr.append(q)
                                i.append(
                                    'Dynamic Top Cast Plaster of Paris Bandage 25cm '
                                )
                                r.append(144)
                                to.append(q * 144)

                                t += q * 144

                    elif f == 2:

                        q = int(input("Select quantity: "))

                        e1 = 'Accusure Electric Heating Pad'

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 757)

                                i.append('Accusure Electric Heating Pad')
                                pr.append(q)
                                r.append(757)
                                to.append(q * 757)

                                t += q * 757


                # ====================================================
                # SKIN
                # ====================================================

                elif medic.lower() == 'skin':

                    print("1. Skin Brightening Cream Pink Lentile 50 Ml")
                    print(
                        "2. Everherb Aloe Vera Juice With Pulp - "
                        "Rejuvenates Skin & Hair - 1 Litre Bottle"
                    )

                    s = int(input("choose 1 or 2: "))

                    if s == 1:

                        q = int(input("Select Quantity: "))

                        e1 = 'Skin Brightening Cream Pink Lentile 50 Ml'

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 247)

                                i.append(
                                    'Skin Brightening Cream Pink Lentile 50 Ml'
                                )
                                pr.append(q)
                                r.append(247)
                                to.append(q * 247)

                                t += q * 247

                    elif s == 2:

                        e1 = (
                            'Everherb Aloe Vera Juice With Pulp - '
                            'Rejuvenates Skin & Hair - 1 Litre Bottle'
                        )

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 191)

                                i.append(e1)
                                pr.append(q)
                                r.append(191)
                                to.append(q * 191)

                                t += q * 191


                # ====================================================
                # SCALP
                # ====================================================

                elif medic.lower() == 'scalp':

                    print(
                        "1. Kesh King Scalp and Hair Medicine "
                        "Anti Hair fall Shampoo 80 ml"
                    )
                    print(
                        "2. Indulekha Bringha Hair Oil Bottle Of 100 Ml"
                    )

                    s = int(input("choose 1 or 2: "))

                    if s == 1:

                        e1 = (
                            'Kesh King Scalp and Hair Medicine '
                            'Anti Hair fall Shampoo 80 ml '
                        )

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 63)

                                i.append(e1)
                                pr.append(q)
                                r.append(63)
                                to.append(q * 63)

                                t += q * 63

                    elif s == 2:

                        e1 = 'Indulekha Bringha Hair Oil Bottle Of 100 Ml'

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 425)

                                i.append(e1)
                                pr.append(q)
                                r.append(425)
                                to.append(q * 425)

                                t += q * 425


                # ====================================================
                # MOUTH
                # ====================================================

                elif medic.lower() == 'mouth':

                    print("1. Listerine Cool mint Mouthwash 250 ml")
                    print(
                        "2. Kwik Mint Instant Action Mouth Freshener "
                        "Spearmint Strips - Pack Of 1 (1 X 20 G)"
                    )

                    m = int(input("choose 1 or 2: "))

                    if m == 1:

                        q = int(input("Select Quantity: "))

                        e1 = 'Listerine Cool mint Mouthwash 250 ml '

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 165)

                                i.append(
                                    'Listerine Cool mint Mouthwash 250 ml'
                                )
                                pr.append(q)
                                r.append(165)
                                to.append(q * 165)

                                t += q * 165

                    elif m == 2:

                        c = int(
                            input("1. cinamon or 2. spearmint (1/2): ")
                        )

                        if c == 1:

                            e1 = (
                                'Kwik Mint Instant Action Mouth Freshener '
                                'Spearmint Strips - Pack Of 1 (1 X 20 G)'
                                '[cinamon flavour]'
                            )

                            q = int(input("Select Quantity: "))

                            if e1 in st:

                                if q > qt[st.index(e1)]:

                                    print(
                                        "This medicine is out of stock."
                                    )

                                elif q <= qt[st.index(e1)]:

                                    qt[st.index(e1)] -= q

                                    print(
                                        "Your order costs", q * 180
                                    )

                                    i.append(e1)
                                    pr.append(q)
                                    r.append(180)
                                    to.append(q * 180)

                                    t += q * 180

                        elif c == 2:

                            e1 = (
                                'Kwik Mint Instant Action Mouth Freshener '
                                'Spearmint Strips - Pack Of 1 (1 X 20 G)'
                                '[spearmint flavour]'
                            )

                            q = int(input("Select Quantity: "))

                            if e1 in st:

                                if q > qt[st.index(e1)]:

                                    print(
                                        "This medicine is out of stock."
                                    )

                                elif q <= qt[st.index(e1)]:

                                    qt[st.index(e1)] -= q

                                    print(
                                        "Your order costs", q * 180
                                    )

                                    i.append(e1)
                                    pr.append(q)
                                    r.append(180)
                                    to.append(q * 180)

                                    t += q * 180


                # ====================================================
                # DIGESTIVE
                # ====================================================

                elif medic.lower() == 'digestive':

                    print("1. Prolyte ORS Liquid - Apple Flavour 200 ml")
                    print("2. Prolyte ORS Liquid - Orange Flavour 200 ml")

                    ch = input("Apple or Orange: ")

                    if ch.lower() == 'apple':

                        e1 = 'Prolyte ORS Liquid - Apple Flavour 200 ml'

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 20)

                                i.append(e1)
                                pr.append(q)
                                r.append(20)
                                to.append(q * 20)

                                t += q * 20

                    elif ch.lower() == 'orange':

                        e1 = 'Prolyte ORS Liquid - Orange Flavour 200 ml '

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 20)

                                i.append(e1)
                                pr.append(q)
                                r.append(20)
                                to.append(q * 20)

                                t += q * 20


                # ====================================================
                # RESPIRATORY
                # ====================================================

                elif medic.lower() == 'respiratory':

                    print("1. Dabur Talisadi Churna 60 gm")
                    print("2. Surgical Face Masks - 3ply(Pack Of 10)")

                    e = int(input("choose 1 or 2: "))

                    if e == 1:

                        e1 = 'Dabur Talisadi Churna 60 gm'

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 92)

                                i.append(e1)
                                pr.append(q)
                                r.append(92)
                                to.append(q * 92)

                                t += q * 92

                    elif e == 2:

                        e1 = 'Surgical Face Masks - 3ply(Pack Of 10)'

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 92)

                                i.append(e1)
                                pr.append(q)
                                r.append(92)
                                to.append(q * 92)

                                t += q * 92


                # ====================================================
                # PAIN
                # ====================================================

                elif medic.lower() == 'pain':

                    print("1. Volini Pain Relief Spray Bottle Of 100g")
                    print("2. Moov Pain Relief Specialist Cream 15 gm")

                    pn = int(input("choose 1 or 2: "))

                    if pn == 1:

                        e1 = 'Volini Pain Relief Spray Bottle Of 100g'

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 92)

                                i.append(e1)
                                pr.append(q)
                                r.append(92)
                                to.append(q * 92)

                                t += q * 92

                    elif pn == 2:

                        e1 = 'Moov Pain Relief Specialist Cream 15 gm'

                        q = int(input("Select Quantity: "))

                        if e1 in st:

                            if q > qt[st.index(e1)]:

                                print("This medicine is out of stock.")

                            elif q <= qt[st.index(e1)]:

                                qt[st.index(e1)] -= q

                                print("Your order costs", q * 64)

                                i.append(e1)
                                pr.append(q)
                                r.append(64)
                                to.append(q * 64)

                                t += q * 64

                else:

                    print("Invalid category selected.")


                # ====================================================
                # CONTINUE SHOPPING
                # ====================================================

                cha = input(
                    "Do you want to continue shopping? yes/no: "
                )

                if cha.lower() == 'no':
                    break

                elif cha.lower() == 'yes':
                    continue

                else:
                    break


            # ========================================================
            # BILL
            # ========================================================

            it = {
                'Item Name': i,
                'Quantity': pr,
                'Rate': r,
                'total': to
            }

            d = p.DataFrame(it)

            print("\nBill")
            print(d)

            # Add total row
            d.loc['Total'] = [' ', ' ', ' ', t]

            # Update stock
            med['Quantity'] = qt

            med.to_csv(
                r'C:\Users\student\Documents\stock.csv',
                index=False
            )

            # ========================================================
            # PERFORMANCE GRAPH
            # ========================================================

            f = input(
                "Do u want to review our performance: y/n "
            )

            if f == 'y' or f == 'Y':

                s = {
                    'January':
                    [45000, 34000, 21000, 30000, 32090,
                     39039, 28983, 43090, 40909],

                    'February':
                    [34200, 34090, 43090, 45090, 56409,
                     54698, 45690, 54099, 54309],

                    'March':
                    [23409, 32409, 45095, 24088, 87680,
                     86987, 97432, 34098, 40844],

                    'April':
                    [47987, 87631, 32498, 43797, 48796,
                     98743, 57947, 39571, 34972],

                    'May':
                    [45232, 25792, 40821, 39871, 32787,
                     29742, 29772, 24792, 27943],

                    'June':
                    [56809, 45893, 25324, 32709, 23822,
                     28367, 97342, 39287, 39827]
                }

                sales = p.DataFrame(
                    s,
                    index=[
                        'Eye',
                        'Nose',
                        'Fracture',
                        'Skin',
                        'Scalp',
                        'Mouth',
                        'Digestive',
                        'Respiratory',
                        'Pain'
                    ]
                )

                sales.plot(kind='bar')

                plt.legend()
                plt.show()

                print("\nBill")
                print(d)

                print("Your Total order costs", t)


            else:

                print(
                    "Thank you for shopping. "
                    "Hope to see you again."
                )


            # ========================================================
            # SAVE ORDER DATA
            # ========================================================

            if t != 0:

                # Remove total row before saving
                if 'Total' in d.index:
                    d.drop('Total', axis=0, inplace=True)

                d['Username'] = ' '
                d['Date & Time of order'] = ' '
                d['Total Amount'] = ' '

                # Put customer/order information in first row
                if len(d) > 0:

                    d.iloc[0, 4] = usrname
                    d.iloc[0, 5] = datetime.today()
                    d.iloc[0, 6] = t

                d.to_csv(
                    r'C:\Users\student\Documents\data.csv',
                    index=False,
                    header=False,
                    mode='a'
                )

                print("Order details saved successfully.")

            else:

                print("No order was placed.")


            # ========================================================
            # AFTER SHOPPING
            # ========================================================

            b = input("Do you want to go back: y/n ")

            if b == 'y' or b == 'Y':

                z = 'failure'
                u = 0
                break

            elif b == 'n' or b == 'N':

                print("Come back again.")

                z = 'failure'
                u += 1
                break

            else:

                print(
                    "Thank you for using the app. "
                    "Stay healthy."
                )

                z = 'failure'
                u += 1
                break


    # ================================================================
    # INVALID INITIAL OPTION
    # ================================================================

    else:

        print("Invalid option.")
        print("Please enter Signup or Login.")