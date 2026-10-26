from flask import render_template, request, redirect, url_for, flash

from app.models.task import ShoeModel


class ShoeController:
    def __init__(self):
        self.model = ShoeModel()

    def index(self):
        shoes = self.model.get_all_shoes()
        return render_template("tasks/index.html", shoes=shoes)

    def store(self):
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        price_input = request.form.get("price", "0").strip()

        try:
            price = float(price_input.replace(",", "."))
        except ValueError:
            price = 0

        if not name or not description or price <= 0:
            flash(
                "Введіть назву, опис і ціну, більшу за нуль.",
                "error"
            )
            return redirect(url_for("index"))

        if self.model.add_shoe(name, description, price):
            flash("Взуття успішно додано!", "success")
        else:
            flash("Не вдалося додати товар.", "error")

        return redirect(url_for("index"))

    def delete(self, shoe_id: int):
        if self.model.delete_shoe(shoe_id):
            flash("Товар успішно видалено!", "success")
        else:
            flash("Товар не знайдено.", "error")

        return redirect(url_for("index"))