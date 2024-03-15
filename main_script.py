import sys
import os
import random
import webbrowser
import speech_recognition as sr
import flet as ft
import openai
from openai import OpenAI 
import asyncio
from openai import AsyncOpenAI

def main(page: ft.Page):
    # Create the icon bar
    icon_bar = ft.IconBar(
        [
            ft.IconItem(
                icon=ft.icons.INFO,
                tooltip="Information",
                on_click=lambda e: page.update_controls(["info_panel.visible = True"]),
            ),
            ft.IconItem(
                icon=ft.icons.SETTINGS,
                tooltip="Settings",
                on_click=lambda e: page.update_controls(["settings_panel.visible = True"]),
            ),
        ]
    )

    # Create the info panel
    info_panel = ft.Ref(ft.Column(controls=[ft.Text("Information panel")]))

    # Create the settings panel
    settings_panel = ft.Ref(ft.Column(controls=[ft.Text("Settings panel")]))

    # Create the type bar
    type_bar = ft.Ref(ft.TextField(label="Type a message"))

    # Create the send button
    send_button = ft.Ref(ft.ElevatedButton("Send", on_click=send_message))

    # Create the main column
    main_column = ft.Ref(ft.Column(controls=[icon_bar, type_bar, send_button, info_panel, settings_panel]))

    # Set the initial visibility of the info and settings panels
    page.controls[0].controls[1].visible = False
    page.controls[0].controls[3].visible = False

    def send_message(e):
        message = type_bar.current_value
        # Add your code here to send the message
        type_bar.value = ""

    page.add(main_column)

if __name__ == "__main__":
    ft.app(target=main)