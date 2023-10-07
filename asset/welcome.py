import discord
from discord.ext import commands
from discord import File
from easy_pil import Editor, Font, load_image
from num2words import num2words
import random
import os

def welcome_member(member:discord.Member):

    pos = sum(m.joined_at < member.joined_at for m in member.guild.members
        if m.joined_at is not None)

    if pos == 1:
        te = "st"
    elif pos == 2:
        te = "nd"
    elif pos == 3:
        te = "rd"
    else:
        te = "th"

    # list of possible background images
    bg1 = os.path.join('asset','Images','wlcbg.jpg')
    bg2 = os.path.join('asset','Images','wlcbg2.jpg')
    bg3= os.path.join('asset','Images','wlcbg3.jpg')
    backgrounds = [bg1,bg2,bg3]

        # randomly select a background image
    random.shuffle(backgrounds)

    font_rose = os.path.join('asset','Fonts','rose.ttf')
    font_bazoka = os.path.join('asset','Fonts','bazoka.ttf')       
    rose = Font(font_rose, size=40)
    rose1 = Font(font_rose, size=30)
    bazoka = Font(font_bazoka, size=30)

    for selected_background in backgrounds:

        background = Editor(selected_background)

        # Card 1
        if selected_background == bg1:
            background = Editor(bg1)
            profile_image = load_image(str(member.display_avatar.url))

            profile = Editor(profile_image).resize((200, 200)).circle_image()
            background.paste(profile, (175, 100))
            background.ellipse(
                (175, 100),
                200,
                200,
                outline="#e68694",
                stroke_width=8,
            )

            background.text(
                (300, 350),
                "Welcome to Your New Home",
                color="#ff7f87",
                font=rose,
                align="center",
            )

            background.text(
                (300, 410),
                f"{member.guild.name}",
                color="#e68694",
                font=bazoka,
                align="center",
            )

            background.text(
                (300, 450),
                f"You Are The {pos}{te} Member",
                color="#e2973f",
                font=rose1,
                align="center",
            )
            #Use elif when adding more pitures
        elif selected_background == bg3:
            background = Editor(bg3)
            profile_image = load_image(str(member.display_avatar.url))

            profile = Editor(profile_image).resize((200, 200)).circle_image()
            background.paste(profile, (580, 120))
            background.ellipse(
                (580, 120),
                200,
                200,
                outline="#1f5db6",
                stroke_width=8,
            )

            background.text(
                (650, 350),
                "Welcome to Your New Home",
                color="#1f5db6",
                font=rose,
                align="center",
            )

            background.text(
                (650, 410),
                f"{member.guild.name}",
                color="#8c75b9",
                font=bazoka,
                align="center",
            )

            background.text(
                (650, 450),
                f"You Are The {pos}{te} Member",
                color="#e088aa",
                font=rose1,
                align="center",
            )
        elif selected_background == bg2: 
            background = Editor(bg2)
            profile_image = load_image(str(member.display_avatar.url))

            profile = Editor(profile_image).resize((200, 200)).circle_image()
            background.paste(profile, (590, 100))
            background.ellipse(
                (590, 100),
                200,
                200,
                outline="#a69cd3",
                stroke_width=8,
            )

            background.text(
                (670, 350),
                "Welcome to Your New Home",
                color="#8c7fc4",
                font=rose,
                align="center",
            )

            background.text(
                (670, 410),
                f"{member.guild.name}",
                color="#ffadbc",
                font=bazoka,
                align="center",
            )
            background.text(
                    (670, 450),
                f"You Are The {pos}{te} Member",
                color="#f9b9a9",
                font=rose1,
                align="center",
            )

    return background.image_bytes

