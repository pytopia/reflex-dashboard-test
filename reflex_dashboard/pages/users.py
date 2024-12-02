from ..template import template
import reflex as rx
from collections import Counter


class User(rx.Base):
    name: str
    email: str
    sex: str


class UserState(rx.State):
    """The app state."""

    users: list[User] = [
        User(name="John Doe", email="john.doe@example.com", sex="Male"),
        User(name="Jane Doe", email="jane.doe@example.com", sex="Female"),
    ]
    users_sex_count_data: list[dict] = [
        {"name": "Male", "value": 1},
        {"name": "Female", "value": 1},
    ]

    def add_user(self, form_data: dict):
        self.users.append(
            User(
                name=form_data["name"],
                email=form_data["email"],
                sex=form_data["sex"],
            )
        )
        self.transform_data()

    def transform_data(self):
        print("-" * 100)
        print("Transforming data")
        users_sex_count = Counter(user.sex for user in self.users)
        self.users_sex_count_data = [
            {"name": sex, "value": count} for sex, count in users_sex_count.items()
        ]


def display_user(user: User) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.sex),
    )


def form_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon(tag="plus"), rx.text("Add User"), color_scheme="green")
        ),
        rx.dialog.content(
            rx.dialog.title("Add User"),
            rx.flex(
                rx.dialog.description("Add a new user to the list"),
                rx.form(
                    rx.flex(
                        rx.input(placeholder="Name", name="name", required=True),
                        rx.input(placeholder="Email", name="email", required=True),
                        rx.select(
                            ["Male", "Female"],
                            placeholder="Male",
                            name="sex",
                            required=True,
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button("Close", variant="soft", color_scheme="gray")
                            ),
                            rx.dialog.close(
                                rx.button(
                                    "Add User", type="submit", color_scheme="green"
                                )
                            ),
                            justify="end",
                            spacing="4",
                        ),
                        direction="column",
                        spacing="4",
                    ),
                    on_submit=UserState.add_user,
                ),
                direction="column",
                spacing="4",
            ),
        ),
    )


def users_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Sex"),
            )
        ),
        rx.table.body(rx.foreach(UserState.users, display_user)),
        variant="surface",
        size="3",
    )


def graph() -> rx.Component:
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            fill=rx.color("accent", 3),
            stroke=rx.color("accent", 8),
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=UserState.users_sex_count_data,
    )


@rx.page(route="/users")
@template
def users() -> rx.Component:
    return rx.flex(
        users_table(),
        form_dialog(),
        graph(),
        direction="column",
        spacing="4",
    )
