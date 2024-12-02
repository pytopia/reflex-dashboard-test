import reflex as rx
from ..template import template


@rx.page(route="/")
@template
def index() -> rx.Component:
    return rx.flex(
        rx.image(src="favicon.ico"),
        rx.heading("Hello! Welcome to Reflex Dashboard"),
        rx.list.ordered(
            rx.list.item(rx.link(rx.text("Go to users"), href="/users")),
            direction="column",
            spacing="4",
        ),
        direction="column",
        spacing="4",
    )
