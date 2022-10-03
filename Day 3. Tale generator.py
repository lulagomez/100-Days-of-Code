print('''
             ,--.
          ,--.  .--,`) )  .--,
       .--,`) \( (` /,--./ (`
      ( ( ,--.  ) )\ /`) ).--,-.
       ;.__`) )/ /) ) ( (( (`_) )
      ( (  / /( (.' "-.) )) )__.'-,
     _,--.( ( /`         `,/ ,--,) )
    ( (``) \,` ==.    .==  \( (`,-;
     ;-,( (_) ~6~ \  / ~6~ (_) )_) )
    ( (_ \_ (      )(      )__/___.'
    '.__,-,\ \     ''     /\ ,-.
       ( (_/ /\    __    /\ \_) )
        '._.'  \  \__/  /  '._.'
            .--`\      /`--.
                 '----' 
                          888                         
                          888                         
                          888                         
88888b.d88b.  .d88b.  .d88888888  888.d8888b  8888b.  
888 "888 "88bd8P  Y8bd88" 888888  88888K         "88b 
888  888  88888888888888  888888  888"Y8888b..d888888 
888  888  888Y8b.    Y88b 888Y88b 888     X88888  888 
888  888  888 "Y8888  "Y88888 "Y88888 88888P'"Y888888 
''')
print("Welcome to Medusa.")
print("Your mission is to find the Gorgone.")


a = input("\nYou're an Amazona warrior and you need to find Medusa to break her curse. \nYou can start your way right NOW, or you can go before to ask the ORACULOUS. \nWhat do you choose? NOW/ORACULOUS: ")
a_l = a.lower()
if a_l == "oraculous":
    b = input("\nWell done! The Oraculous says you must LEAVE your belongings behind, \nand gives you just a little knife to go on. \nYou doubt because you have a lot of GOLD and food for the travel. \nWhat do yo do? LEAVE/GOLD: ")
    b_l = b.lower()
    if b_l == "leave":
        c = input("\nYou didn't need all that weight! You arrive to a lonely lake, \nand spot a little boat with an ancient driver. \nHe tells you that could take you to Medusa's cavern \nif you give him five YEARS of your life. \nOtherwhise you could swim and arrive by YOURSELF. \nWhat is your choice? YEARS/YOURSELF ")
        c_l = c.lower()
        if c_l == "years":
            d = input("\nThe ancient man didn't smells good, and the years of life are infinitely valuable, but you took a great decision! \nNow you found Medusa. You can't look at her because you don't want to become a rock, \nbut she tells you that if you RESCUE her \ncutting her ties with your little knife, \nshe won't hurt you and will help you to come back home. \n\nOn the other hand, you know that Medusa's head \nmeans a millionaire reward \nand could transform you in a HERO at the capital city. \n\nAnd is also posible to run away, \nforget everything and dedicate yourself \nto taking care of SHEEP in your town. \nWhat is your will? RESCUE/HERO/SHEEP: ")
            d_l = d.lower()
            if d_l == "rescue":
                print("\nThis really made you a hero! \nYou rescued Medusa, you broke the unfair curse spelled on her, \nand you two became great friends, \nand now you travel together helping oppressed women around the world!\nCONGRATULATIONS! YOU WIN!")
            elif d_l == "hero":
                print("\nReally? Come on! \nGAME OVER")
            elif d_l == "sheep":
                print("\nWell, ok, simple life is good life, but... \nGAME OVER")
            else:
                print("\nGAME OVER")
        else:
            print("\nYou, crazy foolish! Charybdis, the sea monster, \ncame to the lake for vacation and created deadly whirlpools \nthat made you never come back home again. \nGAME OVER")
    else:
        print("\nYour avarice took you to the most stupid death! \nYour food's smell atracted the Stymphalian Birds, \nthat devored you in seconds beacuse you couldn't run \nfor the weight of your gold. \nGAME OVER")
else:
    print("\nThe night arrived and the Cyclope found you lost in the forest. \nSay goodbye to your head! Nyam nyam! \nGAME OVER)
