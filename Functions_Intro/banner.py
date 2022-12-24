def banner_text(text: str = "",width: int = 80) -> None:
    """
    Centers the text inside the banner which is enclosed by **
    :param text: The text that must be placed inside the banner
    :param width: The screem width of the banner
    :raise: If the string is not long enough
    """
    screen_width = width
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*",30)
banner_text("Always look on the bright side of life...",80)
banner_text("If life seems jolly rotten,", 50)
banner_text("There's something you've forgotten!",80)
# banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text("When you're feeling in the dumps,")
# banner_text("Don't be silly chumps,")
# banner_text("Just purse your lips and whistle - that's the thing!")
# banner_text("And... always look on the bright side of life...")
# banner_text("*")
