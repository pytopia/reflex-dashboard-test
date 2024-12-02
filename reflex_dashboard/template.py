import reflex as rx


def navbar() -> rx.Component:
    return rx.flex(
        rx.link(rx.text("Home"), href="/"),
        rx.link(rx.text("Users"), href="/users"),
        direction="row",
        spacing="4",
    )


def footer() -> rx.Component:
    return rx.flex(
        rx.text("Copyright 2024, All rights reserved."),
        direction="row",
        spacing="4",
    )


def template(page: rx.Component) -> rx.Component:
    return rx.flex(
        navbar(),
        page(),
        footer(),
        direction="column",
        spacing="4",
    )
