from django.db.models import QuerySet

import init_django_orm  # noqa: F401
from db.models import Actor, Genre


def main() -> QuerySet:
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_to_create:
        Genre.objects.create(name=genre_name)

    actors_to_create = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    for first_name, last_name in actors_to_create:
        Actor.objects.create(first_name=first_name, last_name=last_name)

    new_drama = Genre.objects.filter(name="Dramma").update(name="Drama")
    new_clooney = Actor.objects.filter(last_name="Klooney").update(
        last_name="Clooney"
    )
    new_keanu = Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu", last_name="Reeves"
    )
    delete_scarlett = Actor.objects.filter(first_name="Scarlett").delete()
    delete_action = Genre.objects.filter(name="Action").delete()

    __all__ = [
        new_drama,
        new_clooney,
        new_keanu,
        delete_scarlett,
        delete_action,
        main,
    ]
    __all__
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
